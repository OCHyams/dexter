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
from dex.command.commands.LTD.internal.Boolean import Boolean


class BinaryOperator(CommandBase):
    #def __init__(self, lhs: CommandBase, rhs: CommandBase):
    #    self.lhs = lhs
    #    self.rhs = rhs
    #    super().__init__()

    def __init__(self, *args):
        super().__init__()
        print("args: {}".format(args))
        if len(args) != 2:
            raise TypeError('Expected exactly two args')

        # this isn't the __best__ way to do this, fix up later @@
        ## maybe just hoist up (super.__init__())
        for arg in args:
            if isinstance(arg, bool):
                arg = Boolean(arg)
            elif not isinstance(arg, CommandBase):
                raise TypeError('Unrecognised command {}'.format(arg))

        self.lhs = args[0]
        self.rhs = args[1]


    def eval(self):
        pass

    def __str__(self):
        return "({} {} {})".format(self.lhs, self.__class__.__name__, self.rhs)
