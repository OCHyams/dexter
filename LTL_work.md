# LTL-Like language for DExTer

Operator precedence:
Not (!), Next (N)  
Until (U)  
And (/\), Or (\/)  

We expose the operators as functions, so the associativity doesn't matter. But,  
if we decide to change course and use infix operators: Binary operators are left  
associative and Temporal operators are right associative.

The standard definition of LTL is as follows (modified from [this](https://www.win.tue.nl/~jschmalt/teaching/2IX20/reader_software_specification_ch_9.pdf) source):

p ::= a  |  p /\ p  |  !p  |  Xp |  p U p
where:
* a is an atomic proposition
* p represents a valid LTL formula
* X denotes the ”next” operator
* U denotes the ”until” operator
* ! denotes negation
* /\ denotes logical "and"

Usual boolean connectives can be derived:
* !(p /\ q) == p \\/ q   // (disjunciton): i.e. OR
* !p \\/ q == p --> q    // (implication): Easiest to think about this in terms  
of short circuiting bool expression

From the syntax, we define the following:
* p \\/ !p == True
* !True == False

For dexter, we define it as:
* t ::= a  |  !t  |  Xp  |  p U p
* b ::= b /\ t |  t /\ b | !b
* p ::= t | b
where 'a' is a dexter command describing state and everything else uses the same
definitions as above.

This redefinition means that we don't have to worry about using boolean
operations on program state.

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
