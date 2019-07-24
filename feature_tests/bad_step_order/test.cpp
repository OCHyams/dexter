// Purpose:
//      Check that DexExpectStepOrder correctly applies a penalty for steps
//      found out of expected order.
//
// RUN: not dexter.py test --fail-lt 1.0 -w \
// RUN:     --builder clang --debugger lldb --cflags "-O0 -g" -- %S \
// RUN:     | FileCheck %s
// CHECK: bad_step_order:

int main()
{
    volatile int x = 1; // DexExpectStepOrder(3)
    volatile int y = 1; // DexExpectStepOrder(1)
    volatile int z = 1; // DexExpectStepOrder(2)
    return 0;
}
