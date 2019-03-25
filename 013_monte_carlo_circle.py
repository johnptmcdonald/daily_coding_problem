import random

# Estimate Pi using a monte carlo method.


# area of a circle is PI*r**2
# equation for a circle is x**2 + y**2 = r**2

# assume r == 1

def generate_num_in_square():
	return (random.uniform(0, 1), random.uniform(0, 1))

def is_in_circle(num):
	x = num[0]
	y = num[1]

	if x**2 + y**2 < 1:
		return True

	return False




def run():
	count = 0
	iterations = 100000000
	for _ in range(iterations):
		num = generate_num_in_square()
		if is_in_circle(num):
			count += 1

	return (count/iterations)*4


print(run())


