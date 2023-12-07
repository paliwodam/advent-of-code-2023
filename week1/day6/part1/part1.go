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

func searchMinWinning(start, end, time, distance int) int {
	if end > start {
		mid := (end + start) / 2

		if mid * (time - mid) == distance{
			return mid + 1
		} else if mid * (time - mid) > distance {
			return searchMinWinning(start, mid - 1, time, distance)
 		} else if mid * (time - mid) < distance {
			return searchMinWinning(mid + 1, end, time, distance)
		}
	}
	if end * (time - end) > distance {
		return end
	}
	return end + 1
}



func main() {
    readFile, err := os.Open("../input.txt")
  
    if err != nil {
        fmt.Println(err)
    }
    fileScanner := bufio.NewScanner(readFile)
    fileScanner.Split(bufio.ScanLines)
	
	fileScanner.Scan()
	line := fileScanner.Text()
	time := strArrToIntArr(strings.Fields(line)[1:]) 

	fileScanner.Scan()
	line = fileScanner.Text()
	distance := strArrToIntArr(strings.Fields(line)[1:]) 

	multi := 1
	for i := 0; i < len(time); i++ {
		t := time[i]
		d := distance[i]
		m := searchMinWinning(0, (t - 1) / 2, t, d)
		multi *= t-2*m+1
	}

	fmt.Println(multi)
    readFile.Close()
}