#!/usr/bin/env python
'''
Count the lines, words, chars and bytes of a file

Created on Jun 15, 2014

@author: Robb
'''

import sys
import argparse

DEBUG = 0
TEST = 0

def wc_file_name(file_name, lines=True, words=True, chars=True, bytes1=True):
    '''Counts the lines, words, chars, and bytes of a file'''
    with open(file_name,'r') as f_in:
        return wc_file_in(f_in,lines,words,chars,bytes1)
    
def wc_file_in(file_in, lines=True, words=True, chars=True, bytes1=True):
    '''Counts the lines, words, chars, and bytes of an opened file'''
    line_count = 0
    word_count = 0
    char_count = 0
    byte1_count = 0
    
    for line in file_in:
        if lines:
            line_count += 1
        if words:
            word_count += len(line.split())
        if chars:
            char_count += len(line)
        if bytes1:
            byte1_count += len(line)

    counts = []
    if lines:
        counts.append(str(line_count))
    if words:
        counts.append(str(word_count))
    if chars:
        counts.append(str(char_count))
    if bytes1:
        counts.append(str(byte1_count))
    
    max_len = max([len(cnt) for cnt in counts])
    
    output = ' '.join([cnt.rjust(max_len) for cnt in counts])
    path = file_in.name 
    if path != '<stdin>':
        output += '\t' + path 
    
    return output  
    
def wc(file1, lines=True, words=True, chars=True, bytes1=True):
    '''Counts the lines, words, chars, and bytes of an opened file or a file name'''
    if isinstance(file1,str):
        return wc_file_name(file1,lines,words,chars,bytes1)
    else:
        return wc_file_in(file1,lines,words,chars,bytes1)

def wc_dump(file1, lines=True, words=True, chars=True, bytes1=True):
    '''Prints the line, word, char, and byte counts of a file'''
    sys.stdout.writelines(wc(file1,lines,words,chars,bytes1) + '\n')
               
def main():
    ''' Process command line options '''
    
    # Setup argument parser
    parser = argparse.ArgumentParser(description='Counts the lines in the file')
    parser.add_argument('FILE', nargs='?', help='The file to count from', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('-b','--bytes',help='Count the bytes',action='store_true')
    parser.add_argument('-c','--chars',help='Count the chars',action='store_true')
    parser.add_argument('-l','--lines',help='Count the new lines',action='store_true')
    parser.add_argument('-w','--words',help='Count the words',action='store_true')
    
    # Process arguments
    args = parser.parse_args()
    
    # Unpack the arguments
    file_in = args.FILE
    lines = args.lines
    words = args.words
    chars = args.chars
    bytes1 = args.bytes
    
    if not any([lines, words, chars, bytes1]):
        lines, words, chars = True, True, True
    
    with file_in:
        wc_dump(file_in, lines, words, chars, bytes1)
    
    
if __name__ == '__main__':
    if DEBUG:
        sys.argv.append('-h')
    if TEST == 1:
        sys.argv.append('C:\Python27\README.txt')
        #sys.argv.append('C:\Python27\python.exe')
    elif TEST == 2:
        sys.argv.append('-l')
        sys.argv.append('C:\Python27\README.txt')
    elif TEST == 3:
        sys.argv.append('-w')
        sys.argv.append('C:\Python27\README.txt')
    elif TEST == 4:
        sys.argv.append('-c')
        sys.argv.append('C:\Python27\README.txt')
    elif TEST == 5:
        sys.argv.append('-b')
        sys.argv.append('C:\Python27\README.txt')
    
    sys.exit(main())
        