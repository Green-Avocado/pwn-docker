#!/usr/bin/env bash

gcc ln-static.c -o ln-static --static
docker build -t pwndocker .

ln -sfr pwndocker.py ~/bin/pwndocker

