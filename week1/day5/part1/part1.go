package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
	"slices"
)

const MaxUint = ^uint(0)
const MinUint = 0
const MaxInt = int(MaxUint >> 1)
const MinInt = -MaxInt - 1

func atoi(s string) int {
	val, _ := strconv.Atoi(s)
	return val
}

func removeNonNumeric(input string) string {
	regexPattern := regexp.MustCompile("[^0-9 \n]")
	result := regexPattern.ReplaceAllString(input, "")
	return result
}

func stringArrayToIntArray(s []string) []int {
	n := len(s)
	nums := make([]int, n)
	for i := 0; i < n; i++ {
		nums[i] = atoi(s[i])
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

	fileScanner.Scan()
	line := fileScanner.Text()
	seeds := stringArrayToIntArray(strings.Fields(removeNonNumeric(line)))
	seedsNumber := len(seeds)

	prevCorresponding := seeds
	currCorresponding := make([]int, seedsNumber)
	for i := 0; i < seedsNumber; i++ {
		currCorresponding[i] = -1
	}

	for fileScanner.Scan() {
		line := fileScanner.Text();
		if strings.TrimSpace(line) == "" {
			for i := 0; i < seedsNumber; i++ {
				if currCorresponding[i] == -1 {
					currCorresponding[i] = prevCorresponding[i]
				}
			}
		} else if strings.Contains(line, "map") {
			for i := 0; i < seedsNumber; i++ {
				prevCorresponding[i] = currCorresponding[i]
				currCorresponding[i] = -1
			}
		} else {
			ranges := strings.Fields(line)
			x, y, z := atoi(ranges[0]), atoi(ranges[1]), atoi(ranges[2])
			for i := 0; i < seedsNumber; i++ {
				if prevCorresponding[i] >= y && prevCorresponding[i] < y + z {
					currCorresponding[i] = prevCorresponding[i] - y + x
				}
			}
		}
	}
	for i := 0; i < seedsNumber; i++ {
		if currCorresponding[i] == -1 {
			currCorresponding[i] = prevCorresponding[i]
		}
	}

	fmt.Println(slices.Min(currCorresponding))

}
