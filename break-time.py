####################################################################################################
#	break_time.py
#	admin@doctorcode.net
#	This script helps you get a break every 2 hours
#	05 March 2017
#	Usage: python break_time.py
####################################################################################################
import webbrowser # https://docs.python.org/2/library/webbrowser.html
import time

print "This program started on:", time.asctime()

repetitions = 3
time_of_sleep = 2 * 60 * 60 # in seconds

for i in xrange(0,repetitions):
	# waits for N seconds
	time.sleep(time_of_sleep)
	
	# open the browser
	webbrowser.open('https://www.youtube.com/watch?v=0GoGcVs6pbU', new = 1)

print "This program ended on:", time.asctime()