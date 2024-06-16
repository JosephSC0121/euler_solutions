package main

import (
	"fmt"
	"golang/exercises"
)

func main() {
	limit := 4000000
	res := exercises.FibonacciSum(limit)
	fmt.Print(res)
}
