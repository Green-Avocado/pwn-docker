#!/usr/bin/env python3

import os
import subprocess
import signal
from optparse import OptionParser



def signal_handler(sig, frame):
    print("\nShutting down container...\n")
    subprocess.run(["docker", "container", "stop", "pwndocker"])
    exit()

def dockerExec(exec_cmd, detach=False):
    dockerExec_cmd = ["docker", "container", "exec"]
    if detach:
        dockerExec_cmd.append("--detach")
    subprocess.run(dockerExec_cmd + ["pwndocker"] + exec_cmd)



usage = "usage: %prog [OPTIONS] BINARY [GLIBC DEB]"
parser = OptionParser(usage=usage)
parser.add_option(
        "-v", "--version",
        action="store_true", dest="version",
        help="display version information and exit"
        )

(options, args) = parser.parse_args()

if options.version:
    print("pwndocker 2.1.0")
    exit()



deb = None

if len(args) == 0:
    parser.error("Missing binary")
elif len(args) == 2:
    deb = args[1]
elif len(args) > 2:
    parser.error("Too many arguments")

binary = args[0]



signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)



cmd = ["docker", "run", "--rm", "--detach"]
cmd.extend(["--name", "pwndocker"])
cmd.extend(["--mount", "type=bind,source={},target=/mnt,readonly".format(os.path.abspath('.'))])
cmd.extend(["--publish", "1337:1337/tcp"])
cmd.extend(["--publish", "13337:13337/tcp"])
cmd.extend(["--cap-add=SYS_PTRACE"])
cmd.extend(["-it"])
cmd.extend(["pwndocker"])

subprocess.run(cmd)



if deb:
    dockerExec(["dpkg-deb", "-R", deb, "/tmp"])
    dockerExec(["sh", "-c", "mv /tmp/lib/x86_64-linux-gnu/* /lib/x86_64-linux-gnu/"])
    dockerExec(["mv", "-r", "/tmp/lib32", "/"])
    dockerExec(["mv", "/tmp/lib/ld-linux.so.2", "/lib"])
    dockerExec(["/tmp/ln-static", "/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2", "/lib64/ld-linux-x86-64.so.2"])



dockerExec(["gdbserver", "--multi", "localhost:13337"], detach=True)
dockerExec(["socat", "TCP-LISTEN:1337,fork,reuseaddr", "EXEC:'/mnt/{}'".format(binary)], detach=True)
subprocess.run(["docker", "attach", "pwndocker"])

