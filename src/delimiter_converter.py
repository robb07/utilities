#!/usr/bin/env python
'''

delimiter_converter -- Converts file from one delimiter to another
Created on Jun 10, 2014

@author: Robb
'''

import csv
import sys
import os

from argparse import ArgumentParser

DEBUG = 0
TEST = 0

def delim_to_csv(file_in, file_out, in_delim='\t', out_delim=',', num_out=None):
    '''Splits on the input delimiter and joins with commas'''
    with open(file_in, 'rb') as f_in:
        with open(file_out, 'wb') as f_out:
            writer = csv.writer(f_out)
            for i, line in enumerate(f_in):
                writer.writerow(line.strip().split(in_delim))
                if num_out is not None and i+1==num_out:
                    break

def csv_to_delim(file_in, file_out, in_delim=',', out_delim='\t', num_out=None):
    '''Splits on commas and joins with the output delimiter'''
    with open(file_in, 'rb') as f_in:
        reader = csv.reader(f_in)
        with open(file_out, 'wb') as f_out:            
            for i, line in enumerate(reader):
                f_out.write(out_delim.join(line) + os.linesep)
                if num_out is not None and i+1==num_out:
                    break

def delim_to_delim(file_in, file_out, in_delim='\t', out_delim='\t', num_out=None):
    '''Splits on the input delimiter and joins with the output delimiter'''
    with open(file_in, 'rb') as f_in:
        with open(file_out, 'wb') as f_out:
            for i, line in enumerate(f_in):
                f_out.write(out_delim.join(line.strip().split(in_delim)) + os.linesep)
                if num_out is not None and i+1==num_out:
                    break
                
def main():
    ''' Command line options '''
    
    # Setup argument parser
    parser = ArgumentParser(description='Converts a file from one delimiter character to another')
    parser.add_argument("-i", "--in_delim", help="The input delimiter, default is \\t", default='\t')
    parser.add_argument("-o", "--out_delim", help="The output delimiter, default is \\t", default='\t')
    parser.add_argument("-n", help="The number of lines to output", type=int)
    parser.add_argument("file_in", help="The file to convert")#,nargs='?')
    parser.add_argument("file_out", help="The converted file")#,nargs='?')
     
    # Process arguments
    args = parser.parse_args()
     
    # Unpack args
    in_delim = args.in_delim
    out_delim = args.out_delim
    num_out = args.n
    file_in = args.file_in
    file_out = args.file_out
    
    # Switch to correct converter
    if in_delim == ',':
        csv_to_delim(file_in, file_out, in_delim, out_delim, num_out)
    elif out_delim == ',':
        delim_to_csv(file_in, file_out, in_delim, out_delim, num_out)
    else:
        delim_to_delim(file_in, file_out, in_delim, out_delim, num_out)
    
    return 0


if __name__ == '__main__':
    if DEBUG:
        sys.argv.append("-h")
    if TEST == 1:
        sys.argv.append('-o,')
        sys.argv.append('-n 1')
        sys.argv.append('../resources/sample_tab_data.txt')
        sys.argv.append('../resources/sample_tab_data_out2.csv')
    elif TEST == 2:
        sys.argv.append('-i,')
        sys.argv.append('../resources/sample_comma_data.csv')
        sys.argv.append('../resources/sample_comma_data_out2.txt')
    elif TEST == 3:
        sys.argv.append('-o:')
        sys.argv.append('../resources/sample_tab_data.txt')
        sys.argv.append('../resources/sample_tab_data_out_colon2.txt')
    elif TEST == 4:
        sys.argv.append('-i,')
    
    
    sys.exit(main())