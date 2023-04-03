
import tweepy #https://github.com/tweepy/tweepy
import csv
import sys

#Twitter API credentials
consumer_key = "opFtrWWNep28DdEPFJXvMvBWu"
consumer_secret = "AtkMEsfoFouwwQGxaqtnxKoO96ps6mGDcD4IRsZ63PpOwiVxwL"
access_key = "954055231322468353-ODIzhQninrbPm1r34t1fH9qzk6dFdFa"
access_secret = "jFis4Q8SfwjnhnruI3Cx3Ri3D4374eLHEzsw7G7FQkcN6"


def get_all_tweets(screen_name):
        #Twitter only allows access to a users most recent 3240 tweets with this method

        #authorize twitter, initialize tweepy
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)

        #initialize a list to hold all the tweepy Tweets
        alltweets = []

        #make initial request for most recent tweets (200 is the maximum allowed count)
        #new_tweets = api.user_timeline(screen_name = screen_name,count=1)
        new_tweets = api.user_timeline(screen_name = screen_name,count=200, tweet_mode='extended')

        #save most recent tweets
        alltweets.extend(new_tweets)

        #save the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        #keep grabbing tweets until there are no tweets left to grab
        while len(new_tweets) > 0:
                print "getting tweets before %s" % (oldest)

                #all subsequent requests use the max_id param to prevent duplicates
                new_tweets = api.user_timeline(screen_name = screen_name,count=200, tweet_mode='extended',max_id=oldest)

                #save most recent tweets
                alltweets.extend(new_tweets)

                #update the id of the oldest tweet less one
                oldest = alltweets[-1].id - 1

                print "...%s tweets downloaded so far" % (len(alltweets))

        #go through all found tweets and remove the ones with no images 
        outtweets = [] #initialize master list to hold our ready tweets
        for tweet in alltweets:
                #not all tweets will have media url, so lets skip them
                try:
                        print tweet.entities['media'][0]['media_url']
                except (NameError, KeyError):
                        #we dont want to have any entries without the media_url so lets do nothing
                        pass
                else:
                        outtweets.append(["https://twitter.com/Andy_Buck/status/"+tweet.id_str, tweet.created_at, tweet.full_text.encode("utf-8"), tweet.entities['media'][0]['media_url']])


        #write the csv  
        with open('D:\\image+text tweet\\%s_tweets.csv' % screen_name, 'wb') as f:
                writer = csv.writer(f)
                writer.writerow(["id","created_at","text","media_url"])
                writer.writerows(outtweets)

        pass


if __name__ == '__main__':
        #pass in the username of the account you want to download
        get_all_tweets("Andy_Buck")
