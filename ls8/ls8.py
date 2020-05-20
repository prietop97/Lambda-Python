#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()
my_file = sys.argv[1]

cpu.load(my_file)
cpu.run()