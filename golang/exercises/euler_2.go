package exercises

func FibonacciSum(limit int) int {
	a, b := 2, 8
	sum := 2
	for b <= limit {
		sum += b
		a, b = b, 4*b+a
	}
	return sum
}
