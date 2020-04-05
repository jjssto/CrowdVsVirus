from bs4 import BeautifulSoup
from writeToCSV import WriteToCSV
import re
from torrequest import TorRequest

class Pictures:

    def __init__(self, tweets):

        self.tweets = tweets
        self.urls = tweets.getURL()


    def getPictureUrls(self, group=5, pw=None):
        """Extract the urls of the pictures in the tweets

        This function is using the torrequest package in order to
        route the requests through Tor.

        Arguments:
        ============

        group:  number of requests, that are routet through the same Tor
                circuit, before it is reset

        pw:     Password used that is required by TorRequest (from torrequest)
                to establich and reset the Tor circuit

        Results:
        ==========

        list with the urls of the pictures in the tweet
        """

        self.pictureURL = []
        with TorRequest(proxy_port = 9050, ctrl_port = 9051, password = pw) as tr:
            counter = 1
            for url in self.urls:
                try:
                    page = tr.get(url)
                except:
                    counter = 1
                    tr.reset_identity()
                    self.pictureURL.append('')
                    continue

                soup = BeautifulSoup(page.content, 'html.parser')
                media_container = soup.findAll(
                    'div',
                    class_='AdaptiveMedia-container'
                )
                if len(media_container) == 0:
                    self.pictureURL.append('')
                    continue
                else :
                    m = re.findall(
                        r'data-image-url=([^ ]*)',
                        str(media_container[0])
                    )
                    if m != []:
                        for i in range(len(m)):
                            m[i].replace('"','')
                        self.pictureURL.append( m )
                    else:
                        self.pictureURL.append( '' )
                if counter < group :
                    counter += 1
                else:
                    counter = 1
                    tr.reset_identity()

        return( self.pictureURL )
