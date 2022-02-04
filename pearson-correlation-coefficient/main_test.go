package main

import (
	_ "fmt"
	_ "github.com/jesperancinha/images-go/points"
	_ "github.com/stretchr/testify/assert"
	_ "image"
	_ "os"
	"testing"
)

func TestGetChannelValue_Red(t *testing.T) {
	compareImages("zeeland1.jpg", "zeeland2.jpg")
}
