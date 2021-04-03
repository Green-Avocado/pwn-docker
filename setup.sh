#!/usr/bin/env bash

gcc ln-static.c -o ln-static --static

sudo docker image rm pwndocker
sudo docker build -t pwndocker .

mkdir -p ~/bin
cp pwndocker.py ~/bin/pwndocker

