import tweepy
import time

ACCESS_TOKEN = '725129866761359360-NChA607PWMuyYVX9A3GwG9zXQ6PohJh'
ACCESS_SECRET = 'iZtMOJNFwfGUlFmjt632qpmprCGqRgcGOopSm8i4SOa94'
CONSUMER_KEY = 'pDnm5Z5MFjQFVmfrSZVpflZ9b'
CONSUMER_SECRET = 'lyAiTEb0xpQDSdrIpG88u1s80OvJqH2FPCDbLyCt0rGx8IBqTB'
SEARCH=input("Enter the search string ")
FROM=input("Enter the from date (YYYY-MM-DD format) ")
TO=input("Enter the to data (YYYY-MM-DD format) ")
INPUT_FILE_PATH= './'+SEARCH+'.txt'

num=int(input("Enter the number of tweets you want to retrieve for the search string "))
auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
i=0;

f = open(INPUT_FILE_PATH, 'w', encoding='utf-8')

for res in tweepy.Cursor(api.search, q=SEARCH, rpp=100, count=20, result_type="recent", since = FROM,until =TO, include_entities=True, lang="en").items(num):
	i+=1
	f.write(res.user.screen_name)
	f.write(' ')
	f.write('[')
	f.write(res.created_at.strftime("%d/%b/%Y:%H:%M:%S %Z"))
	f.write(']')
	f.write(" ")
	f.write('"')
	f.write(res.text.replace('\n',''))
	f.write('"')
	f.write(" ")
	f.write(str(res.user.followers_count))
	f.write(" ")
	f.write(str(res.retweet_count))
	f.write('\n')
	f.flush()

f.close()
print("Tweets retrieved ",i)
