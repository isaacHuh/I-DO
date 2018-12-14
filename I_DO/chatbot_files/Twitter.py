from twitter import *

class Tweet():
	def __init__(self, status = "hi"):
		self.status = status
		self.consumer_key = '4kg4eV9f3VcYa28s6dGbkxY0z'
		self.consumer_secret = 'JBRoZBk9LYNYo719gSyD9mDqFg8mPLKYXHrzdtG84wPtWWfazx'
		self.access_token = '1072634264787705858-ZL327BPRaGUek76uNKOEj9lhP6XEnZ'
		self.access_secret = 'OhVUcpxw1zvGrX5JlkSqj7aeDVC9uHOB8XhjzFsfjriDq'
		self.send_tweet()

	def send_tweet(self):
		tweet = Twitter(auth=OAuth(self.access_token, self.access_secret, self.consumer_key, self.consumer_secret))
		tweet.statuses.update(status = self.status)

