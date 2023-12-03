package main

import (
    "fmt"
    "os"
	"regexp"
    "strings"
	"strconv"
)


func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func abs(x int) int {
	if x > 0 {
		return x
	}
	return -x 
}

func main() {
	dat, err := os.ReadFile("../input.txt")
	if err != nil {
        fmt.Println(err)
    }

	sum := 0
	lines := strings.Split(string(dat), "\n")
	dx := len(lines)

	for i := 0; i < len(lines); i++{
		line := lines[i]
		reGear := regexp.MustCompile(`\*`)
		gearIdxs := reGear.FindAllStringIndex(line, -1)
		for j := 0; j < len(gearIdxs); j++ {
			idx := gearIdxs[j][0]
			neighNumber := 0
			multiplication := 1
			
			for p := -1; p <= 1; p++ {
				if i + p >= 0 && i + p < dx {
					reNumbers := regexp.MustCompile(`\d+`)
					numberIdxs := reNumbers.FindAllStringIndex(lines[i+p], -1)

					for k := 0; k < len(numberIdxs); k++ {
						startIdx := numberIdxs[k][0]
						endIdx := numberIdxs[k][1]

						if min(abs(startIdx - idx), abs(endIdx - 1 - idx)) <= 1 {
							val, _ := strconv.Atoi(lines[i+p][startIdx : endIdx])
							multiplication *= val
							neighNumber += 1
						}
					}
				}
			}

			if neighNumber == 2 {
				sum += multiplication
			}
		}
	}

	fmt.Println(sum)
}