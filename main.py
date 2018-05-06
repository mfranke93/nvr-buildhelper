#!/usr/bin/env python

import sys
import re
import subprocess
from nvr.nvr import Nvr

class Buildhelper:
    def __init__(self):
        self.nvr = Nvr('/tmp/nvimsocket', False)
        self.nvr.attach()

        self.create_signs()

    def load_errors(self, args):
        """Load in a list of `errorformat` strings"""
        def extract_sign_args(s):
            l = s.split(':')
            return map(lambda x: x[1].strip(), filter(lambda x: (x[0] in [0,1,3]), enumerate(l)))
        self.populate_quickfix(args)
        self.populate_signs(map(extract_sign_args, args))

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

def load_output(iterable):
    b = Buildhelper()
    regex = re.compile(r"^([^:]+):(\d+):\d+: (warning|error):.*")
    qflist = []
    signlist = []
    for line in iterable:
        x = regex.fullmatch(line)
        if x:
            qflist.append(line)
            signlist.append(tuple(map(x.group, range(1,4))))

    print(qflist)
    print(signlist)

    b.populate_quickfix(qflist)
    b.populate_signs(signlist)


if __name__ == '__main__':
    a = sys.argv[1:]

    x = subprocess.run(a, stdout=subprocess.PIPE, universal_newlines=True)
    load_output(x.stdout.split('\n'))
