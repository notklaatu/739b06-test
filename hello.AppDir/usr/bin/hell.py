#!/usr/bin/python2.7

import sys

sys.path.insert(0, "usr/lib/foo")

from foo import bar

bar.echotest(" --> hello")
