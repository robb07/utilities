#!/usr/bin/env python
'''
Return the lines of a file that match the pattern

Created on Jun 26, 2014

@author: Robb
'''

import sys
import re
from itertools import islice

import argparse


DEBUG = 0
TEST = 0

def grep_file_name(file_name, pattern, regular_expression=False, max_num=None, ignore_case=False, invert_match=False):
    '''Generates the lines of a file that match the pattern'''
    with open(file_name,'r') as f_in:
        return (line for line in list(grep_file_in(f_in, pattern, regular_expression, max_num, ignore_case, invert_match)))

def grep_file_in(file_in, pattern, regular_expression=False, max_num=None, ignore_case=False, invert_match=False):
    '''Generates the lines of a file that match the pattern'''
    flags = 0
    if ignore_case:
        flags |= re.IGNORECASE
    
    if not invert_match:
        match_filter = lambda x: x
    else:
        match_filter = lambda x: not x
        
    if regular_expression:
        lines = (line for line in file_in if match_filter(re.search(pattern, line, flags=flags) is not None))
    else:
        if not ignore_case:
            lines = (line for line in file_in if match_filter(line.find(pattern)!=-1))
        else:
            lines = (line for line in file_in if match_filter(line.lower().find(pattern.lower())!=-1))
    
    if max_num is not None:
        lines = islice(lines, max_num)
        
    return lines
        
def grep(file1, pattern, regular_expression=False, max_num=None, ignore_case=False, invert_match=False):
    '''Generates the lines of a file that match the pattern'''
    if isinstance(file1, str):
        return grep_file_name(file1, pattern, regular_expression, max_num, ignore_case, invert_match)
    else:
        return grep_file_in(file1, pattern, regular_expression, max_num, ignore_case, invert_match)

def grep_dump(file1, pattern, regular_expression=False, max_num=None, ignore_case=False, invert_match=False):
    '''Prints the lines of a file that match the pattern'''
    sys.stdout.writelines(grep(file1, pattern, regular_expression, max_num, ignore_case, invert_match))
    
def main():
    ''' Process command line options '''
    
    # Setup argument parser
    parser = argparse.ArgumentParser(description='Prints the lines of a file that match the pattern')
    parser.add_argument('PATTERN', help='The pattern to match')
    parser.add_argument('FILE', nargs='?', help='The file to match lines from', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('-P','--python-regexp', help='PATTERN is a python regular expression', action='store_true')
    parser.add_argument('-m','--max-num', help='Stop after MAX_NUM matches',type=int)
    parser.add_argument('-i','--ignore-case', help='ignore-case distinctions', action='store_true')
    parser.add_argument('-v','--invert-match', help='select non-matching lines', action='store_true')
    
    # Process arguments
    args = parser.parse_args()
    
    # Unpack the arguments
    pattern = args.PATTERN
    file_in = args.FILE
    regexp = args.python_regexp
    max_num = args.max_num
    ignore_case = args.ignore_case
    invert_match = args.invert_match
    
    with file_in:
        grep_dump(file_in, pattern, regexp, max_num, ignore_case, invert_match)
     
    
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
        