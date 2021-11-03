# October-4th_week-codes

- [ ] 1. **25th Oct** - ~~_NULL_~~
- [ ] 2. **26th Oct** - ~~_NULL_~~
- [ ] 3. **27th Oct** - ~~_NULL_~~
- [ ] 4. **28th Oct** - ~~_NULL_~~
- [ ] 5. **29th Oct** - ~~_NULL_~~
- [x] 6. **30th Oct**
     

     - PRAW( _Python Reddit API Wrapper_ )
       > [Subreddit](https://praw.readthedocs.io/en/latest/code_overview/models/subreddit.html)
       - currently working on [matej2/location-info](https://github.com/matej2/location-info)
     
     ```
     import praw
     
     reddit = praw.Reddit(client_id =os.environ.get("id"),
                     client_secret =os.environ.get("secret"),
                     user_agent ='random bullshit go brrr...')

     print(reddit.read_only)
     ```
 - [ ] 7. **31th Oct** - ~~_NULL_~~
