import itertools
import gmpy2

def pandigital_fibonacci():
	MOD = 10**9
	a = 0
	b = 1
	for i in itertools.count():
		if "".join(sorted(str(a))) == "123456789":  
			f = fibonacci(i)[0]
			if "".join(sorted(gmpy2.digits(f)[ : 9])) == "123456789":  
                return str(i)
		a, b = b, (a + b) % MOD
	return str(ans)

# Returns the tuple (F(n), F(n+1)), computed by the fast doubling method.
def fibonacci(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = fibonacci(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)


if __name__ == "__main__":
	print(pandigital_fibonacci())
