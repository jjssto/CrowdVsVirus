#!/usr/bin/env python3

from downloadTweets import DownloadTweets
from pictures import Pictures
from writeToCSV import WriteToCSV

QUERY = '#Masks4All' # search query for twitter
LANG = '' # limit search to language (e.g. en, de or fr)
BEGIN = '' # earliest date
END = '' # latest date
LOCATION = '' # location (doesn't seem to work)
RADIUS = '' # radius around location
NBR = 1000 # how many tweets should be downloaded
GROUP = 5 # after how many requests should the tor identity be changed?
PW = '' # password for tor
CSV_FILE = '' # csv file, in which the results are saved


# download the tweets matching the search
tweets = DownloadTweets(
    query = QUERY,
    language = LANG,
    begin = BEGIN,
    end = END,
    location = LOCATION,
    radius = RADIUS,
    nbr = NBR )
tweets.getTweets()

# get the URLs of the pictures
pics = Pictures( tweets )
urls = pics.getPictureUrls(
    group = GROUP,
    pw = PW
)
tweet_list = tweets.exportList()

# get biggest number of pictures, that a single tweet has
max = 0
for element in urls:
    if len(element) > max:
        max = len(element)

colnames = [ 'text', 'links', 'permalink', 'username', 'date' ]

# preparing the data to write the csv
n = len(colnames) + max
counter = 0
while len(colnames) < n :
    colnames.append( 'photo' + str(counter))
    counter = counter + 1

ret = []
j = 0
for i in range(len(tweet_list)):
    if urls[i] == '':
        continue
    else:
        ret.append(tweet_list[i])
        try:
            ret[j].extend(urls[i])
        except TypeError:
            ret[j].append(urls[i])

        while len(ret[j]) < n:
            ret[j].append('')
        j = j + 1

# ret = []
# for i in range(len(tweet_list)):
#     ret.append(tweet_list[i])
#     try:
#         ret[i].extend(urls[i])
#     except TypeError:
#             ret[i].append(urls[i])
#
#     while len(ret[i]) < n:
#         ret[i].append('')


# write the csv
csv = WriteToCSV(CSV_FILE)
csv.write(ret,colnames)
