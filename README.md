# pwndocker

Create a lightweight docker container for solving CTF challenges

## Setup

```
git clone https://github.com/Green-Avocado/pwndocker.git
cd pwndocker
sudo ./setup.sh
```

Do not run setup as root.

## Usage:

Run `sudo pwndocker [binary]` from your working directory.

Optionally pass a libc and dynamic linker through the `--libc=LIBC` and `--ld=LD` options.

Connect using `nc localhost 1337`.

