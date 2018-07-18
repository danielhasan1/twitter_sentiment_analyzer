import tweepy
from textblob import TextBlob
#login via code
#these are keys which are a gateway for accessing tweeters internal sever function
#keys are altered if you wanna write your own script then you have to just create your app with twitter by filling some authentication info..And they will provide you tokens and keys.
consumer_key = 'bhjI8T7b8urptGWaEJDwLUchuN'
consumer_secret = 'dAklPnRQy4yxQ4k1RPfQZ6bs3cuty6rpsbaVLRUQt4MHPnuLduv'
access_token = '882462301722263553-NKq3FiadxbXMQ3puhTmGKFb55noH0vQf'
access_token_secret = 'NrI9EphybWgvnIhVxlCMKQwES0dPQSvxC5vHFVHTeLzahs'

#accessing the authhandler attribute of tweepy liabrary which will allow us to get authenticated
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
#call token method on auth variable
auth.set_access_token(access_token,access_token_secret)
#this variable will allow us to access whole bunch of diffrent methods
api = tweepy.API(auth)
#create
#search
#find_tweets
#we gonna search for tweets
#create a tweet variable which will store the list  of tweets
#search method of the api variable will take a single argument 
public_tweet = api.search('TRUMP')
#this method will give a bunch of tweets that's related to the argument
#now we can print all tweets out or perform a bunch of operations
#each tweet has a text attribute
for tweet in public_tweet:
	print(tweet.text)
	#here we will call the TextBlob module which will perform its pre written liabrary functions and perfrom the analysis
	analysis = TextBlob(tweet.text)
	#now we can just call the sentiment sentiment attribute to know its polarity and subjectivity
	#polarity will give you how much positive or negative the text is.
	#and subjectivity will give you how much of a opinion it is or how factual
	print(analysis.sentiment)



#for example above search will result in this

#@ambika1900 @NetflixAndLamp And another board member probably doesn’t want to hear about such topics in the first p… https://t.co/p0MSJOPJv2
#Sentiment(polarity=0.125, subjectivity=0.41666666666666663)
#Elon Musk apologizes for calling member of Thai cave rescue team ‘pedo guy’ in flurry of tweets… https://t.co/QW6J5tVRhO
#Sentiment(polarity=0.0, subjectivity=0.0)
#TeslaModel3  Most Profitable Electric Car According to Consultants https://t.co/loDZdWE4aP
#Sentiment(polarity=0.5, subjectivity=0.5)
#RT @thestandardth: อีลอน มัสก์ ได้ออกมากล่าวขอโทษ เวิร์น อันสเวิร์ธ นักดำน้ำชาวสหราชอาณาจักร และหนึ่งในทีมกู้ภัยที่ช่วยเหลือสมาชิกนักฟุตบอล…
#Sentiment(polarity=0.0, subjectivity=0.0)
#I guess someone explained to him what "defamation per se" is. 
