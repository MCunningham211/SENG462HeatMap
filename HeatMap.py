import matplotlib.pyplot as plt
import numpy as np
import math
from operator import itemgetter

KNN = 6

def eucSqrDist(x1,y1,x2,y2):
    return (((x1 - x2)**2) + ((y1 - y2)**2))#math.sqrt

def calculateColor(x,y,points):#Points should be of the form [x,y,value]
    distances = [0] * len(points) #Create an array to store distances to points
    
    for i in range(0,len(points)): #Calculate the the distance between the point and all other points
        distances[i] = eucSqrDist(x,y,points[i][0],points[i][1])
        if distances[i] < 0.01:
            print("Zero Exit:" + " " + str(x) + "," + str(y) + " " + str(points[i][0]) + "," + str(points[i][1]) + " " + str(distances[i]))
            return points[i][2]
    

    for i in range(0,len(points)):
        if(len(points[i]) < 4):
            points[i].append(distances[i])
        else:
            points[i][3] = distances[i]
    points = sorted(points, key=itemgetter(3))
    #print(points)
          
    distanceSquaredSum = 0  #Calculate the squared distance to each point
    for i in range(0,len(points)):
        if(i >= KNN):
            break
        distanceSquaredSum = distanceSquaredSum + points[i][3]
    
    for i in range(0,len(points)):
        if(i >= KNN):
            break
        points[i][3] = distanceSquaredSum/points[i][3]
    
    normalizationSum = 0
    for i in range(0,len(points)):
        if(i >= KNN):
            break
        normalizationSum = normalizationSum + points[i][3]
    for i in range(0,len(points)):
        if(i >= KNN):
            break
        points[i][3] = points[i][3]/normalizationSum
        
    temperature = 0
    for i in range(0,len(points)):
        if(i >= KNN):
            break
        temperature = temperature + points[i][2]*points[i][3]
    return temperature
    
    
    
a = np.zeros((100, 100))
inputPoints = [[13,88,.97],[10,40,1],[10,41,0],[35,29,.42],[5,2,.84],[38,77,.16],[6,62,.17],[7,37,.90],[19,95,.23],[12,28,.94],[54,53,.18],[49,25,.26],[59,77,.07],[38,0,.37],[52,89,.20],[44,54,.99],[12,69,.54],[71,55,.31],[80,56,0.01],[98,8,0.02]]
#[60,130,0.9],[20,114,0.9],[90,120,0.9],[50,180,.8],
for x in range(0,len(a)):
    for y in range(0,len(a[0])):
        a[x][y] = calculateColor(x,y,inputPoints)

plt.imshow(a, cmap='hot', interpolation='nearest')
print(a)
plt.show() 

im = plt.imread('image.jp2')
plt.imshow(im)

plt.imshow(a, cmap='hot', interpolation='nearest', alpha =.3)

print(a)
plt.show() 
        
    
    