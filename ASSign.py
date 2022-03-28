#WAP to test whether an input is integer or not.
#WAP to display unique words from the string.
# python program to print all
# the unique words in a string
# in python using set() method
# function to print unique words


#3.WAP to accept a string and replace all spaces by '#' symbol

# Python program for the above approach

def printf(str):

	
	lis = list(str.split(" "))

	
	string = '#'.join(lis)
	
	return string



str = input("enter a string-:")
print(printf(str))

# This code is contributed by vikkycirus



