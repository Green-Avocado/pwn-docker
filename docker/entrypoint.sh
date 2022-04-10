#!/usr/bin/env bash

if [ $# -eq 0 ]; then
    echo "No arguments supplied"
    exit 1
fi

if [ $# -gt 2 ]; then
    echo "Too many arguments"
    exit 1
fi

if [ -n "$2" ]; then
    dpkg --force-all -i "$2"
fi

(&>/dev/null gdbserver --multi localhost:13337 &)
(&>/dev/null socat TCP-LISTEN:1337,fork,reuseaddr EXEC:"$1" &)

htop
