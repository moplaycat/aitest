#!/usr/bin/python

import urllib2
import sys

#read data from website(uci data repository)
#target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")
#data = urllib2.urlopen(target_url)

#Read data from file(sonar.all-data.txt)
fsock = open("./sonar.all-data.txt", "r")
data = fsock.readlines()

#arrange data into list for labels and list of lists for attributes
xList = []
labels = []
for line in data:
    #split on comma
    row = line.strip().split(",")
    xList.append(row)

sys.stdout.write("Number of Rows of Data = "+str(len(xList))+'\n')
sys.stdout.write("Number od Columns of Data = "+str(len(xList[1]))+'\n')




