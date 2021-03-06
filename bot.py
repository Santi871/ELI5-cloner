import praw
import OAuth2Util

FROM_SUBREDDIT = 'explainlikeimfive'
TARGET_SUBREDDIT = 'ELI5_clone'

r = praw.Reddit('windows:ELI5-cloner v1 by /u/santi871 | https://github.com/Santi871/ELI5-cloner')
o = OAuth2Util.OAuth2Util(r)
o.refresh(force=True)

while True:

    try:
        for submission in praw.helpers.submission_stream(r, FROM_SUBREDDIT, limit=10, verbosity=0):

            try:
                r.submit(TARGET_SUBREDDIT, submission.title, text=submission.body)
            except AttributeError:
                r.submit(TARGET_SUBREDDIT, submission.title, text='')

            print("Mirrored submission: " + submission.title)

    except Exception as e:
        print(e)

