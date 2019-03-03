import tweepy
import csv

consumer_key = 'XXXX'
consumer_secret = 'XXXX'
access_key = 'XXXX'
access_secret = 'XXXX'

screen_name = 'putln2'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

tweets = {}

print('Getting tweets')
c = 0
for tweet in tweepy.Cursor(api.user_timeline, screen_name=screen_name).items():
    tweets.update({c: {'date': tweet.created_at, 'text': tweet.text}})
    c += 1

print('Building CSV')
for item in tweets.items():
    date = item[1]['date'].year
    with open(f'zzz/{screen_name}_{date}.csv', mode='w') as f:
        w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        w.writerow([item[1]['date'], item[1]['text']])

total = len(tweets)
print(f'Wrote {total} tweets to file')
