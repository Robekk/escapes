# -*- python -*-
"""
$Id: util.py 14 2008-11-20 13:47:34Z alexios $

Copyright (C) 2008 Alexios Chouchoulas

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2, or (at your option)
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software Foundation,
Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
"""

import sys


debugEnabled = False


def debug (string):
    """
    Print out debugging information, if debugging is enabled.
    """
    if debugEnabled:
        sys.stderr.write (string + '\n')


def maybe_int (x, default=None):
    """
    Convert a string to int. Return None if the conversion fails.
    """
    try:
        return int (x)
    except (TypeError, ValueError):
        return default


def in_range (x, x0, x1):
    """
    Force `x` to be in range(x0,x1).
    """
    return min (x1 - 1, max (x0, x))


# End of file.