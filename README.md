Random Chord Bot
=================

A Twitter bot that creates random guitar chord.

If my math serves, at 6 strings and 5 frets = 40,920 possible chords.  
At a Tweet every hour, that means it will take ~4.67 years to complete.

**LOAD OAUTH SETTINGS**  
Assumes Twitter OAuth settings, saved in a file
called OAuthSettings.py, saved in the following format:
	
    settings = {
      'consumer_key': 'xxxx',
      'consumer_secret': 'xxxx',
      'access_token_key': 'xxxx',
      'access_token_secret': 'xxxx'
    }

**UNICODE CHARACTERS VIA**
* http://www.busydoingnothing.co.uk/emoji.html
* http://en.wikipedia.org/wiki/List_of_Unicode_characters

**REQUIRES**
* OAuthlib  
https://github.com/requests/requests-oauthlib
* Python Twitter  
https://github.com/bear/python-twitter
