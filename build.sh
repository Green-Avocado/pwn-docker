#!/usr/bin/env bash

mkdir -p build

sudo docker build -t pwndocker-build -f build.Dockerfile PKGBUILD/ &&
sudo docker run --rm --mount type=bind,src="$(pwd)",dst=/mnt pwndocker-build
