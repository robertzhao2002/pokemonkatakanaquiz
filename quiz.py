#!/usr/bin/python

import sys

arguments = sys.argv

if len(arguments) == 2 and arguments[1] == 'get':
    import QuizBuilder
else:
    import csv
    print("hello")
