cd /home/och/dev/dexter-fork/lto
clang -g -O1 -mllvm -stats=1 -flto=thin -fuse-ld=lld msg/ext0.cpp msg/ext1.cpp msg/main.cpp -o msg_thin_lto_O1/a.out
