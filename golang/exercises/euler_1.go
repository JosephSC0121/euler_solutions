package exercises

func CalculateMultiples(limit int) int {
	var sum int
	for i := 1; i < limit; i++ {
		if i%3 == 0 || i%5 == 0 {
			sum = sum + i
		}
	}
	return sum
}
