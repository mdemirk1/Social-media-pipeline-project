import requests
import json

class Client:
    def __init__(self):
        # database
        # self.config = {
        # 'user': 'root',
        # 'password': 'root',
        # 'host': '127.0.0.1',
        # 'port': 8886,
        # 'database': 'redditapitest',
        # 'raise_on_warnings': True
        # }
        # self.cnx = mysql.connector.connect(**self.config)
        # self.cursor = self.cnx.cursor(dictionary=True)

        # reddit api
        self.client_id = 'fzCho4moUq-JjcpIsixHig'
        self.client_secret = 'loL5vwSt7d2GtSx2KK2rAbUoMqRw_A'
        self.auth = requests.auth.HTTPBasicAuth(self.client_id, self.client_secret)
        self.headers = {'User-Agent' : 'api_project/0.1'}
        self.data = {
            'grant_type' : 'password',
            'username' : 'doraxy6120',
            'password' : 'Dorademirkir'
        }
        self.res = requests.post('https://www.reddit.com/api/v1/access_token', auth=self.auth, data=self.data, headers=self.headers)
        self.token = self.res.json()['access_token']
        self.headers['Authorization'] = f'bearer {self.token}'
        # now we can access every endpoint in reddit api.
        # requests.get('https://oauth.reddit.com/api/v1/me', headers=headers).json()

    def get_posts(self):
        res = requests.get('https://oauth.reddit.com/r/CryptoCurrency/hot', headers=self.headers, params={'limit' : '10'})
        posts = []
        for post in res.json()['data']['children']:
            post_id = post['kind'] + '_' + post['data']['id']
            post_title = post['data']['title']
            post_title = post_title.replace("‘","")
            post_title = post_title.replace("’","")
            post_title = post_title.replace("'","")
            post_ups = post['data']['ups']
            post_tuple = (post_id, post_title, post_ups)
            posts.append(post_tuple)
            # if we put ups into tuple, little problem arises
            # when we look into list difference, even though id and title are same
            # when ups change, the item becomes different and it is put into new items list
            # which is wrong, one solution is not putting ups but it limits our functionality
            # the other solution is (extra check) checking if title and id same. If yes, dont put it.
        return posts

    def get_comments(self, post_id):
        frame_url = 'https://oauth.reddit.com/r/CryptoCurrency/comments/'
        full_url = frame_url + post_id
        res = requests.get(full_url, headers=self.headers, params={'limit' : '3'})
        # limit indicates how many comments we get
        # res returns a list of 2 objects
        # comment texts are found in res[1][data][children]
        # each element of this children is comment and their data->body shows the text except the last one
        # comment texts are found in 
        # comment id can be accessed changing the ['body'] below to the ['name'].
        comments = []
        res.raise_for_status()
        data = res.json()
        # print(json.dumps(data, indent=4))
        # print(len(data[1]["data"]["children"]))
        for i in range(len(data[1]['data']['children'])-1):            
            comment_text = data[1]['data']['children'][i]['data']['body']
            comment_id = data[1]['data']['children'][i]['data']['name']
            print(f'Comment id -> {comment_id}  Comment text -> {comment_text}')
        return comments