#include <unistd.h>

int main(int argc, char **argv)
{
    remove(argv[2]);
    symlink(argv[1], argv[2]);
}

