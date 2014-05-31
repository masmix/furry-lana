#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import sys

class FileStatsWriter(object):
    def __init__(self, input, output,
                input_encoding="utf8",
                output_encoding="utf8"):
        self.i = input
        self.i_enc = input_encoding
        self.o = output
        self.o_enc = output_encoding

    def process(self):
        with self.Context(self) as ctx:
            for line in ctx['in']:
               ctx['lines-got'] += 1
               self.got_line(ctx, line)
	       print "process"			
    def got_line(self, ctx, line):
        line = line.rstrip()
        ctx['out'].write(u"{0:4d}:{1:4d}:: {2}\n".format(ctx['lines-got'], len(line), line))

    class Context(dict):
        def __init__(self, writer):
            self.writer = writer

        def __enter__(self):
            w = self.writer
            self.update({
            'in': codecs.open(w.i, "r", encoding=w.i_enc),
            'out': codecs.open(w.o, "w", encoding=w.o_enc),
            'lines-got': 0,
            })
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            try:
                self['in'].close()
            except (IOError, OSError):
                pass

            try:
                self['out'].close()
            except (IOError, OSError):
                pass

if __name__ == '__main__':
    fsw = FileStatsWriter(sys.argv[1], sys.argv[2])
    fsw.process()
