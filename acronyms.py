#!/usr/bin/python3

import re
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument('filename', nargs=1, help='file to search for acronyms') 
argparser.add_argument('-e', '--encoding', nargs=1, help='input file encoding (utf_8,latin_1,...)', default=['utf_8']) 
args = argparser.parse_args()
filename = args.filename[0]
encoding = args.encoding[0]

# Regex for potential acronyms: capital anywhere after the first letter
acrre = re.compile(r'[a-zA-Z0-9]+[A-Z][a-zA-Z0-9]*')

# Find possible acronyms
acronyms = set()
with open(filename,'r', encoding=encoding) as f:
    for line in f:
        for acr in acrre.findall(line):
            acronyms.add(acr)
# Turn into a sorted list
templist = list(acronyms)
templist.sort()
# Remove redundant plurals
acrlist = []
prev = ''
for acr in templist:
    if acr != prev+'s':
        acrlist.append(acr)
        prev = acr
# Output results
for acr in acrlist:
    print(acr)

