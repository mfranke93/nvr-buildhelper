#!/usr/bin/env python

from nvr.nvr import Nvr

class Buildhelper:
    def __init__(self):
        self.nvr = Nvr('/tmp/nvimsocket', False)
        self.nvr.attach()

        self.create_signs()

    def populate_quickfix(self, args):
        """Let args be a list of File:Line:Col: Msg strings."""
        self.nvr.server.command("call setqflist([])")
        for arg in args:
            self.nvr.server.command("caddexpr '{}'".format(
                arg.rstrip().replace("'", "''").replace("|", "\\")))

    def create_signs(self):
        """Signs 'error', 'warning'"""
        self.nvr.server.command("sign define warning text=>> texthl=Blue")
        self.nvr.server.command("sign define error text=>> texthl=Red")

    def populate_signs(self, args):
        self.nvr.server.command("sign unplace 2334")
        id=2334
        for filename, line, errortype in args:
            self.nvr.server.command("sign place 2334 line={} name={} file={}".format(
                line, errortype, filename))

if __name__ == '__main__':
    b = Buildhelper()
    errargs = [
        "/home/max/prog/nvr-buildhelper/main.py:19:5: warning: def in class",
        "/home/max/prog/nvr-buildhelper/main.py:25:42: error: nvim command suspect",
        "/home/max/prog/nvr-buildhelper/test:3:1: error: unexpected token: 'error'"
            ]
    signargs = [
        ( "/home/max/prog/nvr-buildhelper/main.py", 19, "warning"),
        ( "/home/max/prog/nvr-buildhelper/main.py", 25, "error"),
        ( "/home/max/prog/nvr-buildhelper/test", 3, "error")
            ]

    b.populate_quickfix(errargs)
    b.populate_signs(signargs)
