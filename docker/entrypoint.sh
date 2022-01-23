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
    dpkg-deb -R "$2" /tmp

    mv -n /tmp/lib/x86_64-linux-gnu/* /lib/x86_64-linux-gnu/
    mv -f /tmp/lib/x86_64-linux-gnu/* /lib/x86_64-linux-gnu/

    mv -n /tmp/lib32/* /lib/i386-linux-gnu/
    mv -f /tmp/lib32/* /lib/i386-linux-gnu/

    /tmp/ln-static /lib/x86_64-linux-gnu/ld-linux-x86-64.so.2 /lib64/ld-linux-x86-64.so.2
    /tmp/ln-static /lib/i386-linux-gnu/ld-linux.so.2 /lib/ld-linux.so.2
fi

gdbserver --multi localhost:13337 &
socat TCP-LISTEN:1337,fork,reuseaddr EXEC:"$1" &
top
