####################################################################################################
#	find_all_occurences.py
#	admin@doctorcode.net
#	30 April 2017
#	Find all occurences of a word in a large string
#	Usage:
# 		- python find_all_occurences.py
####################################################################################################
long_story = """This is a really tricky one (and trickier than I actually intended it to be). Please don't get frustrated or worried if you don't get this one correct! You can do some experiments to test some of the choices (which I do encourage), but remember the question is asking about whether it is always equivalent for any possible choice of the values of s, t, and i.

Use your Python interpreter on your personal computer, or use any in-browser Python 2.6 or 2.7 interpreter to test this out! Here are a couple interpreters we like: repl.it and Skulpt.org with Python 2.6.

To check your answers, you can use one of these interpreters. Put print in front of each example so you can see the results when you press run. Don't forget to test lots of different examples including the empty string, and different integer values of i. This is a really tricky one (and trickier than I actually intended it to be). Please don't get frustrated or worried if you don't get this one correct! You can do some experiments to test some of the choices (which I do encourage), but remember the question is asking about whether it is always equivalent for any possible choice of the values of s, t, and i. (As you'll see in the answer, I got this one wrong myself twice!)"""
# print long_story

# Find all occurences of a word
word_to_find = 'his' # find this word
word_to_find = raw_input('Word to find:') # or use user input


def find_all_occurences(long_story,string):
	index = 0
	while index <= len(long_story):
		index = long_story.find(string, index)
		if index == -1:
			break
		print "Word '%s' at position:" % string + str(index) + " --> '..." + long_story[index:(index + len(string) + 10)] + "...'" #just to show that its really at that location
		# print long_story[index:]
		index += 1
	
find_all_occurences(long_story, word_to_find)