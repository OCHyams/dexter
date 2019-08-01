
# Args:
SRC_FOLDER=$1

./lto.sh thin $SRC_FOLDER
./lto.sh full $SRC_FOLDER
./lto.sh off $SRC_FOLDER