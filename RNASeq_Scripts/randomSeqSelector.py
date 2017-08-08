#!usr/bin/python

import argparse
from random import randint

parser = argparse.ArgumentParser()

parser.add_argument("inFile", help = "-inFile -> The input fastq file")
parser.add_argument("outFile", help = "-outFile -> The final output fastq file") 

args = parser.parse_args()

infile = open(args.inFile,'r')
outfile = open(args.outFile,'w')

seq = 0

while ( True ):
    line = infile.readline()
    if (line == ""):
        break
    if (line.startswith("@ER")):
        randNum = randint(1,23)
        if (randNum == 1):
            outfile.write(line)
            for i in range(3):
                outfile.write(infile.readline())