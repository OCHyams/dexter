cd /home/och/dev/dexter-fork/lto
clang -g -O2 -mllvm -stats=0 -flto=thin -fuse-ld=lld msg/ext0.cpp msg/ext1.cpp msg/main.cpp -o msg_thin_lto_O2/a.out
