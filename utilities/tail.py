#!/usr/bin/env python
'''
Return the first lines of a file

Created on Jun 15, 2014

@author: Robb
'''

import sys
#from itertools import islice
import argparse

DEBUG = 0
TEST = 1

# def tail(file_in, N=10):
#     '''Prints the last lines of a file'''
#     #doesn't work for stdin
#     length = sum(1 for _ in file_in)
#     file_in.seek(0)
#     sys.stdout.writelines(islice(file_in, length-N, length))

def tail_file_name(file_name, N=10):
    '''Generates the last lines of file name'''
    with open(file_name,'r') as f_in:
        return tail_file_in(f_in, N)
    
def tail_file_in(file_in, N=10):
    '''Generates the last lines of an open file'''
    out_lines = []
    for line in file_in:
        out_lines.append(line)
        if len(out_lines) > N:
            out_lines.pop(0)
            
    return (line for line in out_lines)

def tail(file1, N=10):
    '''Generates the last lines of an open file or file name'''
    if isinstance(file1, str):
        return tail_file_name(file1, N)
    else:
        return tail_file_in(file1, N)

def tail_dump(file1, N=10):
    '''Prints the last lines of an open file or file name'''
    sys.stdout.writelines(tail(file1, N))

def main():
    ''' Process command line options '''
    
    # Setup argument parser
    parser = argparse.ArgumentParser(description='Prints the last lines of a file')
    parser.add_argument('FILE', nargs='?', help='The file to print lines from', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('-n','--lines',help='The number of lines to print',default=10,type=int)
    
    # Process arguments
    args = parser.parse_args()
    
    # Unpack the arguments
    file_in = args.FILE
    N_lines = args.lines
    
    with file_in:
        tail_dump(file_in, N_lines)
     
    
if __name__ == '__main__':
    if DEBUG:
        sys.argv.append('-h')
    if TEST == 1:
        sys.argv.append('C:\Python27\README.txt')
    elif TEST == 2:
        sys.argv.append('-n 4')
        sys.argv.append('C:\Python27\README.txt')
        
    sys.exit(main())
        