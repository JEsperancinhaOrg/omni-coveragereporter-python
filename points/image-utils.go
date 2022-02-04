package multicomparer

import (
	"image"
	_ "image/jpeg"
)

const (
	R = iota
	G = iota
	B = iota
	A = iota
)

func GetChannelValue(img image.Image, x int, y int, channel int) float64 {
	var channelValue uint32 = 0
	switch channel {
	case R:
		channelValue, _, _, _ = img.At(x, y).RGBA()

	case G:
		_, channelValue, _, _ = img.At(x, y).RGBA()

	case B:
		_, _, channelValue, _ = img.At(x, y).RGBA()

	case A:
		_, _, _, channelValue = img.At(x, y).RGBA()
	}
	return float64(channelValue)
}
