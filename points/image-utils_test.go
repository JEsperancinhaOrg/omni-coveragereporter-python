package multicomparer

import (
	"github.com/stretchr/testify/assert"
	"image"
	_ "image/jpeg"
	"os"
	"testing"
)

func TestGetChannelValue_Red(t *testing.T) {
	fImg1, _ := os.Open("icecold.jpg")
	defer fImg1.Close()
	img1, _, _ := image.Decode(fImg1)
	assert.EqualValues(t, 54901, GetChannelValue(img1, 0, 0, R), "Wrong Red value found for image")
}

func TestGetChannelValue_Green(t *testing.T) {
	fImg1, _ := os.Open("icecold.jpg")
	defer fImg1.Close()
	img1, _, _ := image.Decode(fImg1)
	assert.EqualValues(t, 56918, GetChannelValue(img1, 0, 0, G), "Wrong Red value found for image")
}

func TestGetChannelValue_Blue(t *testing.T) {
	fImg1, _ := os.Open("icecold.jpg")
	defer fImg1.Close()
	img1, _, _ := image.Decode(fImg1)
	assert.EqualValues(t, 63405, GetChannelValue(img1, 0, 0, B), "Wrong Red value found for image")
}

func TestGetChannelValue_Alpha(t *testing.T) {
	fImg1, _ := os.Open("icecold.jpg")
	defer fImg1.Close()
	img1, _, _ := image.Decode(fImg1)
	assert.EqualValues(t, 65535, GetChannelValue(img1, 0, 0, A), "Wrong Red value found for image")
}
