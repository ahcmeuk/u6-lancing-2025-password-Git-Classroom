package main

import (
	"fmt"
)

func Valid(password string) {
	not_vld := true
	var pas string
	for not_vld {
		fmt.Println("Enter your password")
		fmt.Print("-> ")
		fmt.Scan(&pas)
		if pas == password {
			fmt.Println("nice")
			not_vld = false
		}
	}
	fmt.Println("Cusseccfully logged in!")
}

func main() {
	var password string
	fmt.Println("your username is - user")
	fmt.Println("create your password")
	fmt.Print("-> ")
	fmt.Scan(&password)
	Valid(password)
	fmt.Println()
	fmt.Println("also - easier than easy")
}
