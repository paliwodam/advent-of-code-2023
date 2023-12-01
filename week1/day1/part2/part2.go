package main

import (
    "bufio"
    "fmt"
    "os"
    "strings"
)

const MaxUint = ^uint(0) 
const MaxInt = int(MaxUint >> 1) 
const MinInt = -MaxInt - 1

func main() {
    readFile, err := os.Open("../input.txt")
  
    if err != nil {
        fmt.Println(err)
    }
    fileScanner := bufio.NewScanner(readFile)
 
    fileScanner.Split(bufio.ScanLines)
  
	sum := 0
    for fileScanner.Scan() {
		firstIdx, first := MaxInt, -1
		lastIdx, last := MinInt, -1
		line := fileScanner.Text();

		digits := [9]string{"1", "2", "3", "4", "5", "6", "7", "8", "9"}
		digitsSpelled := [9]string{"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}

		for i := 0; i < 9; i++{
			firstIdxDigits := strings.Index(line, digits[i])
			lastIdxDigits := strings.LastIndex(line, digits[i])
			fisrtIdxDigitsSpelled := strings.Index(line, digitsSpelled[i])
			lastIdxDigitsSpelled := strings.LastIndex(line, digitsSpelled[i])

			if firstIdxDigits != -1 && firstIdxDigits < firstIdx{
				firstIdx = firstIdxDigits
				first = i+1
				}
			
			if lastIdxDigits != -1 && lastIdxDigits > lastIdx{	
				lastIdx = lastIdxDigits
				last = i+1
			}
			if fisrtIdxDigitsSpelled != -1 && fisrtIdxDigitsSpelled < firstIdx {
				firstIdx = fisrtIdxDigitsSpelled
				first = i+1
			}

			if fisrtIdxDigitsSpelled != -1 &&  lastIdxDigitsSpelled > lastIdx {
				lastIdx = lastIdxDigitsSpelled
				last = i+1
			}
		}
		// fmt.Println(first, last)
		sum += first * 10 + last
    }
  
	fmt.Println(sum)
    readFile.Close()
}