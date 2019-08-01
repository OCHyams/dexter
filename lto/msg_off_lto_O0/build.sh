cd /home/och/dev/dexter-fork/lto
clang -g -O0 -mllvm -stats=1 -fuse-ld=lld msg/ext0.cpp msg/ext1.cpp msg/main.cpp -o msg_off_lto_O0/a.out
