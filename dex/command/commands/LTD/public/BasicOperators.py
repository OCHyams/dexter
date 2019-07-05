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

from dex.command.CommandBase import CommandBase
from dex.command.commands.LTD.internal.BinaryOperator import BinaryOperator
from dex.command.commands.LTD.internal.UnaryOperator import UnaryOperator
from dex.dextIR.DextIR import DextIR

class Not(UnaryOperator):
    def __init__(self, *args):
        super().__init__(*args)

    def eval(self):
        result = self.operand.eval()
        if result is not None:
            result = not result
        return result


    def __str__(self):
        return super().__str__()


class And(BinaryOperator):
    def __init__(self, *args):
        super().__init__(*args)

    def eval(self):
        result = self.lhs.eval()
        if result is not None:
            result = result and self.rhs.eval()
        return rhs_result

    def __str__(self):
        return super().__str__()


class Or(BinaryOperator):
    def __init__(self, *args):
        super().__init__(*args)

    def eval(self):
        result = self.lhs.eval()
        if result is not True:
            result = self.rhs.eval()
        return result

    def __str__(self):
        return super().__str__()


class Until(BinaryOperator):
    def __init__(self, *args):
        super().__init__(*args)
        result: bool = None

    def eval(self):
        # definitive result
        if self.result is not None:
            return self.result

        lhs_result = self.lhs.eval()
        # rhs must hold in the future
        if lhs_result is True:
            rhs_result = self.rhs.eval()
            # no obligation on rhs to hold now...
            if rhs_result is not False:
                # ...but if it does, that's our result.
                # NOTE: rhs_result can be None
                self.result = rhs_result
        # rhs is obligated to hold now
        elif lhs_result is False:
            self.result = self.rhs.eval()

        # Either we have a result OR rhs has returned None. If self.result is
        # None but lhs_result is not, it means that rhs is temporal which is
        # syntactically ok but is semantically rubbish -- lhs just doesn't
        # matter.
        return self.result

    def __str__(self):
        return super().__str__()