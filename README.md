# pwndocker

Create a lightweight docker container for solving CTF challenges

## Setup

### Prerequisites

Requires that docker is installed and running.

### ArchLinux

```
makepkg -si
```

### Other

```
make install
```

## Usage

### Download glibc deb file

Use `fetch-libc LIBC` to download a matching deb file from the Ubuntu archives.

### Create docker container

Run `sudo pwndocker EXEC_CMD GLIBC_DEB` from your working directory.
The binary should be given as a relative path.

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

## Uninstall

```
make remove
```
