package main

import (
    "bufio"
    "fmt"
    "os"
    "strings"
	"strconv"
	"math"
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

	var sum int
    for fileScanner.Scan() {
		line := fileScanner.Text();
		// idx, _ := strconv.Atoi(strings.TrimPrefix(strings.Split(line, ":")[0], "Card "))
		trimmed := strings.Split(line, ":")[1]
		splited := strings.Split(trimmed, "|")

		winningNums := strArrToIntArr(strings.Fields(splited[0]))
		nums := strArrToIntArr(strings.Fields(splited[1]))

		matched := float64(-1)

		for i := 0; i < len(winningNums); i++ {
			for j := 0; j < len(nums); j++ {
				if winningNums[i] == nums[j] {
					matched += 1
				}
			}
		}

		sum += int(math.Pow(2, matched))
    }
  
	fmt.Println(sum)
    readFile.Close()
}