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

// A Determinant
// B Denominator X
// C Denominator Y
func getTCC(img1 image.Image, img2 image.Image, channel int) float64 {
	dotLength := img1.Bounds().Dx()
	dotHeight := img1.Bounds().Dy()
	prod12 := 0.0
	prod1to2 := 0.0
	prod2to2 := 0.0
	for x := 0; x < dotLength; x++ {
		for y := 0; y < dotHeight; y++ {
			point1 := multicomparer.GetChannelValue(img1, x, y, channel)
			point2 := multicomparer.GetChannelValue(img2, x, y, channel)

			prod12 += point1 * point2
			prod1to2 += math.Pow(point1, 2)
			prod2to2 += math.Pow(point2, 2)
		}
	}
	return prod12 / (prod1to2 + prod2to2 - prod12)
}
