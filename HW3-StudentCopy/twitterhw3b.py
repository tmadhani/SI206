# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.
import tweepy
import nltk
from textblob import TextBlob

access_token = "746391890174550016-kfNzCZopGwTBo4mvkCGoZLgvaajxalL"
access_token_secret = "lheX9mXZCzbU3jDMiGVXI7msij1k8Jys7IIwnm2ry5Ab9"
consumer_key = "LSyEcZXGuzkC5ROdGDOOqFmNe"
consumer_secret = "GcnLqTnfHR78zBMImkH7VwCL84pJAQbCHi95cJRqCITsIdlOia"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

public_tweets = api.search('elections2016')
count = 0
# for tweet in public_tweets:
# 	print(tweet.text)
for item in public_tweets:
	analysis = TextBlob(item.text)
	count = count + analysis.sentiment.subjectivity
print("Average subjectivity is " + str(count/len(public_tweets)))
new_count = 0
for item in public_tweets:
	analysis = TextBlob(item.text)
	new_count = new_count + analysis.sentiment.polarity
print("Average polarity is " + str(new_count/len(public_tweets)))
	
#Learn more about Search
#https://dev.twitter.com/rest/public/search


# 
# print("Average subjectivity is")
# print("Average polarity is")
