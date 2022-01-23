# Maintainer: Green-Avocado <greenavocado@protonmail.com>
pkgname=pwndocker
pkgver=3.0.0
pkgrel=1
pkgdesc="Create a lightweight docker container for solving CTF challenges."
arch=('x86_64')
url="https://github.com/Green-Avocado/pwndocker"
license=('GPL3')
depends=(
  'python3'
  'docker'
)
install="$pkgname.install"
makedepends=('git')
source=("$pkgname::git+https://github.com/Green-Avocado/pwndocker.git")
sha256sums=("SKIP")

pkgver() {
  cd "$srcdir/$pkgname"
  git describe --long | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

package() {
  cd "$srcdir/$pkgname"
  make DESTDIR="$pkgdir/usr" install
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
