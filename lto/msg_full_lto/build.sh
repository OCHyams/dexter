cd /home/och/dev/dexter-fork
clang -g -O2 -mllvm -stats=1 -flto=full -fuse-ld=lld lto/msg/ext0.cpp lto/msg/ext1.cpp lto/msg/main.cpp -o lto/msg_full_lto/a.out
