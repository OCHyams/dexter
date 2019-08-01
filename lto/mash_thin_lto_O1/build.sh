cd /home/och/dev/dexter-fork/lto
clang -g -O1 -mllvm -stats=1 -flto=thin -fuse-ld=lld mash/ext0.cpp mash/ext1.cpp mash/main.cpp -o mash_thin_lto_O1/a.out
