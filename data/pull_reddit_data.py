import os
import sys
from psaw import PushshiftAPI  # API wrapper for pushshift.io
import datetime
import pandas as pd


posted_after = int(datetime.datetime(2020, 1, 1).timestamp())  # Y:M:D
posted_before = int(datetime.datetime(2021, 1, 1).timestamp())

api = PushshiftAPI()  # entry point for request

# pull data
query = api.search_submissions(subreddit='nyc', after=posted_after, before=posted_before, limit=10000)
# 'nyc' or 'washingtondc'

# save data
submissions = list()
for element in query:
    submissions.append(element.d_)
df = pd.DataFrame(submissions)

# columns=['id', 'author', 'created_utc', 'domain', 'url', 'title', 'score', 'selftext', 'num_comments',
# 'num_crossposts', 'full_link']
columns = ['author', 'author_fullname', 'created_utc', 'title', 'score', 'selftext', 'num_comments']  # columns to save

df.to_csv('typenamehere.csv', sep=';', header=True, index=False, columns=columns)


if __name__ == '__main__':
    print(len(submissions))

# https://deepnote.com/@deepnote/Mining-and-Exploring-Reddit-Data-using-Python-rfZ7TRRAT2unpCqU6egaKA
