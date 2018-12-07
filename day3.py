quilt = dict()

dupliCount = 0

limit = 1000

testlist = [(1,3,4,4),(3,1,4,4),(5,5,2,2)] #(x,y,width,height)

inputList = []

#read in the list
def readInput():
    with open('listfile.txt', 'r') as filehandle:
        filecontents = filehandle.readlines()
        for line in filecontents:
            lineInput = line[:-1]
            x = extract_x(lineInput)
            y = extract_y(lineInput)
            width = extract_width(lineInput)
            height = extract_height(lineInput)
            inputList.append((int(x),int(y),int(width),int(height)))

#map each value
def mapping():
    for input in inputList:
        start = (limit * input[1]) + input[0]
        for y in range(input[3]):
            xstart = start + (limit * y)
            for x in range(input[2]):
                insertIntoMap( xstart + x, 'X')

def insertIntoMap( key , value ):
    global dupliCount
    if quilt.get(key) == None: #checking if it hasn't been put in before
        quilt[key] = value
    elif quilt.get(key) == 'X': #checking if it has been put in before
        quilt[key] = 'C'
        dupliCount = dupliCount + 1

def extract_x(lineInput):
    comma_loc = lineInput.find(',',0)
    at_loc = lineInput.find('@',0)
    number = lineInput[at_loc+2:comma_loc]
    return number

def extract_y(lineInput):
    comma_loc = lineInput.find(',',0)
    colon_loc = lineInput.find(':',0)
    number = lineInput[comma_loc+1:colon_loc]
    return number

def extract_width(lineInput):
    colon_loc = lineInput.find(':',0)
    cross_loc = lineInput.find('x',0)
    number = lineInput[colon_loc+2:cross_loc]
    return number

def extract_height(lineInput):
    cross_loc = lineInput.find('x',0)
    number = lineInput[cross_loc+1:]
    return number


readInput()
mapping()
print("Count: " + str(dupliCount))
