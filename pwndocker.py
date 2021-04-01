#!/usr/bin/env python3

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

cmd = ["docker", "run", "--rm", "-it"]
cmd.append("debian:stable-slim")
cmd.append("/setup.sh")
cmd.append(binary)

if libc and ld:
    cmd.append(libc)
    cmd.append(ld)
elif libc or ld:
    parser.error("libc and ld must be provided together")
    exit(1)

docker = subprocess.run(cmd)

