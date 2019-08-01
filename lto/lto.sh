#/usr/bin

# Args:
LTOL=$1             # LTO level ('thin', 'full', 'off')
SRC_FOLDER=$2
OUT_FOLDER=$3       # Can be empty


# Tweak:
OPTL=2          # Optimsation level
STATS=1         # Stat report (0, 1)
# Comma separated list of ld flags.
LFLAGLIST=""


# Script:
if [ "$LTOL" = "off" ]
then LTOL=""
else LTOL="-flto="$LTOL
fi

CFLAGS="-g -O$OPTL -mllvm -stats=$STATS $LTOL -fuse-ld=lld"

if [ -z "$LFLAGLIST" ]
then LFLAGS=""
else LFLAGS="-Wl,$LFLAGLIST"
fi

SRC_FILES=$(ls $SRC_FOLDER/*.cpp)

if [ -z $OUT_FOLDER ]
then OUT_FOLDER="$SRC_FOLDER"_out
fi

mkdir -p $OUT_FOLDER

CMD="clang $CFLAGS $LFLAGS $SRC_FILES -o $OUT_FOLDER/a.out"

BUILD_FILE="$OUT_FOLDER/build.sh"

echo $CMD
echo "cd" $(pwd) > $BUILD_FILE
echo $CMD >> $BUILD_FILE

# Execute cmd
$CMD
