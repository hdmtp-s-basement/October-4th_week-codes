import praw
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

reddit = praw.Reddit(client_id =os.environ.get("id"),
                     client_secret =os.environ.get("secret"),
                     user_agent ='random bullshit go brrrr...')

print(reddit.read_only)

subreddit = reddit.subreddit('hdmtp645466')
print(subreddit.display_name)
print(subreddit.title)
#print(subreddit.description)

'''
redditor = reddit.redditor('Fish_Fucker69')
print(redditor.link_karma)
'''

for post in reddit.subreddit("ASUS").hot(limit=5):
	print(post.title)
	print("\n")

'''
for collection in reddit.subreddit("IndianDankMemes").collections:
    print(collection.permalink)
'''

# glided = awards bought with real moni
for item in reddit.subreddit("india").gilded():
    print(item.id)
  	
'''
for wikipage in reddit.subreddit("memes").wiki:
    print(wikipage)


wikipage = reddit.subreddit("memes").wiki["index/banappeals"]
print(wikipage.content_md)
'''

submission = reddit.subreddit("indiandankmemes").random()
print("\n"+submission.title)

for submission in reddit.subreddit("indiandankmemes").random_rising():
    print(submission.title)