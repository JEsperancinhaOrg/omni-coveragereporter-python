package main

import (
	"github.com/jesperancinha/images-go/points"
	"image"
	// Needs to be here to avoid nil error:
	// https://github.com/golang/go/issues/10389
	// http://www.goinggo.net/2014/09/go-compiler-nil-pointer-checks.html
	_ "image/jpeg"
	"math"
)

func getPCC(img1 image.Image, img2 image.Image, channel int) float64 {
	average1 := getAveragePerChannel(img1, channel)
	average2 := getAveragePerChannel(img2, channel)

	ratio := getPCCDetail(img1, img2, average1, average2, channel)
	return ratio
}

// A Determinant
// B Denominator X
// C Denominator Y
func getPCCDetail(img1 image.Image, img2 image.Image, average1 float64, average2 float64, channel int) float64 {
	dotLength := img1.Bounds().Dx()
	dotHeight := img1.Bounds().Dy()
	dett := 0.0
	denX := 0.0
	denY := 0.0
	for x := 0; x < dotLength; x++ {
		for y := 0; y < dotHeight; y++ {
			diffX := multicomparer.GetChannelValue(img1, x, y, channel) - average1
			diffY := multicomparer.GetChannelValue(img2, x, y, channel) - average2
			dett += (diffX) * (diffY)
			denX += math.Pow(diffX, 2)
			denY += math.Pow(diffY, 2)
		}
	}
	return dett / (math.Sqrt(denX) * math.Sqrt(denY))
}

func getAveragePerChannel(img image.Image, channel int) float64 {
	dotLength := img.Bounds().Dx()
	dotHeight := img.Bounds().Dy()
	dotCount := dotLength * dotHeight
	dotAverage := 0.0

	for x := 0; x < dotLength; x++ {
		for y := 0; y < dotHeight; y++ {
			dotAverage += float64(multicomparer.GetChannelValue(img, x, y, channel)) / float64(dotCount)
		}
	}
	return dotAverage
}
