#!/usr/bin/env python3

from os import execvp, path
from optparse import OptionParser

VERSION="3.0.0"

parser = OptionParser(usage="usage: %prog [OPTIONS] BINARY [DEB]")
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
    print("pwndocker {}".format(VERSION))
    exit()

dockerName = options.dockerName or None
socatPort = options.socatPort or "1337"
gdbserverPort = options.gdbserverPort or "13337"

# start docker container with ptrace enabled, ports 1337 and 13337 exposed, current dir mounted as RO
cmd = ["docker", "run", "--rm"]
if dockerName:
    cmd.extend(["--name", dockerName])
cmd.extend(["--mount", "type=bind,source={},target=/mnt,readonly".format(path.abspath('.'))])
cmd.extend(["--publish", "{}:1337/tcp".format(socatPort)])
cmd.extend(["--publish", "{}:13337/tcp".format(gdbserverPort)])
cmd.extend(["--cap-add=SYS_PTRACE"])
cmd.extend(["pwndocker"])
cmd.extend(args)

execvp("docker", cmd)
