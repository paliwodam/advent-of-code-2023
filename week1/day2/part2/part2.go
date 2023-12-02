package main

import (
    "bufio"
    "fmt"
    "os"
    "strings"
	"strconv"
)

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
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
		var maxBlue, maxRed, maxGreen int
		line := fileScanner.Text();
		game := strings.Replace(strings.Split(line, ":")[1], ";", ",", -1)
		cubes := strings.Split(game, ",")

		for i := 0; i < len(cubes); i++ {
			cube := strings.TrimSpace(cubes[i])
			number, _ := strconv.Atoi(strings.Fields(cube)[0])
			color := strings.Fields(cube)[1]

			switch color {
			case "blue" :
				maxBlue = max(maxBlue, number)
			case "red" : 
				maxRed = max(maxRed, number)
			case "green":	
				maxGreen = max(maxGreen, number)
			}
		}
		
		sum += maxRed * maxBlue * maxGreen
    }
  
	fmt.Println(sum)
    readFile.Close()
}