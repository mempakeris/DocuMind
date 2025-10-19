package main

import "fmt"
import "time"

func main() {
	fmt.Print("Go worker started...")

	for {
		fmt.Println("Processing job...")
		time.Sleep(5 * time.Second)
	}
}