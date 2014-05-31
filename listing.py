#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

try:
    f = open(__file__, "r") #1
    try:
        contents = f.read() #2
        print contents
    finally:
        f.close()
except (IOError, OSError):
    print >> sys.stderr, "File can not be read."
    sys.exit(1)
