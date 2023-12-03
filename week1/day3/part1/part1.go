package main

import (
    "fmt"
    "os"
	"regexp"
    "strings"
	"strconv"
)

func isSpecialChar(ch uint8) bool {
	char := rune(ch)
	return (char < '0' || char > '9') && char != '.'
}


func main() {
	dat, err := os.ReadFile("../input.txt")
	if err != nil {
        fmt.Println(err)
    }

	coords := [8][2]int {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}}
	
	sum := 0
	lines := strings.Split(string(dat), "\n")
	dx := len(lines)

	for i := 0; i < len(lines); i++{
		line := lines[i]
		re := regexp.MustCompile(`\d+`)
		matchIdx := re.FindAllStringIndex(line, -1)
		for j := 0; j < len(matchIdx); j++ {
			idxs := matchIdx[j]
			match := line[idxs[0]: idxs[1]]
			withSymbol := false
			for k := idxs[0]; k < idxs[1]; k++ {
				for l := 0; l < len(coords); l++ {
					x := i + coords[l][0]
					y := k + coords[l][1]

					if x >= 0 && x < dx && y >= 0 && y < len(lines[x]) {
						if isSpecialChar(lines[x][y]) {
							withSymbol = true
						}
					}
				}
			}

			if withSymbol {
				val, _ := strconv.Atoi(match)
				sum += val
			}
		}
	}

	fmt.Println(sum)
}