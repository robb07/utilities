#!/usr/bin/env python
'''
Number the lines in a file

Created on Jun 18, 2014

@author: Robb
'''

import sys

from argparse import ArgumentParser

DEBUG = 0
TEST = 1

def nl(path):
    '''Numbers the lines in the file'''
    with open(path,'r') as f_in:
        sys.stdout.writelines((str(i)+'\t'+line for i, line in enumerate(f_in)))
        
    
            
def main():
    ''' Process command line options '''
    
    # Setup argument parser
    parser = ArgumentParser(description='Counts the lines in the file')
    parser.add_argument('FILE',help='The file to count from')
    
    
    # Process arguments
    args = parser.parse_args()
    
    # Unpack the arguments
    file1 = args.FILE
    
    
    nl(file1)
    
if __name__ == '__main__':
    if DEBUG:
        sys.argv.append('-h')
    if TEST == 1:
        sys.argv.append('C:\Python27\README.txt')
        
    
    
    
    sys.exit(main())
    