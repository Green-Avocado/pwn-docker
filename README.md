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

### Download glibc deb file

Use `glibc-fetch LIBC` to download a matching deb file from the Ubuntu archives.

### Create docker container

Run `sudo pwndocker BINARY` from your working directory.
The binary should be given as a relative path.

Optionally pass a glibc deb file as a second argument.

### Connect to docker container

Connect to socat using:

```
$ nc localhost 1337
```

### Connect to gdbserver

Connect to the gdbserver using:
```
(gdb) target extended-remote localhost:13337
```

