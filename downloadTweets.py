import GetOldTweets3 as got
import csv
import requests

class DownloadTweets:

    def __init__(   self,
                    query,
                    begin = '',
                    end = '',
                    location = '',
                    radius = '',
                    language = '',
                    nbr = 100):

        self.criteria = got.manager.TweetCriteria()
        self.criteria.setQuerySearch( query )
        self.criteria.setMaxTweets( nbr )
        if begin != '':
            self.criteria.setSince( begin )

        if end != '':
            self.criteria.setUntil( end )

        if location != '':
            self.criteria.setNear( location )

        if radius != '':
            self.criteria.setNear( radius )

        if language != '':
            self.criteria.setLang( language )

    def getTweets(self):
        '''dowload the tweets'''
        self.tweets = got.manager.TweetManager.getTweets( self.criteria )
        self.urls = []
        for tweet in self.tweets:
            self.urls.append(tweet.urls.split(','))

    def asList (self, tweet) :
        '''return a list with the contents of a tweet'''
        return( [tweet.text, tweet.urls,
        tweet.permalink, tweet.username, tweet.date ])

    def exportList(self):
        '''returns a list which contains lists containing the properties of
        the tweets'''
        ret = []
        for tweet in self.tweets:
            ret.append(self.asList(tweet))
        return(ret)

    def getURL(self):
        '''returns a list with all the permalinks to the tweets'''
        ret = []
        for tweet in self.tweets:
            ret.append(tweet.permalink)
        return( ret )
