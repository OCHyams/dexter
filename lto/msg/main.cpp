#include <stdio.h>

const char* get_msg(unsigned);
unsigned get_msg_id_max();

unsigned generate_msg_id(unsigned val, unsigned max);


int main(int argc, char** argv) {
    int msg_max_id = get_msg_id_max();
    int msg_id = generate_msg_id(argc, msg_max_id);
    const char *msg = get_msg(msg_id);
    printf("%d: %s\n", msg_id, msg);
    return 0; // DexLabel('ret')
}

// DexExpectWatchValue('msg_max_id', '3', on_line='ret')
// DexExpectWatchValue('msg_id', '1', on_line='ret')
