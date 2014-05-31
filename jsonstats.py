#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys

from filestats import FileStatsWriter

class JsonStatsWriter(FileStatsWriter):
    class Context(FileStatsWriter.Context):
        def __enter__(self):
            super(JsonStatsWriter.Context, self).__enter__()
            self['json'] = []
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            enc = self.writer.o_enc
            json.dump(self['json'], self['out'],
                    ensure_ascii=False, indent=2)
            super(JsonStatsWriter.Context, self).__exit__(
            exc_type, exc_val, exc_tb)

    def got_line(self, ctx, line):
        line = line.rstrip()
        ctx['json'].append({
        u'number': ctx['lines-got'],
        u'length': len(line),
        u'line': line
        })

if __name__ == '__main__':
    jsonw = JsonStatsWriter(sys.argv[1], sys.argv[2])
    jsonw.process()
