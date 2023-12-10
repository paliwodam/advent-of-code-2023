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

func recur(nums []int) int {
	n := len(nums)
	allZeros := true
	newNums := make([]int, n-1)
	for i := 1; i < n; i++ {
		newNums[i-1] = nums[i] - nums[i-1]
		if newNums[i-1] != 0 {
			allZeros = false
		}
	}
	
	if allZeros == true {
		return nums[0]
	}
	return nums[0] - recur(newNums) 
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
		nums := strArrToIntArr(strings.Fields(line))
		sum += recur(nums)
    }
  
	fmt.Println(sum)
    readFile.Close()
}