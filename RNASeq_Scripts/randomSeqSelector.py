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