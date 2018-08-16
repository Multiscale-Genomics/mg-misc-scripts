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
parser.add_argument("infile", help = "-infile -> The input depth file")
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
