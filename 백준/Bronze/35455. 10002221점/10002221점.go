package main

import "fmt"

func main() {
	var t int

	fmt.Scan(&t)

	for i := 0; i < t; i++ {
		var n int
		var s int
		fmt.Scan(&n, &s)
		
		var best int;
		best = 10000000 + n;
		if best > s {
			fmt.Println("No")
		} else {
			fmt.Println("Yes")
		}
	}
}
