# cons(a, b) constructs a pair, 
# and car(pair) and cdr(pair) returns the first and last element of that pair. 

# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


# Implement car and cdr

# 'pair' is a function

def util(x,y):
  return (x,y)

def car(pair):
	return pair(util)[0]

def cdr(pair):
	return pair(util)[1]


import unittest

class Test_construct_pair(unittest.TestCase):

	def test_case_one(self):
		self.assertEqual(car(cons(3, 4)), 3)

	def test_case_two(self):
		self.assertEqual(cdr(cons(3, 4)), 4)


unittest.main()


# SOLUTION
# Could have done it with a lambda instead of a named function:
# Still, weirdly simple question.

# def car(pair):
#     return pair(lambda a, b: a)

# def cdr(pair):
#     return pair(lambda a, b: b)
