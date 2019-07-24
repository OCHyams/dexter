// Purpose:
//      Check that DexExpectWatchValue applies no penalties when expected
//      program states are found.
//
// RUN: dexter.py test --fail-lt 1.0 -w \
// RUN:     --builder clang --debugger lldb --cflags "-O0 -glldb" -- %S \
// RUN:     | FileCheck %s
// CHECK: gcd:

int GCD(int lhs, int rhs)
{
    if (rhs == 0)
        return lhs; // DexLabel('check')
    return GCD(rhs, lhs % rhs);
}

int main()
{
    return GCD(111, 259);
}

/*
DexExpectProgramState({
    'frames': [
        {
            'location': {
                'lineno': 'check'
            },
            'watches': {
                'lhs': '37', 'rhs': '0'
            }
        },
        {
            'watches': {
                'lhs': '111', 'rhs': '37'
            }
        },
        {
            'watches': {
                'lhs': '259', 'rhs': '111'
            }
        },
        {
            'watches': {
                'lhs': '111', 'rhs': '259'
            }
        }
    ]
})
*/
