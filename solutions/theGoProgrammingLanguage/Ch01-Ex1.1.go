package main 

import (
    "fmt"
    "os"
    "strings"
)

//To test: "go run Ch01-Ex1.1.go -v -a -b testing", random test strings after file name.
func main() {
	//echo1
	var s, sep string
	for i := 0; i < len(os.Args); i++ {
		s += sep + os.Args[i]
		sep = " "
	}
	fmt.Println(s)
	
	//echo2
	s2, sep2 := "", ""
	for _,arg := range os.Args {
		s2 += sep2 + arg
		sep2 = " "
	}
	fmt.Println(s2)
	
	//echo3
    fmt.Println(strings.Join(os.Args, " "))	
}
