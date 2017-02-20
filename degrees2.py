# -*- coding: utf-8 -*-
####################################################################################################
#	degrees2.py
#	admin@doctorcode.net
#	24 January 2017
#	Converts degrees to radians - improved degrees.py
# 	https://en.wikipedia.org/wiki/Minute_and_second_of_arc
#	Usage:
# 		- python degrees2.py
# 		or
# 		- python --> import degrees2.py; quit: 'q'
####################################################################################################
import math
space = 20
arcminute = 1.0 / 60
arcsecond = 1.0 / 60 / 600


# PRINT A TABLE WITH CONSTANT VALUES
def printTable(x, y, z):
	print str(x).rjust(space),
	print str(y).rjust(space),
	print str(z).rjust(space)

for x in range(1, 6): # xrange() is faster CPU-vise
	if x >= 3:
		print "-" * (((space + 4) * 3) - 2)

	if x == 1:
		print "*" * (((space + 4) * 3) - 2)
		printTable("UNIT", "VALUE", "IN RADIANS")
		print "*" * (((space + 4) * 3) - 2)
	elif x == 2:
		printTable("degree", "1/360 turn", math.pi/180)
	elif x == 3:
		printTable("arcminute", "1/60 degree", math.pi/180/60)
	elif x == 4:
		printTable("arcseconds", "1/60 arcminute", math.pi/180/60/60)


# USER INPUTS
all_radians = []
while True: # error checking
	degrees = raw_input("Degrees to radians: ")
	if degrees == 'q':
		break
	elif degrees == 'arcminute':
		degrees = arcminute
	elif degrees == 'arcsecond':
		degrees = arcsecond
	
	try:
		degrees = float(degrees)
		radians = degrees * math.pi/180
		all_radians.append(radians)
		print "%.4f° --> %.8f rad" % (degrees, radians)
	except ValueError:
		print "Not good"


### TODO - store all_radians to a separate file - degrees.txt
file = "degrees.txt"
target_file = open(file, 'w') # open the file, with writing/editing enabled
print "I'm going to write all searches to a text file - %s" % (file)
for i in xrange(len(all_radians)):
	if i != 0: # if sentences in general slow down the program, so avoid it whenever possible
		target_file.write("\n") # prints a new line first, except for the first line
	target_file.write(str(all_radians[i])) # writes to the opened txt file
target_file.close()

# TODO - improve what's being written in .txt file, e.g.: '50° --> 0.87266463 rad'