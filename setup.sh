#!/usr/bin/env bash

gcc ln-static.c -o ln-static --static

sudo docker image rm pwndocker
sudo docker build -t pwndocker .

mkdir -p ~/bin
install pwndocker.py ~/bin/pwndocker

