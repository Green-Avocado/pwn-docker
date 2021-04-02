#!/usr/bin/env python3

import os
import subprocess
import signal
from optparse import OptionParser

def sigint_handler(sig, frame):
    if docker:
        docker.terminate()
        subprocess.run(["docker", "container", "stop", "pwndocker"])
    exit()

usage = "usage: %prog [options] binary"
parser = OptionParser(usage=usage)
parser.add_option("--libc", dest="libc",
                  help="libc to copy to docker", metavar="LIBC")
parser.add_option("--ld", dest="ld",
                  help="dynamic linker to copy to docker", metavar="LD")

(options, args) = parser.parse_args()

if len(args) == 0:
    parser.error("Missing binary")
elif len(args) > 1:
    parser.error("Too many arguments")

binary = args[0]
libc = options.libc
ld = options.ld

runstring = ""

if libc and ld:
    runstring += " ln -sfr {} /lib/x86_64-linux-gnu/libc.so.6;".format(libc)
    runstring += " ln -sfr {} /lib/x86_64-linux-gnu/ld-linux-x86-64.so.2;".format(ld)
elif libc or ld:
    parser.error("libc and ld must be provided together")
    exit(1)

runstring += " socat TCP-LISTEN:1337,fork,reuseaddr EXEC:'./{}';".format(binary)

cmd = ["docker", "run", "--rm"]
cmd.extend(["--name", "pwndocker"])
cmd.extend(["--mount", "type=bind,source={},target=/mnt,readonly".format(os.path.abspath('.'))])
cmd.extend(["--publish", "1337:1337/tcp"])
cmd.append("pwndocker")
cmd.extend(["/bin/bash", "-c", runstring])

docker = None
signal.signal(signal.SIGINT, signal_handler)

docker = subprocess.run(cmd)

