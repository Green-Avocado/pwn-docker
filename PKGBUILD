# Maintainer: Green-Avocado <greenavocado@protonmail.com>
pkgname='pwndocker'
pkgver=2.2.0
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
  make DESTDIR="$pkgdir" PREFIX="/usr" _install
  install -Dm644 pwndocker.tar "$pkgdir/usr/share/$pkgname/pwndocker.tar"
}
