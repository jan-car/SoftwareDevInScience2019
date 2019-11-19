# -*- coding: utf-8 -*-
#
# collatz.py
#
# This file is part of printNumbers.
#
# Copyright (C) 2017 G. Trensch, SLNS, JSC, FZ Jülich
#
# printNumbers is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# printNumbers is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with printNumbers.  If not, see <http://www.gnu.org/licenses/>.


def CollatzSequence(n):
    '''
    :param n:   Operand
    :return:    fib(n) as list of fibonacci numbers, [0, 1, 1, 2, ... ]
    '''
    sequence = [int(n)]
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        sequence.append(int(n))

    return sequence