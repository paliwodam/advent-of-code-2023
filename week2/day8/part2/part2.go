package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func lcm(a, b int) int {
	return a * b / gcd(a, b)
}

func multipleLCM(numbers []int) int {
	result := lcm(numbers[0], numbers[1])

	for i := 2; i < len(numbers); i++ {
		result = lcm(result, numbers[i])
	}

	return result
}

func main() {
	readFile, err := os.Open("../input.txt")

	if err != nil {
		fmt.Println(err)
	}
	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	fileScanner.Scan()
	instruction := fileScanner.Text();
	fileScanner.Scan()

	paths := make(map[string][]string)
	startingPoints := make([]string, 0, 1000)

	for fileScanner.Scan() {
		line := fileScanner.Text()
		mainSplit := strings.Split(line, "=")
		from := strings.Trim(mainSplit[0], " ")
		if from[2] == 'A' {
			startingPoints = append(startingPoints, from)
		}
		to := strings.Split(mainSplit[1], ", ")
		to1 := strings.TrimPrefix(to[0], " (")
		to2 := strings.Trim(to[1], ")")
		paths[from] = []string{to1, to2}
	}

	toZ := make([]int, len(startingPoints))
	for k := 0; k < len(startingPoints); k++ {
		var i int
		for curr := startingPoints[k]; curr[2] != 'Z'; i++ {
			idx := i % len(instruction)
			if instruction[idx] == 'L' {
				curr = paths[curr][0]
			} else {
				curr = paths[curr][1]
			}
		}
		toZ[k] = i
	}
	
	fmt.Println(multipleLCM(toZ))

	readFile.Close()
}
