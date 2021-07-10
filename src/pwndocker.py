#!/usr/bin/env python3

import os
import subprocess
import signal
from optparse import OptionParser



def signal_handler(sig, frame):
    print("\nShutting down container...\n")
    subprocess.run(["docker", "container", "stop", dockerName])
    exit()

def dockerExec(exec_cmd, detach=False, quiet=True):
    dockerExec_cmd = ["docker", "container", "exec", "--workdir /mnt"]

    if detach:
        dockerExec_cmd.append("--detach")

    fullcmd = dockerExec_cmd + [dockerName] + exec_cmd

    if quiet:
        subprocess.run(fullcmd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL)
    else:
        subprocess.run(fullcmd)



usage = "usage: %prog [OPTIONS] BINARY [DEB]"
parser = OptionParser(usage=usage)
parser.add_option(
        "-v", "--version",
        action="store_true", dest="version",
        help="display version information and exit"
        )
parser.add_option(
        "-p", "--port",
        dest="socatPort",
        help="set socat port", metavar="PORT"
        )
parser.add_option(
        "-g", "--gdb",
        dest="gdbserverPort",
        help="set gdbserver port", metavar="PORT"
        )
parser.add_option(
        "-n", "--name",
        dest="dockerName",
        help="set container name", metavar="NAME"
        )

(options, args) = parser.parse_args()

if options.version:
    print("pwndocker 2.2.0")
    exit()



deb = None

if len(args) == 0:
    parser.error("Missing binary")
elif len(args) == 2:
    deb = args[1]
elif len(args) > 2:
    parser.error("Too many arguments")

binary = args[0]

dockerName = options.dockerName or "pwndocker"
socatPort = options.socatPort or "1337"
gdbserverPort = options.gdbserverPort or "13337"



signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)



# start docker container with ptrace enabled, ports 1337 and 13337 exposed, current dir mounted as RO
cmd = ["docker", "run", "--rm", "--detach"]
cmd.extend(["--name", dockerName])
cmd.extend(["--mount", "type=bind,source={},target=/mnt,readonly".format(os.path.abspath('.'))])
cmd.extend(["--publish", "{}:1337/tcp".format(socatPort)])
cmd.extend(["--publish", "{}:13337/tcp".format(gdbserverPort)])
cmd.extend(["--cap-add=SYS_PTRACE"])
cmd.extend(["-it"])
cmd.extend(["pwndocker"])

subprocess.run(cmd)



if deb:
    dockerExec(["dpkg-deb", "-R", deb, "/tmp"], quiet=False)

    # move glibc files
    dockerExec(["sh", "-c",
        "mv /tmp/lib/x86_64-linux-gnu/* /lib/x86_64-linux-gnu/"])
    dockerExec(["sh", "-c",
        "mv /tmp/lib32/* /lib/i386-linux-gnu/"])

    # link ld
    dockerExec(["/tmp/ln-static",
        "/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2",
        "/lib64/ld-linux-x86-64.so.2"])
    dockerExec(["/tmp/ln-static",
        "/lib/i386-linux-gnu/ld-linux.so.2",
        "/lib/ld-linux.so.2"])



# start gdbserver and socat
dockerExec(["gdbserver", "--multi", "localhost:13337"], detach=True)
dockerExec(["socat", "TCP-LISTEN:1337,fork,reuseaddr", "EXEC:'{}'".format(binary)], detach=True)

# attach to docker shell
subprocess.run(["docker", "attach", dockerName])

