#!usr/bin/python

infile = open ("/Users/reham/Documents/Mouse_chr19.fasta",'r')
outfile = open ("bsSeeker.Mouse.GRCm38.fasta",'w')

counter = 0; genomeStart = 45649132; genomeEnd = 45651199 ; lineNum = 0
#genomeStart + 111 + 2000

outfile.write (infile.readline())

for line in infile :
    counter += 60
    lineNum += 1
    if counter - genomeStart  >= 1 and counter - genomeStart < 60:
        outfile.write (line)
    if counter >= genomeStart and counter <= genomeEnd :
        print genomeStart, genomeEnd
        print lineNum, counter
        outfile.write (line)
    
    elif counter > genomeEnd : 
        break