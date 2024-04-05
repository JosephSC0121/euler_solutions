import math


def compute():
	DIGITS = 100
	MULTIPLIER = 100**DIGITS
	ans = sum(
		sum(int(c) for c in str(math.sqrt(i * MULTIPLIER))[ : DIGITS])
		for i in range(100)
		if math.sqrt(i)**2 != i)
	return str(ans)


if __name__ == "__main__":
	print(compute())
