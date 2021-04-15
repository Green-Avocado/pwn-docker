#!/usr/bin/env python3

import requests
import re
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
    print("glibc-fetch 1.0.1")
    exit()

if len(args) == 0:
    parser.error("Missing libc argument")
elif len(args) > 1:
    parser.error("Too many arguments")

libc_filename = args[0]

try:
    libc = open(libc_filename, 'rb').read()
    libc_ver = re.search(b'GNU C Library \(Ubuntu GLIBC (.+?)\)', libc).group(1).decode()
except:
    print("fatal error")
    exit()

url = "https://launchpad.net/ubuntu/+archive/primary/+files/libc6_{}_amd64.deb".format(libc_ver)

print(url)

r = requests.get(url)
open('glibc.deb', 'wb').write(r.content)

