# DExTer : Debugging Experience Tester
# ~~~~~~   ~         ~~         ~   ~~
#
# Copyright (c) 2018 by SN Systems Ltd., Sony Interactive Entertainment Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from dex.dextIR import DextStepIter, StepIR
from dex.command.commands.LTD.internal.Proposition import AtomicProposition
from dex.command.commands.LTD.internal.OperatorTypes import (
    BinaryOperator, UnaryOperator
)


class Not(UnaryOperator):
    def __init__(self, *args):
        super().__init__(*args)

    def eval(self, program: DextStepIter):
        print("v--- Not ---v")
        result =  not self.operand.eval(program.shallow_copy())
        print("^--- Not (ret {}) ---^".format(result))
        return result

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return super().__str__()


class And(BinaryOperator):
    def __init__(self, *args):
        super().__init__(*args)

    def eval(self, program: DextStepIter):
        print("v--- And ---v")
        result = (self.lhs.eval(program.shallow_copy())
                and self.rhs.eval(program.shallow_copy()))
        print("^--- And (ret {}) ---^".format(result))
        return result


    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return super().__str__()


class Or(BinaryOperator):
    def __init__(self, *args):
        super().__init__(*args)

    def eval(self, program: DextStepIter):
        return (self.lhs.eval(program.shallow_copy())
                or self.rhs.eval(program.shallow_copy()))

    def __str__(self):
        return super().__str__()

def __repr__(self):
        return super().__str__()


class Weak(BinaryOperator):
    """ Weak(p, q) == p must hold until q and q may never hold
    """
    def __init__(self, *args):
        super().__init__(*args)

    def eval(self, program: DextStepIter):
        print("v--- {} ---v".format(self))
        while not program.at_end():
            print("v--- Weak step ---v")
            result = self.rhs.eval(program.shallow_copy())
            print("Weak rhs -- {}".format(result))
            if result is True:
                print("^--- Weak step (rhs True) ---^")
                return True
            else:
                result = self.lhs.eval(program.shallow_copy())
                print("Weak lhs -- {}".format(result))
                if result is False:
                    print("^--- Weak step (lhs False) ---^")
                    return False
            print("^--- Weak step ---^")
            program.increment()

        print("^--- Weak (ret False)---^")
        return True

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return super().__str__()


class Until(BinaryOperator):
    def __init__(self, *args):
        super().__init__(*args)

## @@ consider renaming to reduce confusion with CommandBase
    def eval(self, program: DextStepIter):
        print("v--- {} ---v".format(self))

        while not program.at_end():
            print("v--- Until step ---v")
            result = self.rhs.eval(program.shallow_copy())
            print("Until rhs -- {}".format(result))
            if result is True:
                print("^--- Until step (rhs {})---^".format(result))
                return True
            else:
                result = self.lhs.eval(program.shallow_copy())
                print("Until lhs -- {}".format(result))
                if result is False:
                    print("^--- Until step (lhs False)---^")
                    return False
            print("^--- Until step ---^")
            program.increment()

        print("^--- Until (ret False)---^")
        return False

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return super().__str__()
