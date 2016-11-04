# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

import tweepy
import nltk

cons_key = 'LSyEcZXGuzkC5ROdGDOOqFmNe'
cons_sec = 'GcnLqTnfHR78zBMImkH7VwCL84pJAQbCHi95cJRqCITsIdlOia'
accs_tok = '746391890174550016-kfNzCZopGwTBo4mvkCGoZLgvaajxalL'
accs_sec = 'lheX9mXZCzbU3jDMiGVXI7msij1k8Jys7IIwnm2ry5Ab9'

auth = tweepy.OAuthHandler(cons_key, cons_sec)
auth.set_access_token(accs_tok, accs_sec)

api = tweepy.API(auth)


update_status = api.update_with_media("pink-logo.png", "#UMSI206 #Proj3")


print("""No output necessary although you 
	can print out a success/failure message if you want to.""")