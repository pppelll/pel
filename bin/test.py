#!/usr/bin/env python3

import sys
import os
import re
import argparse
import pprint
import logging as log


sys.path.append(os.environ["HOME"] + '/git/pel/lib/')
import L3

######################################################################
# functions

######################################################################
# argparse - https://docs.python.org/3/library/argparse.html

prog   = os.path.basename(__file__)
desc   = 'A "main" template for Python.'
epilog = f'''
Examples:

{prog} -h
{prog} --ifn fn > out.tsv
'''

parser = argparse.ArgumentParser(description=desc, epilog=epilog,
                                 formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('-D', '--dates', metavar='STR', type=str, default='',
                    help='specify date range (from,to): YYYYMMDD,YYYYMMDD')
parser.add_argument('-a', '--action', metavar='STR', type=str, default='',
                    help='action to run')
parser.add_argument('-f', '--file', type=str, default=None, help='input file')
parser.add_argument(      '--ofmt', type=str, default=None,
                    help='output format')
parser.add_argument('--lfmrc', metavar='FN', type=str,
                    default=f'{os.environ["HOME"]}/.lfmrc',
                    help='specify non-default .lfmrc file')
parser.add_argument('-v', '--verbose', action='count')

# required argument
# parser.add_argument('integers', metavar='ints', type=int, nargs='+',
#                     help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
parser.add_argument('argv', nargs=argparse.REMAINDER)

######################################################################
# main

# quick and dirty way to turn a library into a runnable test harness
# if __name__ == "__main__":
#     ... rest of main here
b = '             pel olson                        '
print('<' + L3.lrtrim(b) + '>')
