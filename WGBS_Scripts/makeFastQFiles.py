#!usr/bin/python

"""
.. See the NOTICE file distributed with this work for additional information
   regarding copyright ownership.
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import argparse

parser = argparse.ArgumentParser()

def extractFastqHeads (infile, pathToOutFile):
    

    infile = open(infile,'r')
    outfile = open(pathToOutFile+"headsFromHumanRNAFastq.txt",'w')
#    print outfile
          
    for line in infile:
        if line.startswith("SR"):
            #continue
            lineHeads = line.split("\t")
            outfile.write(lineHeads[0]+"\n")
    
    infile.close()
    outfile.close()
    
    
    
def extractFaqtQEntries (fastqFile, pathToOutfile, fastqOutName):
    fastqFile = open(fastqFile,'r')
    tagsFile = open(pathToOutfile+"headsFromHumanRNAFastq.txt")
    outFile = open(pathToOutfile+fastqOutName,"w")

    catedHeads={}

    for line in tagsFile:
        line = line.strip()
        catedHeads[line] = None

    tagsFile.close()    
     
    for line in fastqFile:
        if line.startswith("@"):
            lineHeads = line.split(" ")
            """Uncomment while running for sam file """
            lineHeads[0]=lineHeads[0][1:]  
            if catedHeads.has_key(lineHeads[0]):
                outFile.write(line)
                for i in range(3):
                    line2 = fastqFile.next()
                    outFile.write(line2)


    fastqFile.close()
    outFile.close()
    

parser.add_argument("--samfile", help = "-samfile -> The processed sam file")
parser.add_argument("--fastQfile", help = "-fastQfile -> The original fastq file") 
parser.add_argument("--pathToOutput", help = "-pathToOutputFile -> Path for saving the output fastq file")
parser.add_argument("--fastqOut", help = "-fastqOut -> name of output Fastq file")

args = parser.parse_args()

print args.pathToOutput

extractFastqHeads (args.samfile, args.pathToOutput)
extractFaqtQEntries (args.fastQfile, args.pathToOutput, args.fastqOut)





