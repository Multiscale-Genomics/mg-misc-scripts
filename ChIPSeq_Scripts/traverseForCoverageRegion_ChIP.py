#!usr/bin/python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("infile", help = "-infile -> The input fasta file")
args = parser.parse_args()

inputFile = open(args.infile)

dictList = {}

for line in inputFile:
    parts = line.split("\t")
    pos1 = int(parts[1]) 
    dp = int(parts[2]) 
    dictList[pos1] = dp
    
counter = 0
coverageLength = 55
prev = 0
    
for key,value in dictList.iteritems():
    if key - prev > 1 :
        prev = key 
        counter = 0
        continue
    
    if value >= 70 :
        counter = counter +1
        
    else :
        counter = 0
        continue
        
    if counter >= coverageLength:
        print key-coverageLength, key  
               
    prev = key
