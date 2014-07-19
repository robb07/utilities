#!/usr/bin/env python
'''
Number the lines in a file

Created on Jun 18, 2014

@author: Robb
'''

import sys
import argparse

DEBUG = 0
TEST = 0

def nl_file_name(file_name):
    '''Generator of the first lines of a file'''
    with open(file_name) as f_in:
        return (line for line in list(nl_file_in(f_in)))

def nl_file_in(file_in):
    '''Generator of the first lines of an open file'''
    return (str(i)+'\t'+line for i, line in enumerate(file_in))
    
def nl(file1):
    '''Numbers the lines in the file'''
    if isinstance(file1,str):
        return nl_file_name(file1)
    else:
        return nl_file_in(file1)
        
def nl_dump(file_in):
    '''Numbers the lines in the file'''
    sys.stdout.writelines(nl(file_in))    
            
def main():
    ''' Process command line options '''
    
    # Setup argument parser
    parser = argparse.ArgumentParser(description='Counts the lines in the file')
    parser.add_argument('FILE', nargs='?', help='The file to number lines in', type=argparse.FileType('r'), default=sys.stdin)
    
    # Process arguments
    args = parser.parse_args()
    
    # Unpack the arguments
    file_in = args.FILE
    
    with file_in:
        nl_dump(file_in)
    
if __name__ == '__main__':
    if DEBUG:
        sys.argv.append('-h')
    if TEST == 1:
        sys.argv.append('C:\Python27\README.txt')
    
    sys.exit(main())
    