#!usr/bin/python

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("infile", help = "-infile -> The input fasta file")
parser.add_argument("outfile", help = "-outfile -> The output file for chromosomal region") 
parser.add_argument("gStart", help = "-genomeStart -> The starting base position for chromosomal region", type = int)
parser.add_argument("gEnd", help = "-genomeEnd -> The ending base position for chromosomal region", type = int)

args = parser.parse_args()

inputFile = open(args.infile, 'r')
outputFile = open(args.outfile, 'w')


counter = 0; genomeStart = args.gStart ; genomeEnd = args.gEnd ; lineNum = 0


outputFile.write (inputFile.readline())

for line in inputFile :
    counter += 60
    lineNum += 1
    if counter - genomeStart  >= 1 and counter - genomeStart < 60:
        outputFile.write (line)
    if counter >= genomeStart and counter <= genomeEnd :
        print genomeStart, genomeEnd
        print lineNum, counter
        outputFile.write (line)
    
    elif counter > genomeEnd : 
        break
