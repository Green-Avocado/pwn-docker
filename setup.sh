#!/usr/bin/env bash

docker build -t pwndocker .
ln -sfr pwndocker.py ~/bin/pwndocker
gcc ln-static.c -o ln-static --static

