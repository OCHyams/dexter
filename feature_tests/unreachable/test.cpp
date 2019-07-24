// Purpose:
//    Check that DexUnreachable causes DExTer to report a fail if the command's
//    line is stepped on.
//
// RUN: not dexter.py test --fail-lt 1.0 -w \
// RUN:     --builder clang --debugger lldb --cflags "-O0 -g" -- %S \
// RUN:     | FileCheck %s
// CHECK: unreachable

int
main()
{
  return 0;  // DexUnreachable()
}
