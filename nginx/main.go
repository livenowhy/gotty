package main

import (
	"path/filepath"
	"os"
	"os/exec"
	"fmt"
	"strings"
)

func main() {





	file, err := exec.LookPath(os.Args[0])
	if err != nil {
		fmt.Println(err.Error())
	}
	path, err := filepath.Abs(file)
	if err != nil {
		fmt.Println(err.Error())
	}
	i := strings.LastIndex(path, "/")
	if i < 0 {
		i = strings.LastIndex(path, "\\")
	}
	if i < 0 {
		fmt.Println(`error: Can't find "/" or "\".`)
	}

	fmt.Println(string(path[0 : i+1]))

}
