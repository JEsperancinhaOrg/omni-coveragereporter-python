#!/bin/bash
export GOPATH=$HOME/go/
export PATH="$GOROOT/bin:$PATH"
export PATH="$PATH:$GOPATH/bin"
unset GO111MODULE
export GO111MODULE=auto
