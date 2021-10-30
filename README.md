# October-4th_week-codes

6. **30th Oct**
     

     - PRAW( _Python Reddit API Wrapper_ )
       > [Subreddit](https://praw.readthedocs.io/en/latest/code_overview/models/subreddit.html)
       - currently working on [matej2/location-info](https://github.com/matej2/location-info)
     
     ```
     import praw
     
     reddit = praw.Reddit(client_id =os.environ.get("id"),
                     client_secret =os.environ.get("secret"),
                     user_agent ='my user agent')

     print(reddit.read_only)
     ```
    
 
