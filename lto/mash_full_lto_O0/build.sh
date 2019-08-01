cd /home/och/dev/dexter-fork
clang -g -O0 -mllvm -stats=1 -flto=full -fuse-ld=lld lto/mash/ext0.cpp lto/mash/ext1.cpp lto/mash/main.cpp -o lto/mash_full_lto_O0/a.out
