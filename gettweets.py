import urllib
import urllib2
import json
 
#start getTwitterData
def getData(keyword):
    url = 'http://search.twitter.com/search.json?q=keyword&lang=en&result_type=recent&since=20120601&until=20120602'
    data = {'q': keyword, 'lang': 'en', 'result_type': 'recent'}
    params = urllib.urlencode(data)
    try:
        req = urllib2.Request(url, params)
        response = urllib2.urlopen(req)
        jsonData = json.load(response)
        tweets = []
        for item in jsonData['results']:
            tweets.append(item['text'])
        return tweets
    #except urllib2.URLError, e:
        #self.handleError(e)
    #return tweets
#end    
	tweets = getData("messi");
	print tweets
