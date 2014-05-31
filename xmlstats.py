#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from xml.etree import ElementTree as ET

from filestats import FileStatsWriter

class XmlStatsWriter(FileStatsWriter):
    class Context(FileStatsWriter.Context):
        def __enter__(self):
            super(XmlStatsWriter.Context, self).__enter__()
            self['xml'] = ET.Element('stats')
            self['xml'].text = '\n'
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            enc = self.writer.o_enc
            xml = ET.tostring(self['xml'], encoding=enc)
            xml = xml.decode(enc)
            self['out'].write(xml)
            super(XmlStatsWriter.Context, self).__exit__(
            exc_type, exc_val, exc_tb)

    def got_line(self, ctx, line):
        line = line.rstrip()
        tag = ET.SubElement(ctx['xml'], 'line')
        tag.set('number', str(ctx['lines-got']))
        tag.set('length', str(len(line)))
        tag.text = line
        tag.tail = '\n'

if __name__ == '__main__':
    xmlw = XmlStatsWriter(sys.argv[1], sys.argv[2])
    xmlw.process()
