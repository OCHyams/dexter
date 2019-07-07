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
from dex.command.commands.LTD.internal.OperatorTypes import (
    BinaryOperator, UnaryOperator
)

class Not(UnaryOperator):
    def __init__(self, *args):
        super().__init__(*args)

    def eval(self, program: DextStepIter):
        result =  not self.operand.eval(program.shallow_copy())
        print("Not -- {}".format(result))
        return result

    def __str__(self):
        return super().__str__()


class And(BinaryOperator):
    def __init__(self, *args):
        super().__init__(*args)

    def eval(self, program: DextStepIter):
        return (self.lhs.eval(program.shallow_copy())
                and self.rhs.eval(program.shallow_copy()))

    def __str__(self):
        return super().__str__()


class Or(BinaryOperator):
    def __init__(self, *args):
        super().__init__(*args)

    def eval(self, program: DextStepIter):
        return (self.lhs.eval(program.shallow_copy())
                or self.rhs.eval(program.shallow_copy()))

    def __str__(self):
        return super().__str__()


class Until(BinaryOperator):
    def __init__(self, *args):
        super().__init__(*args)
        self.result: bool = None

## @@ consider renaming to reduce confusion with CommandBase
    def eval(self, program: DextStepIter):
        for step in program:
            result = self.rhs.eval(program.shallow_copy())
            if result is False:
                result = self.lhs.eval(program.shallow_copy())
                print("Until -- {}".format(result))
                return result
            else:
                print("Until -- True")
                return True

    def __str__(self):
        return super().__str__()
