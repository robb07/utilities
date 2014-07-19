#!/usr/bin/env python
'''
Return the first lines of a file

Created on Jun 15, 2014

@author: Robb
'''

import sys
from itertools import islice
import argparse

DEBUG = 0
TEST = 0

def head_file_name(file_name, N=10):
    '''Generator of the first lines of a file'''
    with open(file_name) as f_in:
        return (line for line in list(head_file_in(f_in, N)))

def head_file_in(file_in, N=10):
    '''Generator of the first lines of an open file'''
    return islice(file_in, N)
    
def head(file1, N=10):
    '''Generates the first lines of a file (file_name or open)'''
    if isinstance(file1,str):
        return head_file_name(file1, N)
    else:
        return head_file_in(file1, N)
        
def head_dump(file1, N=10):
    '''Prints the first lines of a file'''
    sys.stdout.writelines(head(file1,N))
            
def main():
    ''' Process command line options '''
    
    # Setup argument parser
    parser = argparse.ArgumentParser(description='Prints the first lines of a file')
    parser.add_argument('FILE', nargs='?', help='The file to print lines from', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('-n','--lines',help='The number of lines to print',default=10,type=int)
    
    # Process arguments
    args = parser.parse_args()
    
    # Unpack the arguments
    file_in = args.FILE
    N_lines = args.lines
    
    
    with file_in:
        head_dump(file_in, N_lines) 
        
if __name__ == '__main__':
    if DEBUG:
        sys.argv.append('-h')
    if TEST == 1:
        sys.argv.append('C:\Python27\README.txt')
    elif TEST == 2:
        sys.argv.append('-n 4')
        sys.argv.append('C:\Python27\README.txt')
        
    sys.exit(main())
        