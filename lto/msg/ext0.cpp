
static const char* msg_hello = "Hello, World!";
static const char* msg_bye = "Goodbye, World!";
static const char* msg_default = "._.";

enum MSG_ID {
    id_hello,
    id_bye,

    id_default,
    id_max
};

const char* get_msg(unsigned id) {
    switch (id) { // DexLabel('switch')
        case id_hello: return msg_hello;
        case id_bye: return msg_bye;
    }
    return msg_default;
}

const unsigned get_msg_id_max()
{
    return id_max;
}

// DexExpectWatchValue('id', '1', on_line='switch')
