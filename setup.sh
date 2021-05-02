#!/usr/bin/env bash

gcc ln-static.c -o ./docker/ln-static --static

sudo docker image rm pwndocker
sudo docker build -t pwndocker ./docker

install -D ./src/pwndocker.py ~/bin/pwndocker
install -D ./src/glibc-fetch.py ~/bin/glibc-fetch

