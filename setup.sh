#!/usr/bin/env bash

gcc ln-static.c -o ln-static --static

sudo docker image rm pwndocker
sudo docker build -t pwndocker .

install -D pwndocker.py ~/bin/pwndocker
install -D glibc-fetch.py ~/bin/glibc-fetch

