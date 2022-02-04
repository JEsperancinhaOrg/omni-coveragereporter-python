package main

import (
	"fmt"
	"github.com/jesperancinha/images-go/points"
	"image"
	"os"
)

func main() {
	arguments := os.Args
	filename1 := arguments[1]
	filename2 := arguments[2]

	compareImages(filename1, filename2)
}

func compareImages(filename1 string, filename2 string) {
	fImg1, _ := os.Open(filename1)
	defer fImg1.Close()
	img1, _, _ := image.Decode(fImg1)

	fImg2, _ := os.Open(filename2)
	defer fImg2.Close()
	img2, _, _ := image.Decode(fImg2)

	ratio12R := getPCC(img1, img2, multicomparer.R)
	ratio12G := getPCC(img1, img2, multicomparer.G)
	ratio12B := getPCC(img1, img2, multicomparer.B)
	ratio12A := getPCC(img1, img2, multicomparer.A)
	fmt.Println("Ratio for R [", filename1, "] and [", filename2, "] is:", ratio12R)
	fmt.Println("Ratio for G [", filename1, "] and [", filename2, "] is:", ratio12G)
	fmt.Println("Ratio for B [", filename1, "] and [", filename2, "] is:", ratio12B)
	fmt.Println("Ratio for A [", filename1, "] and [", filename2, "] is:", ratio12A)
}
