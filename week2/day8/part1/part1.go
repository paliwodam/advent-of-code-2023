package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

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
	for fileScanner.Scan() {
		line := fileScanner.Text()
		mainSplit := strings.Split(line, "=")
		from := strings.Trim(mainSplit[0], " ")
		to := strings.Split(mainSplit[1], ", ")
		to1 := strings.TrimPrefix(to[0], " (")
		to2 := strings.Trim(to[1], ")")
		paths[from] = []string{to1, to2}
	}

	var i int
	for curr := "AAA"; curr != "ZZZ"; i++ {
		idx := i % len(instruction)
		if instruction[idx] == 'L' {
			curr = paths[curr][0]
		} else {
			curr = paths[curr][1]
		}
	}

	fmt.Println(i)

	readFile.Close()
}
