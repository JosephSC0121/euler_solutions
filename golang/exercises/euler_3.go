package exercises

import "fmt"

func Triplet(limit int) int {
	a, b, c, result := 0, 0, 0, 0
	for a <= limit {
		for b <= limit-a {
			c = limit - a - b
			if a^2+b^2 == c^2 {
				fmt.Println(result)
				result = a * b * c
			}
		}
	}
	return result
}
