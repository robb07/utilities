#!/usr/bin/env python
'''
Return the first lines of a file

Created on Jun 15, 2014

@author: Robb
'''

import sys

from argparse import ArgumentParser

DEBUG = 0
TEST = 1

def head(path, N=10):
    '''Prints the first lines of a file'''
    with open(path,'rb') as f_in:
#         for line in f_in:
#             print N, line.strip()
#             N -= 1
#             if N == 0:
#                 break
        #[print( line.strip()) for i, line in enumerate(f_in) if i<N]
        #lines = [line.strip() for i, line in enumerate(f_in) if i<N]
        lines = [line.strip() for _, line in zip(range(N),f_in)]
        for line in lines:
            print line
        
            
def main():
    ''' Process command line options '''
    
    # Setup argument parser
    parser = ArgumentParser(description='Prints the first lines of a file')
    parser.add_argument('FILE',help='The file to print lines from')
    parser.add_argument('-n','--lines',help='The number of lines to print',default=10,type=int)
    
    # Process arguments
    args = parser.parse_args()
    
    # Unpack the arguments
    file1 = args.FILE
    N_lines = args.lines
    
    head(file1, N_lines) 
    
if __name__ == '__main__':
    if DEBUG:
        sys.argv.append('-h')
    if TEST == 1:
        sys.argv.append('C:\Python27\README.txt')
    elif TEST == 2:
        sys.argv.append('-n 4')
        sys.argv.append('C:\Python27\README.txt')
        
    sys.exit(main())
        