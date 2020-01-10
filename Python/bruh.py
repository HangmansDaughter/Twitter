import tweepy
import random
from random import randint
import time
consumer_key = 'POLm2T8bERqHu2DbL3M9lBbnS'
consumer_secret = 'IbxOT13lIyWXEIuyphsJo2XvUH9NjxbkeKL0Z3Wx7auAm4Qj7V'
access_token = '1214857954782011392-PvQEwx9tVVP4Mil7HTJ7XDb8FH8GDg'
access_token_secret = '18de0ef5vzgIWkLHdFqrgF4feRHWXt4hjAo9j6MZ98q7N'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def user_followers():
    username = input("Username >>>>>")
    userFollowerCount = api.get_user(username).followers_count
    print (username)
    print(userFollowerCount)


while True:
    try:
        array=["Cliff", "Rita", "Larry", "Ezekiel", "Admiral Whiskers", "Vic", "Niles", "Flex", "Mr Nobody", "Dr Harrison", "Hammerhead", "Karen", "Flit", "Lucy Fugue", "Val", "Danny", "Gar", "Baby Doll", "Driver 8","Sex Bomb", "Scarlet Harlot", "Silver Tongue", "The Hangman's Daughter", "Liza Radley", "Lex"]
        rand=(randint(0,23))
        muse=array[rand]
        print (rand)
        if muse == array[11]:
            tweet=(muse + " does not support Jane's lesbian rights.")
            print(tweet)
        elif muse ==array[10]:
            tweet=(muse + " does not support /Jane's/ rights but she does support lesbians.")
        else:
            tweet=(muse + " supports Jane's lesbian rights.")
            print(tweet)
        api.update_status(tweet)
        print(tweet)
        
        time.sleep(10)

        f = open('./fUCKTHIS/quotes.txt', 'r')
        content=[]
        content = f.readlines()
        content = [x.strip() for x in content] 
        num=randint(0,17)
        beb=(content[num])
        api.update_status(beb)

        time.sleep(300)

        
    except:
        print("there has been an error")
        time.sleep(2)
    # def tweeting():
    #     array=["Cliff", "Rita", "Larry", "Ezekiel", "Admiral Whiskers", "Vic", "Niles", "Flex", "Mr Nobody", "Dr Harrison", "Hammerhead", "Karen", "Flit", "Lucy Fugue"]
    #     rand=(randint(0,13))
    #     muse=array[rand]
    #     print (rand)
    #     if muse == array[11]:
    #         tweet=(muse + " does not support Jane's lesbian rights.")
    #     else:

    #         tweet= (muse + " supports Jane's lesbian rights.")
    #     api.update_status(tweet)
    #     print(tweet)
    #     time.sleep(300)
    # tweeting()

