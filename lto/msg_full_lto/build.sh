cd /home/och/dev/dexter-fork/lto
clang -g -O2 -mllvm -stats=1 -flto=full -fuse-ld=lld msg/ext0.cpp msg/ext1.cpp msg/main.cpp -o msg_full_lto/a.out
