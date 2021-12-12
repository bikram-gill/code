package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

/**To test:
go run Ch01-Ex1.3.go 10000
go run Ch01-Ex1.3.go 100000 -a -b -c -d -e -f -g -h -i -j -k -l -m -n -o -p -q -r -s -t -u -v -w -x -y -z
go run Ch01-Ex1.3.go 100000 -a -b -c -d -e -f -g -h -i -j -k -l -m -n -o -p -q -r -s -t -u -v -w -x -y -z -0123456789 -longstring1 -longstring2 "This is to test performance"

First argument could be increased further to run the loop longer.

TO DO: Benchmark tests
*/
func main() {

	loop, err := strconv.Atoi(os.Args[1])
	if err != nil {
		fmt.Println(err)
		os.Exit(2)
	}

	start1 := time.Now()
	for i := 0; i < loop; i++ {
		echo1(i)
	}
	secs1 := time.Since(start1).Seconds()

	start2 := time.Now()
	for i := 0; i < loop; i++ {
		echo2(i)
	}
	secs2 := time.Since(start2).Seconds()

	start3 := time.Now()
	for i := 0; i < loop; i++ {
		echo3(i)
	}
	secs3 := time.Since(start3).Seconds()

	fmt.Printf("echo1: %.2fs seconds, iterations: %d\n", secs1, loop)
	fmt.Printf("echo2: %.2fs seconds, iterations: %d\n", secs2, loop)
	fmt.Printf("echo3: %.2fs seconds, iterations: %d\n", secs3, loop)
}

func echo1(n int) {
	var s, sep string
	for i := 0; i < len(os.Args); i++ {
		s += sep + os.Args[i]
		sep = " "
	}
	fmt.Printf("%d %s\n", n, s)
}

func echo2(n int) {
	s2, sep2 := "", ""
	for _, arg := range os.Args {
		s2 += sep2 + arg
		sep2 = " "
	}
	fmt.Printf("%d %s\n", n, s2)
}

func echo3(n int) {
	fmt.Printf("%d %s\n", n, strings.Join(os.Args, " "))
}
