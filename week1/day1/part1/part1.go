package main

import (
    "bufio"
    "fmt"
    "os"
    "unicode"
)


func main() {
    readFile, err := os.Open("input.txt")
  
    if err != nil {
        fmt.Println(err)
    }
    fileScanner := bufio.NewScanner(readFile)
 
    fileScanner.Split(bufio.ScanLines)
  
	var sum = 0
    for fileScanner.Scan() {
		var first = -1
		var last = -1
		var line = fileScanner.Text();
		for _, letter := range line {
			if unicode.IsDigit(letter) {
				last = int(letter) - 48
				if first == -1 {
					first = int(letter) - 48
				}
			}
		}
		sum += first * 10 + last
    }
  
	fmt.Println(sum)
    readFile.Close()
}