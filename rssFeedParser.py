#Parses and prints titles and content of a RSS feed

import feedparser

d = feedparser.parse('http://www.somewebsiteaddress.com/rss')

#Print feed titles
print d['feed']['title']

#Print feed content
for post in d.entries:
    print post.title + "\n" + post.description + "\n" + "Link: " + post.link + "\n"
	
	
	
