# LTL-Like language for DExTer

Operator precedence:
```
Not (`!`), Next (N)  
Until (`U`)  
And (`/\`), Or (`\/`)  
```

We expose the operators as functions, so the associativity doesn't matter. But,<br/>
if we decide to change course and use infix operators: Binary operators are left<br/>
associative and Temporal operators are right associative.

The standard definition of LTL is as follows (modified from [this](https://www.win.tue.nl/~jschmalt/teaching/2IX20/reader_software_specification_ch_9.pdf) source):

```
p ::= a  |  p /\ p  |  !p  |  Xp |  p U p
```

Where:
* `a` is an atomic proposition
* `p` represents a valid LTL formula
* `X` denotes the ”next” operator
* `U` denotes the ”until” operator
* `!` denotes negation
* `/\` denotes logical "and"


Usual boolean connectives can be derived:
```
* !(p /\ q) == p \/ q   // (disjunciton): i.e. OR
* !p \/ q == p --> q    // (implication): Easiest to think about this in
                           terms of short circuiting bool expression.
```

From the syntax, we define the following:
```
p \/ !p == True
!True == False
```

For dexter, we define it as:
```
t ::= a  |  !t  |  Xp  |  p U p
b ::= b /\ t |  t /\ b | !b
p ::= t | b
```

Where `a` is a dexter command describing state and everything else uses the<br/>
same definitions as above. This redefinition means that we don't have to worry<br/>
about performing boolean operations on program state. This makes it easier to<br/>
understand test failures but does make the "language" more difficult to write<br/>
and and less expressive.

This gives us the following command hierarchy where 'public' commands are
prefixed with 'Dex':
```
Proposition
  Temporal(Proposition)
    Command(Temporal)
      DexCommandXX(Command)
        args: list
      DexCommandYY(Command)
        args: list
    TemporalNot(Temporal)
      operand: Temporal
    DexNext(Temporal)
      operand: Proposition
    DexUntil(Temporial)
      lhs: Proposition
      rhs: Proposition

  Boolean(Proposition)
    __BooleanBinaryLeft(Boolean)
      lhs: Boolean
      rhs: Temporal
    __BooleanBinaryRight(Boolean)
      lhs: Temporal
      rhs: Boolean
    BooleanBinary(Boolean)
      union
        __BooleanBinaryLeft,
        __BooleanBinaryRight
    DexNot(Boolean)
      operand: Boolean
```

[note] Still unsure on the whole "no composition" thing. If we say "DexState" __is__
aggregation, then * wildcard operator is __kind__of__ like an "OR anything". But this feels
flimsy. Can't AND literally translate to "all of these things must be true, independantly"
without any aggregation/merging? Then we can even give good diagnostics at run-time
"this expression can never be true, use "False()"...?

[note] This doesn't actually work, e.g.
```
F(x) == true U x
(p U q) /\ F(x) -types-> (t U t)[t] /\ t == t /\ t, apparently invalid.

...and adding t /\ t to the b ::= def means you can have a /\ a, which is
invalid.
```


[note] JM says ditching next is completely fine.


[wip] Trying out another definition...
```
need to allow this:
(p U q) /\ Xp -- having "binary expr can only work on temp operands", as below,
doesn't work because

t ::=  p U p | Xp 
b ::=  a  |  !a  |  t /\ t
```

The follwing DexCommands are based on real or upcoming commands:  
(list is a list of strings)  
DexLine(vars: list, linenos: list)
DexValue(vars: list, values: list) -- variables have specified values  
DexCallStack(frames: list) -- call stack matches some pattern  
DexType(vars: list, tyeps: list) -- variables have specified type  
DexEval(expression: str) -- expression evaluates to specified value  
DexState(...) -- explicit declaration of program state (call stack, locals, globals)  

