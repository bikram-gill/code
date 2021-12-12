package main 

import (
    "fmt"
    "os"
)

//To test: "go run Ch01-Ex1.2.go test1 -test2 -v -b", random test strings after file name.
func main() {
	//echo1
	for i := 0; i < len(os.Args); i++ {
		fmt.Printf("%d \t%s\n", i, os.Args[i] )
	}
	
	//echo2
	for i2,arg := range os.Args {
		fmt.Printf("%d \t%s\n", i2, arg )
	}
	
	//echo3
    //?	
}
