#Project Euler Problem 34
from math import factorial

f = [factorial(0),
factorial(1),
factorial(2),
factorial(3),
factorial(4),
factorial(5),
factorial(6),
factorial(7),
factorial(8),
factorial(9)]

#sum of factorial of the digits
def factorial_digits(n):
	s = 0
	while n:
		s += f[n%10]
		n //= 10
	return s

#variable to save the value of solution
solution = 0

#for loop to loop till 1854721
for i in range(10,1854721):
	if factorial_digits(i) == i:
		solution += i

#printing the solution
print(solution)
