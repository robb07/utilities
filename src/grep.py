#!/usr/bin/env python
'''
Return the lines of a file that match the pattern

Created on Jun 26, 2014

@author: Robb
'''

import sys
import re
from itertools import islice

from argparse import ArgumentParser

DEBUG = 0
TEST = 0

def grep(path, pattern, regular_expression=False, max_num=None, ignore_case=False, invert_match=False):
    '''Prints the lines of a file that match the pattern'''
    flags = 0
    if ignore_case:
        flags |= re.IGNORECASE
    
    with open(path,'r') as f_in:
        if regular_expression:
            lines_and_matches = ((line, re.search(pattern, line, flags=flags) is not None) for line in f_in)
        else:
            if not ignore_case:
                lines_and_matches = ((line, line.find(pattern)!=-1) for line in f_in)
            else:
                lines_and_matches = ((line, line.lower().find(pattern.lower())!=-1) for line in f_in)
            
        if not invert_match:
            lines = (line for line, matched in lines_and_matches if matched)
        else:
            lines = (line for line, matched in lines_and_matches if not matched)
            
        if max_num is not None:
            lines = islice(lines, max_num)
            
        sys.stdout.writelines(lines)
        
        
            
def main():
    ''' Process command line options '''
    
    # Setup argument parser
    parser = ArgumentParser(description='Prints the lines of a file that match the pattern')
    parser.add_argument('PATTERN', help='The pattern to match')
    parser.add_argument('FILE', help='The file to print lines from')
    parser.add_argument('-P','--python-regexp', help='PATTERN is a python regular expression', action='store_true')
    parser.add_argument('-m','--max-num', help='Stop after MAX_NUM matches',type=int)
    parser.add_argument('-i','--ignore-case', help='ignore-case distinctions', action='store_true')
    parser.add_argument('-v','--invert-match', help='select non-matching lines', action='store_true')
    
    # Process arguments
    args = parser.parse_args()
    
    # Unpack the arguments
    pattern = args.PATTERN
    path = args.FILE
    regexp = args.python_regexp
    max_num = args.max_num
    ignore_case = args.ignore_case
    invert_match = args.invert_match
        
    grep(path, pattern, regexp, max_num, ignore_case, invert_match) 
    
if __name__ == '__main__':
    if DEBUG:
        sys.argv.append('-h')
    if TEST == 1:
        sys.argv.append('python')
        sys.argv.append('C:\Python27\README.txt')
    elif TEST == 2:
        sys.argv.append('Python')
        sys.argv.append('C:\Python27\README.txt')
    elif TEST == 3:
        sys.argv.append('-i')
        sys.argv.append('python')
        sys.argv.append('C:\Python27\README.txt')
    elif TEST == 4:
        sys.argv.append('-v')
        sys.argv.append('python')
        sys.argv.append('C:\Python27\README.txt')
    elif TEST == 5:
        sys.argv.append('-i')
        sys.argv.append('-v')
        sys.argv.append('python')
        sys.argv.append('C:\Python27\README.txt')
    elif TEST == 6:
        sys.argv.append('-m 3')
        sys.argv.append('python')
        sys.argv.append('C:\Python27\README.txt')
    elif TEST == 7:
        sys.argv.append('2.6+')
        sys.argv.append('C:\Python27\README.txt')
    elif TEST == 8:
        sys.argv.append('-P')
        sys.argv.append('2.6+')
        sys.argv.append('C:\Python27\README.txt')
    elif TEST == 9:
        sys.argv.append('-P')
        sys.argv.append('install|build')
        sys.argv.append('C:\Python27\README.txt')
        
    sys.exit(main())
        