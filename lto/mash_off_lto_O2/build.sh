cd /home/och/dev/dexter-fork
clang -g -O2 -mllvm -stats=1 -fuse-ld=lld lto/mash/ext0.cpp lto/mash/ext1.cpp lto/mash/main.cpp -o lto/mash_off_lto_O2/a.out
