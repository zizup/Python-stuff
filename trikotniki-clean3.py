###############################################################################
#	trikotniki-clean3.py
#	Added separate functions to do stuff
#	13 February 2017
# 	New functions:
#	- https://docs.python.org/2/library/datetime.html#datetime.datetime.utcnow
#	- http://stackoverflow.com/questions/19192209/attributeerror-module-object-has-no-attribute-utcnow
#	Usage: time python trikotniki-clean3.py trikotniki.txt
###############################################################################
from math import *
from sys import argv
from datetime import datetime

def main():
	script, filename = argv

	max_search = take_user_input()
	successful_results = calculate(max_search)
	check_results(successful_results)
	print_sorted_results(successful_results, filename)


def take_user_input():
	while True: # error checking
		try:
			max_search = int(raw_input("To which number should I count? "))
			if max_search <= 0:
				print "Give me a bigger number!!!"
			elif max_search > 10000:
				print " This would take forever. Give me a smaller number!"
			else:
				break
		except ValueError:
			print "C'mon, give me an integer."
	print "-" * 20
	print "Try %d A and %d B combinations" % (max_search, max_search)
	print "C = sqrt(A**2 + B**2)"
	return max_search


def calculate(max_search):
	successful_results = []
	combinations, success, fail = 0, 0, 0 
	print "CALCULATING ..."
	for a in range(1,max_search + 1): # TODO replace it with xrange()
	# http://pythoncentral.io/how-to-use-pythons-xrange-and-range/
		for b in range(1,max_search + 1):
			combinations +=1
			# for large amount of combinations:
			if combinations == 100000000:
				print "... at 100.000.000 combinations ..."
			elif combinations == 10000000:
				print "... at 10.000.000 combinations ..."
			elif combinations == 1000000:
				print "... at 1.000.000 combinations ..."


			c = sqrt(a**2 + b**2)
			
			if c % int(c) == 0: # this checks for an integer
				success += 1
				tmp_array = [c, a, b]
				successful_results.append(tmp_array)
			else:
				fail += 1

	print "combinations tried out:", combinations
	print "successes:", success # TODO: replace these  
	# with print "successes: {0}" . format(success), because the script runs faster
	print "fails:", fail
	# print "successful_results:", successful_results
	print "-" * 20
	return successful_results


def check_results(successful_results):
	print "CHECKING ..." # CHECKING
	for results in successful_results:
		for check_again in successful_results:
			# delete doubles
			if results[0] == check_again[0]: 
				if results[1] == check_again[2] and results[2] == check_again[1]:
					successful_results.remove(check_again)
	print "CHECKED!"
	print "-" * 20


def print_sorted_results(successful_results, filename):
	# Print sorted results to a file "trikotniki.txt"
	# The lambda returns the first element of each of the inner lists and the
	# sorted function uses that to sort those list.
	successful_results = sorted(successful_results, key = lambda x: x[0])
	target_file = open(filename, 'w')
	# write a date
	target_file.write(str(datetime.utcnow()))
	
	target_file.write("\nPythagorean theorem: c = sqrt(a**2 + b**2)\nLegend: c, a, b\n\n")
	
	print "END RESULT --> see %s" % filename
	for end_result in successful_results:
		target_file.write(str(end_result) + "\n")
	target_file.close()


if __name__ == "__main__":
	main()