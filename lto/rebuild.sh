
# Args:
SRC_FOLDER=$1

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

$DIR/lto.sh thin $SRC_FOLDER
$DIR/lto.sh full $SRC_FOLDER
$DIR/lto.sh off $SRC_FOLDER