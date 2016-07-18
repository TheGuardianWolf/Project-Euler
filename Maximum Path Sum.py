#input variables

triangle = "75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"

pathSum = 0

#function to construct the triangle

def constructTriangle(numbers):
    
    triangleArray = []
    
    row = 1
    position = 0
    numberCount = 0
    currentRow = []
    buffer = ""
    
    while position < len(numbers):
        while numberCount != row:
            try:
                if numbers[position].isdigit():
                    buffer = buffer + str(numbers[position])
                else:
                    numberCount += 1
                    currentRow.append(int(buffer))
                    buffer = ""
                position += 1
            except:
                currentRow.append(int(buffer))
                break
        print("The current row is: " + str(currentRow))

        triangleArray.append(currentRow)
        row += 1
        currentRow = []
        numberCount = 0

    print("Triangle construction complete " + str(triangleArray))
    return(triangleArray)

def arraySum(subarray,start,end):

    total = 0
    
    for coordinatex in range(start,end):
        total += subarray[coordinatex]

    return(total)

def triangleSum(array,originy,originx):

    triTotal = 0
    counter = 0
    
    for coordinatey in range(originy,len(array)):
        counter += 1
        triTotal += arraySum(array[coordinatey],originx,counter+originx)

    return(triTotal)
            
def arrayConnectedPaths(array,originy,originx):
    
    pathSums = []

    originy += 1

    print("Looking at y = " + str(originy)) 

    if len(array[originy]) == 1:
       pathSums.append(triangleSum(array,originy,0))
       
    else:
        for coordinatex in range(originx,originx+2):
            print("Looking at x = " + str(coordinatex))
            pathSums.append(triangleSum(array,originy,coordinatex))

    return(pathSums)

def findMaxPath(array):

    coordinates = []
    originx = 0 #assume 1 term in topmost row
    
    for originy in range(0,len(array)-1):

        coordinates.append([originy,originx])
        
        pathSums = arrayConnectedPaths(array,originy,originx)
        
        print("Path sums are " + str(pathSums))
        
        if pathSums[0] < pathSums[1]:
            originx += 1
            print("Moving origin one across to: " + str(originx))
            
    coordinates.append([originy+1,originx]) #append final row
    
    print("We have the coordinates: " + str(coordinates))
    return(coordinates)

def addArrayCoordinates(array,coordinates):

    arraySum = 0

    for coordinate in coordinates:
        arraySum += array[coordinate[0]][coordinate[1]]

    print("Sum of coordinates in array is: " + str(arraySum))
    return(arraySum)

    
#store triangle

print("Constructing triangle...")

triangleArray = constructTriangle(triangle)

#analyse rows for path sums

print("Beginning path analysis...")

coordinates = findMaxPath(triangleArray)

print("Finding the maximum sum...")

addArrayCoordinates(triangleArray,coordinates)
