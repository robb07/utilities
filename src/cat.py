#!/usr/bin/env python
'''
Concatenates the file(s) or standard input to standard output

Created on Jun 27, 2014

@author: Robb
'''

import sys
import argparse

DEBUG = 0
TEST = 0

def cat(files_in):
    '''Prints the file'''
    for file_in in files_in:
        sys.stdout.writelines(file_in)
        
            
def main():
    ''' Process command line options '''
    
    # Setup argument parser
    parser = argparse.ArgumentParser(description='Concatenates the file(s) or standard input to standard output',
                                     epilog='With no FILE, or when FILE is -, read standard input.')
    parser.add_argument('FILE', nargs='*', help='The file(s) to concatenate to standard output', default='-')
    
    # Process arguments
    args = parser.parse_args()
    
    # Unpack the arguments
    files = args.FILE
    
    files_in = [open(path,'r') if path != '-' else sys.stdin for path in files]
    
    print files
    print files_in
    
    cat(files_in) 
    
    for file_in in files_in:
        file_in.close()
    
if __name__ == '__main__':
    if DEBUG:
        sys.argv.append('-h')
    if TEST == 1:
        sys.argv.append('C:\Python27\README.txt')
    elif TEST == 2:
        sys.argv.append('C:\Python27\README.txt')
        sys.argv.append('C:\Python27\LICENSE.txt')
    elif TEST == 3:
        sys.argv.append('C:\Python27\README.txt')
        sys.argv.append('-')
    sys.exit(main())
        