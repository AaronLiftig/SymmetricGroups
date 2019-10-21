from itertools import permutations
from scipy.signal import find_peaks

def loopName(seriesNumber):
    seriesList = []
    for i in range(1,seriesNumber+1):
        seriesList.append(i)

    vals = list(permutations(seriesList))
    tempList = []

    for val in vals:
        num = find_peaks(val)[0].tolist()
        if num:
            tempList.append(([x+1 for x in num],list(val)))
    
    return tempList

def sorter(tempList):
    sortedDict = {}
    for peak in value.finalResult:
        if isinstance(peak,tuple):
            temp = []
            for i in tempList:
                if i[0] == peak[0]:
                    temp.append(i[1])
                    tempList.remove(i)
            sortedDict.update({tuple(peak[0]):temp})
        else:
            temp = []
            for i in tempList:
                if i[0] == peak:
                    temp.append(i[1])
                    tempList.remove(i)
            sortedDict.update({tuple(peak):temp})

    print(sortedDict)
    
    return sortedDict

def wordMaker(sortedDict):
    distList = {}
    
    for a,b in sortedDict.items():
        temp = []
        print('#####',a)
        for item in b:
            print(Permutation(item).reduced_word())
            temp.append(len(Permutation(item).reduced_word()))
        distList.update({a:temp.sort()})
            
    print(distList)
