#!/usr/bin/env python
'''
Return the first lines of a file

Created on Jun 15, 2014

@author: Robb
'''

import sys
from itertools import islice

from argparse import ArgumentParser

DEBUG = 0
TEST = 0

def tail(path, N=10):
    '''Prints the last lines of a file'''
    length = sum(1 for line in open(path,'rb'))
            
    with open(path, 'rb') as f_in:
        for line in islice(f_in, length-N, length):
            print line.strip() 
            
def main():
    ''' Process command line options '''
    
    # Setup argument parser
    parser = ArgumentParser(description='Prints the last lines of a file')
    parser.add_argument('FILE',help='The file to print lines from')
    parser.add_argument('-n','--lines',help='The number of lines to print',default=10,type=int)
    
    # Process arguments
    args = parser.parse_args()
    
    # Unpack the arguments
    file1 = args.FILE
    N_lines = args.lines
    
    tail(file1, N_lines) 
    
if __name__ == '__main__':
    if DEBUG:
        sys.argv.append('-h')
    if TEST == 1:
        sys.argv.append('C:\Python27\README.txt')
    elif TEST == 2:
        sys.argv.append('-n 4')
        sys.argv.append('C:\Python27\README.txt')
        
    sys.exit(main())
        