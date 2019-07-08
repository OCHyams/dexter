# DexVerify
## Contents
1. Introduction
2. Motivation
3. Theory
4. Quick reference

## 1. Introduction
A DexVerify command takes the form `DexVerify(p: Proposition)`. It will verify
that the proposition `p` is true. The most basic proposition, an atomic
proposition, expresses the expected state of the program at a given point in
time, or `True` or `False`.

For example, if you wanted to verify that at a given point in time the variable
`a` is equal to `5`, you may write (1):
```
DexVerify(Expect('a', '5'))
```

In this example, it just so happens that the "given point in time" is the first
step that the debugger takes (2). This is not a very useful verification
because we could be stepping through pre-main startup code.

If you want to check that eventually a local variable `a` is `5` you'd write:
```
DexVerify(Eventually(Expect('a', '5')))
```

You can try this yourself (3, 4):
```
somewhere/dexter/examples/intro_0
$ cat test.cpp
int main()
{
    for (int a = 0; a < 10; ++i)
        ;
    return 0;
}

somewhere/dexter/examples/intro_0
$ cd ../../

somewhere/dexter
$ python dexter.py test --builder clang --debugger lldb --cflags "-O0 -g" -- examples/intro_0
intro_0: 1.000
```

`Eventually` is a temporal operator. **Temporal** operators work over **time**.
This one is easy to work with. simply, `Eventually(p)` means that p must become
true at some point during program execution.

`Eventually(p)` is defined as `Until(True, p)` (see the
[source](dex/command/commands/LTD/public/CompositeOperators.py)).
It's easy to explain how this works if we take a look at `Until(p, q)`.
`Until` and `Weak` (see the Quick reference) are used to define all other
temporal operators. All operators are exposed as functions so the formulae
read in Polish, or 'prefix', notation.

`Until(p, q)` means that `q` must hold in the future, and **until** then `p`
must hold.

Looking at `Eventually(p)` again then; `Until(True, p)` can be translated to
"`p` must hold in the future, and until then, `True` must hold". `True` *is*
always `True` so you could instead just say "`p` must hold in the future".

Temporal operators are very useful but are not a catch-all solution. What if
you want to say eventually `a == 5` and eventually `b == 1`? It's pretty much
as easy as writing that. This is where boolean connectives come in:
```
DexVerify(And(Eventually(Expect('a', '5')), Eventually(Expect('b', '1'))))
```

This formula doesn't impose any ordering on the `Expect` propositions.
If you want to say that `b == 1` at some point in the future *after*
`a == 5` you'd write:
```
DexVerify(Eventually(And(Expect('a', 5), Eventually(Expect('b', 1)))))
```


## Motivation

We needed a better way to represent the changes in program state.
@@TODO Write more about why we chose LTL and talk about regex


