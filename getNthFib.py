#Nth FIbonacci
# The fibonacci sequence is defined as follows: 
#the first number of the sequence is 0
# the second number is one
# the nth number is the sum of the (n - 1)th and (n - 2)th numbers
# write a function that takes an integer n and returns the fibonacci number

# sample input: 6
#Sample output: 5(0, 1, 1, 2, 3, 5)

def getNthFib(n, calculated = {1:0, 2:1, 3:1}):
	if n in calculated:
		return calculated[n]

	calculated[n] = getNthFib(n-1, calculated) + getNthFib(n - 2, calculated)
	return calculated[n]