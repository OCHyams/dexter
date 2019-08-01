
// ext0.cpp
int sum_range(int argc, char **);

// ext1.cpp
int something();

int main(int argc, char** argv) {
    int a = something();
    int b = sum_range(argc, argv);
    return 0; // DexLabel('ret')
}

// DexExpectWatchValue('a', '0', on_line='ret')
// DexExpectWatchValue('b', '10', on_line='ret')