## Thoery
The DexVerify command formulae are based on Linear Temporal Logic (LTL).
The standard definition of LTL is as follows (modified from [this](https://www.win.tue.nl/~jschmalt/teaching/2IX20/reader_software_specification_ch_9.pdf) source):

```
p ::= a  |  p /\ p  |  !p  |  Xp |  p U p
```

Where:
* `a` is an atomic proposition
* `p` represents a valid LTL formula
* `X` denotes the ”next” operator (5)
* `U` denotes the ”until” operator
* `!` denotes negation
* `/\` denotes logical "and"


Usual boolean connectives can be derived:
```
!(p /\ q) == p \/ q   // (disjunciton): i.e. OR
!p \/ q == p --> q    // (implication):
```

From the syntax, we define the following:
```
p \/ !p == True
!True == False
```

Further temporal operators can be derived:
```
F p == true U p  // p will hold at some point in the Future.
```
There are others, e.g. Weak(W) and Release(R) and more.

Operator precedence:
1. Unary operators
2. Binary temporal
3. Binary boolean
---

[This](http://www.lsv.fr/~gastin/ltl2ba/index.php) website is a fantastic
resource -- view your LTL as a Büchi automaton.

## LTD (Linear Temporal Dexter commands)
We expose the LTL operators as functions. This makes the formulae easy to parse
because the functions will map directly to python like the existing DexCommands.

Temporal operators are right associative and boolean connectives are left
associative.

### LTD functors
```
Proposition
  // Atomic propositions
  ExpectValues(Proposition)
    vars: list
    values: list
  ExpectStack(Proposition)
    frames: list
  ExpectState(ExpectValues, ExpectStack)

  // Unary operators
  Not(Proposition)
    prop: Proposition
  Next(Proposition)

  // Binary boolean operators
  BinaryBoolean(Proposition)
    Or(BinaryBoolean)
      list: Proposition
    And(BinaryBoolean)
      list: Proposition

  // Binary temporal operators
  Until(BinaryTemporal)
    lhs: Proposition
    rhs: Proposition
```
The binary boolean operators all take a list argument. This is syntactic sugar
for a chained sequence of operators. Temporal binary operators cannot accept
a list because it doesn't make sense for our use case (remember that binary
temporal operators are right associative):

Imagine that we want to verify your program produces one of these trace:
```
1. p -- program has property p
2. q -- etc
3. r

1. p q
2. r

1. p q r
```
We want to verify that "p holds, then q holds, then after q holds, r holds" so
you write `Until(p, q, r)` which is the same as `p U (q U r)` in infix notation.

```
1. p | true U (q U r) -- q U r must hold when q does not
2. q | false U (q U r) -- q U r must hold from here on
     | false U (true U r) -- r must hold when q does not
3. r | false U (false U r) -- r must hold from here on
	 | false U (false U true) -- woohoo
```
So, what's the problem? Well, imagine that after running your program it
produces this trace:
```
1. p
2. z
3. r
```
Then, working through the verification:
```
1. p | true U (q U r) -- q U r must hold when q does not
2. z | false U (q U r) -- q U r must hold from here on
     | false U (false U r) -- r must hold from here on
3. r | false U (false U true) -- woohoo - wait a minute
```
`Until(p, q, r)` is untuitive: it is stating that you may, but not are not
obliged, to see `q` between `p` and `r`.

The correct model to use here is:
```
p /\ (p U (q /\ (q U r))) == And(p, Until(p, And(q, Until(q, r))))
```

[notes] come up with an abstraction for this pattern.

Order(p, q) == And(p, Until(p, q))

[todo] everything from here onwards needs to be reworked
### Examples
[todo] Redo examples

### LTD Suggestions

Renaming operators or patterns of operators may be useful. Subject to future
changes, I like these substitutions (remember that binary operator functions
take a list of operands):
```
Until    -> Consecutively
Future   -> Eventually (This is the formal name anyway)
And      -> All
Or       -> Any
```

Then instead of:
```
DexVerify(
  Future(
    Until(
      ExpectState({stack: [f, *], vars: [s.a[0], s.a[1], s.a[2], <etc>], values: [0, 1, 2, <etc>], lines: [17]}),
      ExpectState({stack: [main, *], vars: [s.a[0], s.a[1], s.a[2], <etc>], values: [0, 1, 2, <etc>], lines: [27]}),
      Future(ExpectState({stack: [b, *], vars: [x], values: [42], lines: [40]}))
    )
  )
)
```
we could write:
```
DexVerify(
  Eventually(
    Consecutively(
      ExpectState({stack: [f, *], vars: [s.a[0], s.a[1], s.a[2], <etc>], values: [0, 1, 2, <etc>], lines: [17]}),
      ExpectState({stack: [main, *], vars: [s.a[0], s.a[1], s.a[2], <etc>], values: [0, 1, 2, <etc>], lines: [27]}),
      Eventually(ExpectState({stack: [b, *], vars: [x], values: [42], lines: [40]}))
    )
  )
)
```
We can have syntactic sugar too. If we say that a list of propositions that are
**Eventually** true, **Consecutively**, are listed **Sequentially** then we can
change the following example (which I've updated with the syntax proposed above)
from this:
```
DexVerify(
  Consecutively(
    Eventually(ExpectState({lines: [7], vars:[c], values:[1]})),
    Eventually(ExpectState({lines: [7], vars:[c], values:[2]})),
    Eventually(ExpectState({lines: [7], vars:[c], values:[3]})),
    Eventually(ExpectState({lines: [7], vars:[c], values:[4]})),
    Eventually(ExpectState({lines: [7], vars:[c], values:[5]}))
  )
)
```
to this:
```
DexVerify(
  Sequentially(
    ExpectState({lines: [7], vars:[c], values:[1]}),
    ExpectState({lines: [7], vars:[c], values:[2]}),
    ExpectState({lines: [7], vars:[c], values:[3]}),
    ExpectState({lines: [7], vars:[c], values:[4]}),
    ExpectState({lines: [7], vars:[c], values:[5]})
  )
)
```
### @@ TODO/notes
1. The Expect syntax will not look anything like this.
2. Makes sense for the first step to be stepping into main -- discuss with team.
3. Create this examples directory
4. maybe just reference the example and don't show it all here
5. note - may remove Next operator from dexter
