def create_triangle(filename):
    f = open(filename, 'r')
    triangle = []
    triangle2 = []
    number = ""


    for line in f:
        line = line.strip("\n")
        for character in line:
            if character != " ":
                number = number + str(character)
            else:
                triangle2.append(int(number))
                number = ""
        triangle2.append(int(number))
        number = ""
        triangle.append(triangle2)
        triangle2 = []

    return(triangle)

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

#Verified up to this point

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

triangle = create_triangle("triangle.txt")
print("Constructed triangle:")
print(triangle)

