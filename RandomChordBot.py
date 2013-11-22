
'''
GUITAR CHORD BOT
Jeff Thompson | 2013 | www.jeffreythompson.org

A Twitter bot that creates random guitar chord.

If my math serves, at 6 strings and 5 frets = 40,920 possible chords.
At a Tweet every hour, that means it will take ~4.67 years to complete.

LOAD OAUTH SETTINGS
Assumes Twitter OAuth settings, saved in a file
called OAuthSettings.py, saved in the following format:
	
	settings = {
		'consumer_key': 'xxxx',
		'consumer_secret': 'xxxx',
		'access_token_key': 'xxxx',
		'access_token_secret': 'xxxx'
	}

REQUIRES
+ OAuthlib
	- https://github.com/requests/requests-oauthlib
+ Python Twitter
	- https://github.com/bear/python-twitter

UNICODE CHARACTERS VIA
+ http://www.busydoingnothing.co.uk/emoji.html
+ http://en.wikipedia.org/wiki/List_of_Unicode_characters

'''

from OAuthSettings import settings				# import from settings.py
import random															# for random chord position
import twitter														# for posting to Twitter
import os																	# for getting current directory
from sys import exit											# for exiting when done posting

# VARIABLES
off = u'\u25fb'.encode('utf-8')		# unicode char for non-pressed fret
on = u'\u25fc'.encode('utf-8')		# unicode char for finger
rows = 6													# number of rows (strings)
columns = 5												# number of columns (frets)
num_fingers = 4										# how many fingers to press


# TUNING (from top string to bottom)
tuning = [ 'e  ', 'B  ', 'G  ', 'D  ', 'A  ', 'E  ' ]


# LOAD OAUTH DETAILS FROM FILE TO ACCESS TWITTER
# see notes at top for format
consumer_key = settings['consumer_key']
consumer_secret = settings['consumer_secret']
access_token_key = settings['access_token_key']
access_token_secret = settings['access_token_secret']


# CREATE EMPTY TAB
chord = []
for y in range(rows):
	chord.append([])
	for x in range(columns):
		chord[y].append(off)


# CREATE RANDOM CHORD
for i in range(num_fingers):
	x = random.randrange(columns)
	y = random.randrange(rows)
	chord[y][x] = on


# REMOVE ANY DUPLICATES ALONG SAME STRING
for y in range(rows):
	found_finger = False
	for x in range(columns-1,-1, -1):
		if chord[y][x] == on and not found_finger:
			found_finger = True
		elif found_finger:
			chord[y][x] = off


# FORMAT RESULTING CHORD AS A STRING
chord_string = ''
for y in range(rows):
	chord_string += tuning[y]
	for x in range(columns):
		chord_string += chord[y][x]
	chord_string += '\n'
chord_string = chord_string.strip()


# CONNECT TO TWITTER API, POST and PRINT RESULT
# catch any errors and let us know
try:
	api = twitter.Api(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token_key = access_token_key, access_token_secret = access_token_secret)	
	print '\n\n' + chord_string + '\n\n'
	print 'posting to Twitter...'
	status = api.PostUpdate(chord_string)
	print '  post successful!\n\n'
except twitter.TwitterError:
	print api.message


# SAVE TWEETS TO FILE
# get current directory, prepend to word list paths
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'Tweets.txt'), 'a') as file:
	file.write(chord_string + '\n\n')


# ALL DONE!
exit()