import re
import itertools

def count(stringList = ['']):
    numberOfRectangles = 0
    if(stringList):
        for i in range(len(stringList)-1):
            corners = [position for position, character in enumerate(stringList[i]) if character == '+']
            possibleTops = [combo for combo in itertools.combinations(corners,2)]
            confirmedTops = [(left, right) for left,right in possibleTops if re.match("\+\-*\+", stringList[i][left:right+1])]
            for left,right in confirmedTops:
                for index in range(i+1,len(stringList)):
                    if(re.match("^\+[\+\-]*\+$",stringList[index][left:right+1])):
                        numberOfRectangles += 1
                    elif(not re.match("^[\|\+].*[\|\+]$",stringList[index][left:right+1])):
                        break
    return numberOfRectangles