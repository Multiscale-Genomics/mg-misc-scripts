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

parser.add_argument("infile", help = "-infile -> The input fasta file")
parser.add_argument("outfile", help = "-outfile -> The output file for chromosome") 

args = parser.parse_args()

inputFile = open(args.infile, 'r')
outputFile = open(args.outfile, 'w')

for line in inputFile:
    if line.startswith(">"):        
        if("22" in line):
            print line
            outputFile.write(line)
            while True:
                line=inputFile.next()
                if (line.startswith(">")):
                    break
                    
                outputFile.write(line)

inputFile.close()
outputFile.close()
