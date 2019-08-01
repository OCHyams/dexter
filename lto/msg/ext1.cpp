#include <stdio.h>
unsigned generate_msg_id(unsigned val, unsigned max) {
    return val % max; // DexLabel('gen')
}

// DexExpectWatchValue('max', '3', on_line='gen')
// DexExpectWatchValue('val', '1', on_line='gen')
