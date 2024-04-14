import time
import faktory

faktory_url = "tcp://:password@localhost:7419"

with faktory.connection(faktory_url) as client:
    while True:
        client.queue("new_post", queue="posts")
        time.sleep(300)
