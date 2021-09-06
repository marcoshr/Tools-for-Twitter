import tweepy
import time
import requests
import os
from countdown import countdown

consumer_key = '0hVKwyzAEJYTCbfDa63N6XeJl'
consumer_secret = '8vyH6tbuNYY7XBuiqA4iOvmVJJx6TJdJvQYvioeaKjkku2AAmj'

access_token = '185760709-CGuRGOX1BieFeaubth1jOpFsnZuiAQaHUAmuc5SA'
access_token_secret = 'ZBisPi5Wz2KYhXPOGeqF2BwQO4gzIuq40DutJ6y8iilwo'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print (user.name + " | " + str(user.id))

def follow_who_follow():
        for followers in tweepy.Cursor(api.followers).items():
            followers.follow()
            print ("Followed everyone that is following " + user.name)

# Rtea y dale fav a tweets por palabras clave
def rt_fav_keyword():
    numberOfTweets = 3
    search = "Alain De Botton"

    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        try:
            tweet.retweet()
            tweet.favorite()
            print ('Retweeted the tweet')

        except tweepy.TweepError as e:
            print (e.reason)

        except StopIteration:
            break

def reply_to_keyword():
    tweetId = "289429998"
    username = "DaniHeatCrazy"

    phrase = "Maquina"

    for tweet in tweepy.Cursor(api.search,   search).items(numberOfTweets):
        try:
            #tweetId = tweet.user.id
            #username = tweet.user.screen_name
            api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)
            print ("Replied with " + phrase)

        except tweepy.TweepError as e:
            print (e.reason)

        except StopIteration:
            break

def get_home_timeline():
    public_tweets = api.home_timeline()
    print(public_tweets)
    count = 1
    for tweet in public_tweets:
        print("Tweet " + str(count))
        count += 1
        print(tweet.text + "\n")

def tweet_image(url, message):
    print ("principio de tweet_image    ")
    filename = 'temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        print("entra en el if")
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        print("antes del update")
        api.update_with_media(filename, status=message)
        print("despues del update")
        os.remove(filename)
        print("IMAGEN TWITTEADA")
    else:
        print (request.status_code)
        print("Unable to download image")

def get_all_timeline():

    timeline_record = []
    for tweet_timeline in api.user_timeline(user.id):

        if tweet_timeline.text not in timeline_record:
            timeline_record.append(tweet_timeline.text);

    return timeline_record

def main():
    print ("main Function started \n-----\n")
    count = 1
    #time.sleep(3)

    timeline_record = get_all_timeline()

    # Get all direct messages
    direct_messages_record = []
    for direct_message in api.direct_messages():

        if direct_message.text not in timeline_record:
            try:
                print ("Twitteo esto: " + direct_message.text)
                api.update_status(direct_message.text)
                timeline_record.append(direct_message.text);

            except tweepy.TweepError as e:
                print (e.reason)

    print ("\nTimeline Record List:")
    for item in timeline_record:
        print(item + '/n')




        
def unfollow_everyone():
    
    ids = []
    for page in tweepy.Cursor(api.friends_ids, screen_name="Marksssssss").pages():
        ids.extend(page)
        #print(ids)
        countdown(5)
        print ("Siguiendo ahora: " + str(len(ids)))
        i = 1
        for id_i in ids:
            api.destroy_friendship(id_i)
            print(str(i) + " - Eliminado: " + str(id_i))
            i += 1
            countdown()
            

def delete_complete_timeline():
    
    print("Recogiendo todos tus tweets")
    timeline = tweepy.Cursor(api.user_timeline).items()
    
    for tweet in timeline:
        print ("ELiminando tweet %d: Creado [%s]" % (tweet.id, tweet.created_at))
        api.destroy_status(tweet.id)

def check_username_by_id():
    print("20 primeros")
    ids = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,327]
    users = api.lookup_users(user_ids=ids)
    for u in users:
        print(str(u.id) + ": " + u.screen_name)
        


def delete_all_favs():
    print("- Delete_all_favs -")
    
    f = open('like.js')
    
    for line in f:
        if "tweetId" in line:
            try:
                api.create_favorite(line[17:-2])
                api.destroy_favorite(line[17:-2])
                print("Favorito eliminado --> " + line[17:-2])
            except Exception as e:
                print("type error: " + str(e))
                
    f.close()    
    print("The End.")
    
print("--- Main ---")
#delete_all_favs()