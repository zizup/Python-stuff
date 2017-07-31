################################################
# Multiple of 3 = 'Fizz', Multiple of  5 = 'Buzz'
# Multiple of 3 and 5 = 'FizzBuzz'
################################################
final_number = 120

for i in xrange(1,final_number+1):
	# First code:
	# if i % 5 == 0 and i % 3 == 0:
	# 	print 'FizzBuzz'
	# elif i % 3 == 0:
	# 	print 'Fizz'
	# elif i % 5 == 0:
	# 	print 'Buzz'
	# else:
	# 	print i

	# Better practice because you can simply add future conditions easily:
	outcome = ""
	if i % 3 == 0: outcome += 'Fizz'
	if i % 5 == 0: outcome += 'Buzz'
	if i % 7 == 0: outcome += 'Happy' # example of future condition
	if i % 3 != 0 and i % 5 != 0 and i % 7 != 0: outcome = i

	print outcome