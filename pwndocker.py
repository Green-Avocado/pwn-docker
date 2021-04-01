#!/usr/bin/env python3

import os
import subprocess
from optparse import OptionParser

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

runstring = "cd /mnt;"

if libc and ld:
    runstring += " ln -s {} /lib/x64_64-linux-gnu/libc.so.6;".format(libc)
    runstring += " ln -s {} /lib/x64_64-linux-gnu/ld-linux-x86-64.so.2;".format(ld)
elif libc or ld:
    parser.error("libc and ld must be provided together")
    exit(1)

runstring += " ./{};".format(binary)

cmd = ["docker", "run", "--rm"]
cmd.append("-it")
cmd.extend(["--name", "pwndocker"])
cmd.extend(["--mount", "type=bind,source={},target=/mnt,readonly".format(os.path.abspath('.'))])
cmd.append("debian:stable-slim")
cmd.extend(["/bin/bash", "-c", runstring])

subprocess.run(cmd)
