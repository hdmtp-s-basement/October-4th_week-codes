import praw
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

reddit = praw.Reddit(client_id =os.environ.get("id"),
                     client_secret =os.environ.get("secret"),
                     user_agent ='my user agent')

print(reddit.read_only)

subreddit = reddit.subreddit('callofduty')
print(subreddit.display_name)
print(subreddit.title)
#print(subreddit.description)

'''
redditor = reddit.redditor('Fish_Fucker69')
print(redditor.link_karma)
'''

for post in reddit.subreddit("memes").hot(limit=5):
	print(post.title)
	print("\n")

'''
for collection in reddit.subreddit("IndianDankMemes").collections:
    print(collection.permalink)
'''

# glided = awards bought with real moni
for item in reddit.subreddit("IndianDankMemes").gilded():
    print(item.id)
  	

for wikipage in reddit.subreddit("memes").wiki:
    print(wikipage)


wikipage = reddit.subreddit("memes").wiki["config/sidebar"]
print(wikipage.content_md)