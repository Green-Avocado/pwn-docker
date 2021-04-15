#!/usr/bin/env python3

import requests
import re
import subprocess
from optparse import OptionParser

usage = "usage: %prog LIBC"
parser = OptionParser(usage=usage)
parser.add_option(
        "-v", "--version",
        action="store_true", dest="version",
        help="display version information and exit"
        )
(options, args) = parser.parse_args()

if options.version:
    print("glibc-fetch 1.1.0")
    exit()

if len(args) == 0:
    parser.error("Missing libc argument")
elif len(args) > 1:
    parser.error("Too many arguments")

libc_filename = args[0]

try:
    libc = open(libc_filename, 'rb').read()
    libc_ver = re.search(b'GNU C Library \(Ubuntu GLIBC (.+?)\)', libc).group(1).decode()

    fileinfo = subprocess.check_output(['file', '-b', libc_filename]).split()[1].decode()
    if fileinfo == "64-bit":
        arch = ""
    elif fileinfo == "32-bit":
        arch = "-i386"
    else:
        raise
except:
    print("fatal error")
    exit()

url = "https://launchpad.net/ubuntu/+archive/primary/+files/libc6{}_{}_amd64.deb".format(arch, libc_ver)

print(url)

r = requests.get(url)
open('glibc.deb', 'wb').write(r.content)

