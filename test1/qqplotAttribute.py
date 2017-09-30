#!/usr/bin/python

import numpy as np
import pylab
import scipy.stats as stats
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

nrow=len(xList)
ncol=len(xList[1])

type = [0]*3
colCounts = []

#generate summary statistics for column 3 (e.g.)
col = 3
colData = []
for row in  xList:
    colData.append(float(row[col]))

stats.probplot(colData,dist="norm",plot=pylab)
pylab.show()