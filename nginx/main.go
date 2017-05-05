package main

import "fmt"
import "github.com/yudai/gotty/app"

func main() {
	ret, _ := app.CheckPods("caa83842-df79-440e-806f-515fd2558fdc", "0e4a97b9800f540b360a21ba434565313d94cc8250a2dd1d32d4a3bf4336e849")

	if ret {
		fmt.Printf("is true")
	}else {
		fmt.Printf("is false")
	}

}
