#!/usr/bin/env bash

gcc ./src/ln-static.c -o ./docker/ln-static --static

sudo docker image rm pwndocker
sudo docker build -t pwndocker ./docker

install -D ./src/pwndocker.py ~/bin/pwndocker
install -D ./src/glibc-fetch.py ~/bin/glibc-fetch

echo "#!/usr/bin/env bash" > uninstall.sh
echo "sudo docker image rm pwndocker" >> uninstall.sh
echo "rm ~/bin/pwndocker" >> uninstall.sh
echo "rm ~/bin/glibc-fetch" >> uninstall.sh
chmod +x uninstall.sh

