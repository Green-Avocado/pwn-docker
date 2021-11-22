# Maintainer: Green-Avocado <greenavocado@protonmail.com>
pkgname='pwndocker'
pkgver=2.2.0.r10.g5002d2e
pkgrel=1
pkgdesc="Create a lightweight docker container for solving CTF challenges."
arch=('x86_64')
url="https://github.com/Green-Avocado/pwndocker"
license=('GPL3')
depends=(
  'python3'
  'docker'
)
makedepends=(
  'git'
  'sudo'
)
install="$pkgname.install"
source=("$pkgname::git+https://github.com/Green-Avocado/pwndocker.git")
sha256sums=("SKIP")

pkgver() {
  cd "$srcdir/$pkgname"
  git describe --long | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  cd "$srcdir/$pkgname"
  make DESTDIR="$pkgdir" PREFIX="/usr" build
}

package() {
  cd "$srcdir/$pkgname"
  install -Dm644 ./pwndocker.tar "$pkgdir/usr/share/$pkgname"
  install -Dm755 ./src/pwndocker.py "$pkgdir"/usr/bin/pwndocker
  install -Dm755 ./src/glibc-fetch.py "$pkgdir"/usr/bin/glibc-fetch
}
