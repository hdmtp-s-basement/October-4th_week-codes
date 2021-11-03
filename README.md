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

<hr>
<div align="center">

Day      | Score
:--------------:|:----------------:
**25th Oct** | **0**
**26th Oct** | **0**
**27th Oct** | **0**
**28th Oct** | **0**
**29th Oct** | **1**
**30th Oct** | **0**
**31th Oct** | **0**
***Total***     | ***1***
     
</div>
<hr>
<!--Below part needs to be edited-->
Here is a simple footnote[^1].

A footnote can also have multiple lines[^2].  

You can also use words, to fit your writing style more closely[^note].

[^1]: My reference.
[^2]: Every new line should be prefixed with 2 spaces.  
  This allows you to have a footnote with multiple lines.
[^note]:
    Named footnotes will still render with numbers instead of the text but allow easier identification and linking.  
    This footnote also has been made with a different syntax using 4 spaces for new lines.
