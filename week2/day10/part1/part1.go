package main

import (
    "bufio"
    "fmt"
    "os"
    "strings"
)

func getMax(arr[][]int) int {
	max := -2
	for i := 0; i < len(arr); i++ {
		for j := 0; j < len(arr[i]); j++{
			if arr[i][j] > max{
				max = arr[i][j]
			}
		}
	}
	return max
}

func recur(x, y, dist int, pipeMap []string, distances[][]int) {
	if x < 0 || x >= len(pipeMap) || y < 0 || y >= len(pipeMap[x]) {
		return 
	} 
	if distances[x][y] != -2 && distances[x][y] <= dist {
		return 
	}
	if pipeMap[x][y] == '.' {
		distances[x][y] = -1
		return
	}

	
	distances[x][y] = dist

	if pipeMap[x][y] == '|' {
		recur(x+1, y, dist + 1, pipeMap, distances)
		recur(x-1, y, dist + 1, pipeMap, distances)
		return
	}
	if pipeMap[x][y] == '-' {
		recur(x, y+1, dist + 1, pipeMap, distances)
		recur(x, y-1, dist + 1, pipeMap, distances)
		return
	}
	if pipeMap[x][y] == 'L' {
		recur(x-1, y, dist + 1, pipeMap, distances)
		recur(x, y+1, dist + 1, pipeMap, distances)
		return
	}
	if pipeMap[x][y] == 'J' {
		recur(x-1, y, dist + 1, pipeMap, distances)
		recur(x, y-1, dist + 1, pipeMap, distances)
		return 
	}
	if pipeMap[x][y] == '7' {
		recur(x+1, y, dist + 1, pipeMap, distances)
		recur(x, y-1, dist + 1, pipeMap, distances)
		return
	}
	if pipeMap[x][y] == 'F' {
		recur(x+1, y, dist + 1, pipeMap, distances)
		recur(x, y+1, dist + 1, pipeMap, distances)
		return 
	}
	
	if x - 1 >= 0 && (pipeMap[x-1][y] == '|' || pipeMap[x-1][y] == '7' || pipeMap[x-1][y] == 'F') {
		recur(x-1, y, dist+1, pipeMap, distances)
	} 
	if x + 1 < len(pipeMap) && (pipeMap[x+1][y] == '|' || pipeMap[x+1][y] == 'L' || pipeMap[x+1][y] == 'J'){
		recur(x+1, y, dist+1, pipeMap, distances)
	} 
	if y - 1 >= 0 && (pipeMap[x][y-1] == 'L' || pipeMap[x][y-1] == 'F' || pipeMap[x][y-1] == '-') {
		recur(x, y-1, dist+1, pipeMap, distances)
	}
	if y + 1 < len(pipeMap[0]) && (pipeMap[x][y+1] == '-' || pipeMap[x][y+1] == 'J' || pipeMap[x][y+1] == '7') {
		recur(x, y+1, dist+1, pipeMap, distances)
	}
}

func main() {
    readFile, err := os.Open("../input.txt")
  
    if err != nil {
        fmt.Println(err)
    }

    fileScanner := bufio.NewScanner(readFile)
    fileScanner.Split(bufio.ScanLines)

	var x, y int
	pipeMap := make([]string, 0, 150)
    for fileScanner.Scan() {
		line := fileScanner.Text();
		pipeMap = append(pipeMap, line)
		if strings.Contains(line, "S") {
			x = len(pipeMap) - 1
			y = strings.Index(line, "S")
		}
    }
	distances := make([][]int, len(pipeMap))
	for i := 0; i < len(distances); i++ {
		distances[i] = make([]int, len(pipeMap[0]))
		for j := 0; j < len(pipeMap[0]); j++ {
			distances[i][j] = -2
		}
	}
	recur(x, y, 0, pipeMap, distances)
	fmt.Println(getMax(distances))
    readFile.Close()
}