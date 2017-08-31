#!usr/bin/python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("infile", help = "-infile -> The input wig file")
args = parser.parse_args()

inputFile = open(args.infile)
dictList = {}

inputFile.readline()

for line in inputFile:
    parts = line.split("\t")
    pos = int(parts[0])
    dp = float(parts[1])
    dictList[pos] = dp
    
counter = 0
coverageLength = 3000
peakNum = 0
peaks = []
minPeakNum = 5
prev = 0
    
for key,value in dictList.iteritems():
    
    if value >= 0.5 :
        counter = counter +1
        peakNum = peakNum +1
        peaks.append(value)
        
    else :
        peakNum = 0
        continue
        
    if counter >= coverageLength and peakNum >= minPeakNum :
        print key-coverageLength, key  
        print peaks
        
               
    
    


