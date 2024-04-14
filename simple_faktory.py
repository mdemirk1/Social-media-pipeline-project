import faktory
import logging
import time
import datetime
from faktory import Worker
from reddit_api_class import Client
import psycopg2
import os

faktory_url = "tcp://:password@localhost:7419"
my_client = Client()
posts_to_be_added = []
posts_list_old = my_client.get_posts()

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')

def get_posts_wrapper():
    logging.info(f'get_posts_wrapper()')
    global posts_list_old
    posts_list_new = my_client.get_posts()
    # print("10 posts on hot")
    # print(*posts_list_new, sep='\n')
    # print("----")
    for new_item in posts_list_new:
        not_new = False
        for old_item in posts_list_old:
            if new_item[0] == old_item[0]:
                # same id item found, not a new post
                not_new = True
        if not_new == False:
            posts_to_be_added.append(new_item)
            # When the list becomes big, put it into the database
            # and empty the list for potential memory issues.
    print(*posts_to_be_added, sep='\n')
    posts_list_old = posts_list_new
    print("---------")
    # test_id = 1
    # test_post_id = 2
    # test_title = "test"
    # test_date = "04:05:06.789-8"
    # test_date_created = "04:05:06.789-8"

    # # Database connection parameters
    # db_params = {
    #     "host": os.getenv("DB_HOST"),
    #     "database": os.getenv("DB_NAME"),
    #     "user": os.getenv("DB_USER"),
    #     "password": os.getenv("DB_PASSWORD"),
    #     "port": os.getenv("DB_PORT")
    # }


    # sql = 'INSERT INTO realcrawlers_api_reddit (id, post_id, title, date, date_created) VALUES (%s, %s, %s, %s, %s)'
    # try:
    #     # Connect to the database
    #     connection = psycopg2.connect(**db_params)
    #     cursor = connection.cursor()

    #     # Execute the INSERT query
    #     cursor.execute(sql, (test_id, test_post_id, test_title, test_date, test_date_created))

    #     # Commit the transaction
    #     connection.commit()

    #     print("Row inserted successfully")

    # except (Exception, psycopg2.Error) as error:
    #     print("Error inserting row:", error)

    # finally:
    #     if connection:
    #         cursor.close()
    #         connection.close()
    

# main func.
if __name__ == "__main__":
    # get_posts_wrapper()
    w = Worker(faktory=faktory_url, queues=["posts"], concurrency=1, use_threads=True)
    w.register("new_post", get_posts_wrapper)
    w.run()
  
