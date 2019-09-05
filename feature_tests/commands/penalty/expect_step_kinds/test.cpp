// Purpose:
//      Check that \DexExpectStepKind correctly applies a penalty when
//      unexpected step kinds are encountered.
//
// REQUIRES: linux, clang, lldb
//
// RUN: not dexter.py test --fail-lt 1.0 -w  \
// RUN:     --builder clang --debugger lldb --cflags "-O0 -g" -- %S \
// RUN:     | FileCheck %s
// CHECK: expect_step_kinds:

int abs(int i){
    return i < 0? i * -1: i;
}

int main()
{
    volatile int x = 2;
    for (int i = 0; i < x; ++i) {
        abs(i);
    }
    return 0;
}

// DexExpectStepKind('FUNC', 5)
// DexExpectStepKind('FUNC_EXTERNAL', 2)
// DexExpectStepKind('VERTICAL_BACKWARD', 2)
