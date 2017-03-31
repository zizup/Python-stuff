###############################################################################
#	trikotniki-clean3.py
#	Added separate functions to do stuff
#	19 February 2017
# 	New TODO stuff
#	Usage: time python trikotniki-clean3.py trikotniki.txt
###############################################################################
from math import *
from sys import argv
from datetime import datetime

def main():
	script, filename = argv # script=trikotniki-clean3.py, filename=trikotniki.txt

	max_search = take_user_input()
	successful_results = calculate(max_search) # calculate() returns an array
	# and stores it in successful_results[]
	check_results(successful_results) # checks the array calculate() returned
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
	successful_results_for_calculate_function = [] # calculate function returns this array
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
				successful_results_for_calculate_function.append(tmp_array)
			else:
				fail += 1

	print "combinations tried out:", combinations
	print "successes:", success # TODO: replace these with 'print "successes: {0}" . format(success)'
	# because the script runs faster
	print "fails:", fail
	# print "successful_results_for_calculate_function:", successful_results_for_calculate_function
	print "-" * 20
	return successful_results_for_calculate_function
	return success # TODO: can a function return > 1 outcome? I need this for check_result() TODO


def check_results(array_to_be_checked): #checks the array calculate() returned
	print "CHECKING ..." # CHECKING for the same triangles (a=3,b=4 is the
	# same triangle as a=4,b=3)
	for results in array_to_be_checked:
		for check_again in array_to_be_checked:
			# delete doubles
			if results[0] == check_again[0]: 
				if results[1] == check_again[2] and results[2] == check_again[1]:
					array_to_be_checked.remove(check_again)
	print "CHECKED!"

	"""TODO: print again how many combinations there are left, and compare them to
	the variable 'success' (a=3,b=4,c=5 and a=4,b=3,c=5 are considered as)
	two different triangles at 'success' variable"""
	print "Length:", len(array_to_be_checked)


	print "-" * 20


def print_sorted_results(array_to_be_printed, file_to_be_opened):
	# Print sorted results to a file "trikotniki.txt"
	"""The lambda returns the first element of each of the inner lists and the
	sorted function uses that to sort those list. The first element in our case is
	c; see 'tmp_array'."""
	array_to_be_printed = sorted(array_to_be_printed, key = lambda x: x[0])
	target_file = open(file_to_be_opened, 'w') # open file with write privileges
	# write a date
	target_file.write(str(datetime.utcnow()))
	
	target_file.write("\nPythagorean theorem: c = sqrt(a**2 + b**2)\nLegend: c, a, b\n\n")
	
	print "END RESULT --> see %s" % file_to_be_opened
	for each_result in array_to_be_printed:
		target_file.write(str(each_result) + "\n")
	target_file.close()

if __name__ == "__main__":
	main()