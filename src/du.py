#!/usr/bin/env python
'''
Disk Utilization -- how much disk space does a folder and its files take up

Created on Jun 14, 2014

@author: Robb
'''

import sys
import os
import re

from argparse import ArgumentParser

DEBUG = 0
TEST = 0

possible_units = ['K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y'] 

def dynamic_units(size, base=1024, suffix=''):
    '''Calculates the string as a multiplier of largest unit possible and adds the unit''' 
    exp = 1
    while size/base**exp > base and exp < len(possible_units):
        exp += 1
    return str(size/base**exp)+possible_units[exp-1]+suffix

def disp_units(size, units=None, base=1024):
    '''Calculates the string as a multiplier of the specified unit and adds the unit'''
    if units:
        prefix = units[0]
        if units.find('B') != -1:
            base = 1000
            suffix = 'B'
        else:
            suffix = ''
            
        if units == 'B':
            return str(size/base)
        elif prefix == '*':
            return dynamic_units(size, base, suffix)
        else:
            try:
                exp = possible_units.index(prefix)+1
                return str(size/base**exp) + units
            except ValueError:
                raise ValueError('Unsupported unit "' + units[0] + '" valid prefixes are *, B, ' + str(possible_units))        
    else:
        return str(size/base)

def du(path, depth=0, max_depth=None, print_files=False, units=None):
    '''Calculates the disk utilization of a file or recurses for a directory'''
    if os.path.isdir(path):
        size = sum([du(os.path.join(path,p), depth+1, max_depth, print_files, units) for p in os.listdir(path)])
        if max_depth is None or depth <= max_depth:
            print disp_units(size, units), '\t', path
    else:
        size = os.path.getsize(path)
        if print_files and (max_depth is None or depth <= max_depth):
            print disp_units(size, units), '\t', path
        
    return size

def main():
    ''' Process command line options '''
    
    # Setup argument parser
    parser = ArgumentParser(description='Summarize the disk utilization of a file, recursively for a directory')
    parser.add_argument('FILE',help='Summarize the disk utilization of each file or directory in FILE', nargs='?')
    parser.add_argument('-a','--all',help='Print size for files too',action='store_true')
    parser.add_argument('-s','--summarize',help='Only print total size for each entry in FILE',action='store_true')
    parser.add_argument('-t','--total',help='Print total combined size of entries in FILE',action='store_true')
    parser.add_argument('-d','--max-depth',help='Print disk utilization for directories no deeper than MAX_DEPTH',type=int)
    parser.add_argument('-u','--units',help='Print display utilization in specified UNITS (K, M, G, T, P, E, Z, Y are powers of 1024, KB, MB, ... are powers of 1000, * and *B are dynamic)')
    
    
    # Process arguments
    args = parser.parse_args()
    
    # Unpack the arguments
    if args.FILE:
        files = [f.strip('"') for f in re.findall(r'[^\s"]+|"[^"]*"', args.FILE)]
        # explanation of the regular expression:
        # [^\s"]+ -- matches all characters until a white space or quote (i.e. strings separated by white space or quotes)
        # |       -- or
        # "[^"]*" -- matches quote plus all characters through the next quote (i.e. only matches an object enclosed in quotes)
        # the or keeps the regular expression match going through white space enclosed in quotes
    else:
        files = [os.curdir]
    
    print_files = args.all
    summarize = args.summarize
    total = args.total
    max_depth = args.max_depth
    units = args.units
    
    if units:
        units = units.strip()
        if units[0] != '*' and units[0] != 'B':
            try:
                possible_units.index(units[0])
            except ValueError:
                raise ValueError('Unsupported unit ' + units[0] + ' valid units are *, B, ' + str(possible_units))
       
    if summarize:
        max_depth = 0
        
    sizes = [du(file1, 0, max_depth, print_files, units) for file1 in files]
    if total:
        print disp_units(sum(sizes),units), '\tTotal'
    
    return 0
    
if __name__ == '__main__':
    if DEBUG:
        sys.argv.append('-h')
    if TEST == 1:
        sys.argv.append('-a')
        #sys.argv.append('-u K')
        sys.argv.append('C:\Python27\python.exe')
    elif TEST == 2:
        sys.argv.append('C:\Python27')
    elif TEST == 3:
        sys.argv.append('-a')
        sys.argv.append('-d 2')
        sys.argv.append('-u *B')
        sys.argv.append('C:\Python27')
    elif TEST == 4:
        sys.argv.append('-s')
        sys.argv.append('-u K')
        sys.argv.append('C:\Python27')
    elif TEST == 5:
        sys.argv.append('-s')
        sys.argv.append('-t')
        sys.argv.append('-d 3')
        sys.argv.append('-u *')
        sys.argv.append('C:\Python27\lib C:\Python27\Tools    "C:\Program Files\Java"')
    
        
    sys.exit(main())

