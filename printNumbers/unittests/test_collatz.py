# -*- coding: utf-8 -*-
#
# test_collatz.py
#
# This file is part of PrintNumbers.
#
# Copyright (C) 2017 G. Trensch, SLNS, JSC, FZ Jülich
#
# PrintNumbers is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# PrintNumbers is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PrintNumbers.  If not, see <http://www.gnu.org/licenses/>.

#
# Unit tests: 'collatz'.
#

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest
from functions.collatz import *


class TestCollatz(unittest.TestCase):

    def test_value_1(self):
        self.assertEqual(CollatzSequence(1), [1] )

    def test_value_2(self):
        self.assertEqual(CollatzSequence(2), [2, 1])

    def test_value_4(self):
        self.assertEqual(CollatzSequence(4), [4, 2, 1])

    def test_value_5(self):
        self.assertEqual(CollatzSequence(5), [5, 16, 8, 4, 2, 1])

    def test_value_7(self):
        self.assertEqual(CollatzSequence(7),
                         [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])


def suite():
    suite = unittest.makeSuite(TestCollatz, 'test')
    return suite

def run():
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(suite())

if __name__ == "__main__":
    run()