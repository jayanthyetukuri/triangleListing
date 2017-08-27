inputFilePath = r'C:\Users\jyy\Documents\FindingTriangles\DataSets\CA-AstroPh.txt'

import numpy
import csv
import operator
from collections import OrderedDict
triangles = set()
count = 0
totalEdges = 0
trianglesCount = 0
orderedAL = {}
injectionMap = {}
inputFile = open(inputFilePath, 'r')
for line in inputFile:                 
    count +=1
    if count > 4:
        edge = line.strip().split('\t')
        fromNode = int(edge[0])
        toNode = int(edge[1])
        if fromNode < toNode:
            if fromNode not in orderedAL:
                orderedAL[fromNode] = {}
                orderedAL[fromNode]['toNodes']=[]
                orderedAL[fromNode]['fromNodes']=[]
                orderedAL[fromNode]['toNodes'].append(toNode)
            else:
                orderedAL[fromNode]['toNodes'].append(toNode)
            if toNode not in orderedAL:
                orderedAL[toNode] = {}
                orderedAL[toNode]['toNodes']=[]
                orderedAL[toNode]['fromNodes']=[]
                orderedAL[toNode]['fromNodes'].append(fromNode)
            else:
                orderedAL[toNode]['fromNodes'].append(fromNode)

for node in orderedAL:
    if len(orderedAL[node]['toNodes']) in injectionMap:
        injectionMap[len(orderedAL[node]['toNodes'])].append(node)
    else:
        injectionMap[len(orderedAL[node]['toNodes'])] = []
        injectionMap[len(orderedAL[node]['toNodes'])].append(node)

trianglesCount = 0
for node in orderedAL:
    for fromNode in orderedAL[node]['fromNodes']:
        if node in orderedAL[fromNode]['toNodes']:
            triNodes = set(orderedAL[node]['toNodes']).intersection(set(orderedAL[fromNode]['toNodes']))
            for n in triNodes:
                trianglesCount +=1
                triangles.add(str(fromNode) + '-' + str(node) + '-' + str(n))

print 'SortedTrinanglesCount : '+ str(trianglesCount)
print 'Triangles : '+ str(len(triangles))
