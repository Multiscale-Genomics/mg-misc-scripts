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
        
               
    
    


