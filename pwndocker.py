#!/usr/bin/env python3

import os
import subprocess
import signal
from optparse import OptionParser

def signal_handler(sig, frame):
    print("\nShutting down container...\n")
    subprocess.run(["docker", "container", "stop", "pwndocker"])
    exit()

def dockerExec(exec_cmd):
    subprocess.run(["docker", "container", "exec", "--detach", "pwndocker"] + exec_cmd)

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

if (not libc and ld) or (libc and not ld):
    parser.error("libc and ld must be provided together")
    exit(1)

cmd = ["docker", "run", "--rm", "--detach"]
cmd.extend(["--name", "pwndocker"])
cmd.extend(["--mount", "type=bind,source={},target=/mnt,readonly".format(os.path.abspath('.'))])
cmd.extend(["--publish", "1337:1337/tcp"])
cmd.extend(["--publish", "13337:13337/tcp"])
cmd.extend(["--cap-add=SYS_PTRACE"])
cmd.extend(["-it"])
cmd.extend(["pwndocker"])

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

subprocess.run(cmd)

if libc and ld:
    dockerExec(["/tmp/ln-static", "/mnt/{}".format(libc), "/lib/x86_64-linux-gnu/libc.so.6"])
    dockerExec(["/tmp/ln-static", "/mnt/{}".format(ld), "/lib/x86_64-linux-gnu/ld-2.19.so"])

dockerExec(["gdbserver", "--multi", "localhost:13337"])
dockerExec(["socat", "TCP-LISTEN:1337,fork,reuseaddr", "EXEC:'/mnt/{}'".format(binary)])
subprocess.run(["docker", "attach", "pwndocker"])

