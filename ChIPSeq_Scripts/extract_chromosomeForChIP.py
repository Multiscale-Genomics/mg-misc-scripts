#!usr/bin/python

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("infile", help = "-infile -> The input fasta file")
parser.add_argument("outfile", help = "-outfile -> The output file for chromosome") 
args = parser.parse_args()

inputFile = open(args.infile, 'r')
outputFile = open(args.outfile, 'w')

for line in inputFile:
    if line.startswith(">"):
        line2 = line.split(",")
        line2 = line2[0].split(" ")
        
        if(line2[4] == "22"):
            print line
            while True:
                line = inputFile.next()

                if (line.startswith(">")):
                    break
                    
                outputFile.write(line)
            
            
            
            

