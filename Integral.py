# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Get started with interactive Python!
# Supports Python Modules: builtins, math,pandas, scipy 
# matplotlib.pyplot, numpy, operator, processing, pygal, random, 
# re, string, time, turtle, urllib.request
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp
import re
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import numpy as np
from scipy.spatial.distance import directed_hausdorff

            
def euclidean(dimension, A, B):
  storeMetric = 0
  for j in range(dimension):
    storeMetric += ( A[0][j] - B[0][j] ) ** 2
    storeMetric = np.sqrt(storeMetric)
    print("euclidean distance between a and b: " + str(storeMetric) + "\n")
    return storeMetric
            
    ##hausdorff
def Hausdorff(A,B):
  hausdorff = max(directed_hausdorff(A,B)[0], directed_hausdorff(B,A)[0])
  print("hausdorff distance between A and B" + str(hausdorff) + '\n')



betaList = [] 


def integral(x,p):
    return (abs(x[0] - x[1]) ** p)


## Infimum
def findInf(x, dimension, A, B):
    infimumA = np.Infinity
    infimumB = np.Infinity
    for i in range(len(A)):
        storeA = 0
        #euclidean metric
    for j in range(dimension):
        storeA +=(x[j] - A[i][j]) ** 2
        print(min(storeA))
        storeA = np.sqrt(storeA)
        print(min(storeA))
        #lowest as infumum
        if(min(storeA) < infimumA):
            infimumA = min(storeA)
    for i in range(len(B)):
         storeB = 0
            #the same for B
    for j in range(dimension):
        storeB +=(x[j] - B[i][j]) ** 2
        storeB = np.sqrt(storeB)
                #lowest as infumum
        if(min(storeB) < infimumB):
            infimumB = min(storeB)
            # return d_A(x) and d_B(x)
            return(infimumA, infimumB)


def integrate(p, dimension, numPoints, X, volume, A, B, confidence):
    #initialize zero vector
    x=[0 for i in range(dimension)]
    integralVal = 0.0
    integralSquared = 0.0
    #loop over all points
    for i in range(numPoints):
        #generate  vector with values between 0 and 1
        for j in range(dimension):
            x[j] = np.random.uniform(low = X[0], high = X[1])
            #return the value of integral metric
            funcval = integral(findInf(x, dimension, A,B), p)
            print(funcval)
            # sum of each function that can be used for approximate the integral
            integralVal += funcval
            integralSquared +=funcval ** 2
          
    #print
    integralAverage = integralVal/numPoints
    integralSquaredAverage = integralSquared/numPoints
    solvedIntegral = volume * integralAverage
    
    #euclidean metric
    euclideanMetric = euclidean(dimension, A,B)
    beta = (solvedIntegral ** (1/p)) / euclideanMetric
    #hausdorff
    # hausdorff_distance = Hausdorff(A,B)
    # beta = (solvedIntegral ** (1/p)) / hausdorff_distance
    betaList.append(beta)
    
    print(betaList)
    print(solvedIntegral)        
    print("Solved", (solvedIntegral ** (1/p)))
    print("integral metric between A and B:" + str(solvedIntegral **( 1/p)) + '\n\n')
            
    # standart error
    print("standart error :")
    stderror = volume * np.sqrt(integralSquaredAverage - (integralAverage ** p) / numPoints)
    print("STD", stderror)
            
    
X = [[2,3],[3,7]] 
A = [[9,15,62], [65, 6, 67]]
B = [[1,2], [6,25]]
volume = 1000
numPoints = 100            
            
integrate(2,2, numPoints, X, volume, A,B, 0.9)

