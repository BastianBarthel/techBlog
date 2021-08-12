import requests


class Post:

    def __init__(self):
        self.all_posts = requests.get("https://api.npoint.io/e65d40199cd45175cd03").json()
