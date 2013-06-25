#hi, this program goes through an rss feed and prints out the top words of the last 20 entries


import feedparser
import os
import string
import re

wordList = {}
yesTerm = []
def crawl(site, outFile):
	i = 0

	btrss = open(outFile, 'w')

	while i < 177:
		i+=1
		page = str(i)
		rssSite = site+page+"/rss"
		print rssSite
#		python_wiki_rss_url = rssUrl
#	 	nothing = ""
		howMany = -1
		largeFeed = feedparser.parse(rssSite)

	#check for the truth, is there such a thing called 'title'?
	#(don't know if this works atm because the current rss grab shows that everything
	#has a title key)
#		if largeFeed.feed.has_key('title') == True:
		entries = largeFeed['entries']


#			print "yeah!"
#		print page #that's the number
		#save it somewhere, this file will have the full entries viewable
		
		for title in entries:
			#howMany used to be a thing for me to figure out
			#how many entries i was getting
			#but now it's used to get the time of each posting
			howMany += 1


			#the connection post's text
			if title.has_key('title') == True:
				connection= title['title']
#				print connection
				time = entries[howMany].published
			#makes like a tuple
				deetz =  connection, time
			#makes it a string, .write() wouldn't take anything else
			#jerk
				full = str(deetz)+"\n\n"
		catlovers		
				btrss.write(full)
	btrss.close()

	#ok let's read that csv?
	#whatever!
	#count it too!
def histo(inFile, outFile):
	csv = open(inFile, 'r')
	line = csv.readlines()
	while (line !=""):
		lineAsString= ', '.join(line)
		words = re.split('\W+', lineAsString)
		for word in words:	
			if word not in wordList:
			#save it in a wordList
				wordList[word] = 1
			else:
				wordList[word] += 1
	
			line = csv.readline()
#						print "hey"
		
	csv.close()
	final = open(outFile, 'w')
	for word in wordList:
		line = str(wordList[word]) + "\t" + word + "\n"
		final.write(line)
	final.close()




def find(inFile, outFile, searchTerm):
	search = open(inFile, 'r')
	line = search.readlines()
	line_count = 0
	for numb in line:
		if searchTerm in numb:
			yesTerm.append(numb)
	search.close()
	#this is a very silly way of going about this,
	#but let's open another .csv to save the final stage.
	#this file will show the histograms if one opens the file with:
	#$ sort final.csv
		
	theSearch = open(outFile, 'w')
	for a in yesTerm:
		aResult = a + "\n"
		theSearch.write(aResult)
	theSearch.close()


	
	
#trying different blogs and feeds
#foo("http://benningtonstudents.tumblr.com/rss")
#foo("http://terrornoiseaudio.blogspot.com/feeds/posts/default?alt=rss")
crawl("http://btonmissedconnections.tumblr.com/page/", 'btrss.csv')
histo('btrss.csv', 'histo.csv')
find('btrss.csv', 'search.csv', 'ass')

