package main

import (
    "bufio"
    "fmt"
    "os"
    "strings"
	"strconv"
)

func strArrToIntArr(s []string) []int {
	n := len(s)
	nums := make([]int, n)
	for i := 0; i < n; i++ {
		val, _ := strconv.Atoi(s[i])
		nums[i] = val
	}
	return nums
}

func main() {
    readFile, err := os.Open("../input.txt")
  
    if err != nil {
        fmt.Println(err)
    }
    fileScanner := bufio.NewScanner(readFile)
    fileScanner.Split(bufio.ScanLines)
	
	copies := make([]int, 500)

	var sum, i int
    for fileScanner.Scan() {
		copies[i] += 1
		line := fileScanner.Text();
		trimmed := strings.Split(line, ":")[1]
		splited := strings.Split(trimmed, "|")

		winningNums := strArrToIntArr(strings.Fields(splited[0]))
		nums := strArrToIntArr(strings.Fields(splited[1]))

		matched := 0

		for k := 0; k < len(winningNums); k++ {
			for j := 0; j < len(nums); j++ {
				if winningNums[k] == nums[j] {
					matched += 1
					copies[i+matched] += 1 * copies[i]
				}
			}
		}

		i += 1
    }
	
	for j := 0; j < i; j++{
		sum += copies[j]
	}

	fmt.Println(sum)
    readFile.Close()
}