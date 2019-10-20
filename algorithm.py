class sumFunction:
    def __init__(self,cls,seriesNumber):
        self.currResult = []
        self.finalResult = []
        self.seriesList = []

        for i in range(1,seriesNumber+1):
            self.seriesList.append(i)

        cls.algorithm(self,cls,seriesNumber)

    def algorithm(self,cls,seriesNumber):
        cls.FirstVals(self,seriesNumber)
        cls.RemainVals(self,cls,seriesNumber)
        print(len(self.finalResult))
        print(self.finalResult)
            
    def FirstVals(self,seriesNumber):
        if seriesNumber%2 == 0:
            for i in range(1,int(seriesNumber/2)):
                tempList1 = []
                tempList2 = []
                tempList1.append(self.seriesList[i])
                tempList2.append(self.seriesList[-i-1])
                self.currResult.append((tempList1,tempList2))
        else:
            for i in range(1,int((seriesNumber+1)/2)):    
                tempList1 = []
                tempList2 = []
                tempList1.append(self.seriesList[i])
                tempList2.append(self.seriesList[-i-1])
                if tempList1 == tempList2:
                    self.currResult.append(tempList1)
                else:
                    self.currResult.append((tempList1,tempList2))  
        
        self.finalResult += self.currResult

    def RemainVals(self,cls,seriesNumber):     
        usedList = []
        for val in self.currResult:
            if isinstance(val,tuple):
                for j in range(2,seriesNumber-val[0][-1]):
                    tempList = []
                    tempVal1 = val[0]+[val[0][-1]+j]
                    tempVal2 = [val[1][0]-j] + val[1]
                    if tempVal1 == tempVal2:
                        tempList.append(tempVal1)
                        if len(tempVal1) >= (seriesNumber-2)/2:
                            self.finalResult += tempList
                            return False
                        else:                            
                            self.finalResult += tempList
                            self.currResult += tempList
                            break
                    else:
                        if len(tempVal1) > (seriesNumber-2)/2:
                            return False
                        elif tempVal1 in usedList:                           
                            break
                        tempList.append((tempVal1,tempVal2))
                        usedList.append(tempVal2)
                        self.finalResult += tempList
                        self.currResult += tempList

for seriesNumber in range(1,11):
    S_list = sumFunction(sumFunction,seriesNumber)

    sumList=[]

    for S in S_list.finalResult:
        temp=[]
        if isinstance(S,tuple):    
            P=peak_set(S[0],seriesNumber)
        else:
            P=peak_set(S,seriesNumber)

        TL=[]

        for i in range(maxlength(P)+1):
            TL.append([])

        for p in P:
            (TL[p.length()]).append(p)

        for i in range(maxlength(P)+1):
            temp.append(len(TL[i]))

        sumList.append(temp)

    for i in range(len(sumList)):
        for j in sumList[i]:
            if j == 0:
                sumList[i].append(0)
            else:
                break

    counter=0
    critList=[]

    for iter1 in range(len(sumList)):
        for iter2 in range(iter1+1,len(sumList)):
            temp=[]
            for val1,val2 in zip(sumList[iter1],sumList[iter2]):
                temp.append(val1+val2)
            critList.append(temp)

    inList=[]

    for val in critList:
        if val in sumList:
            counter += 1
            inList.append(val)

    print(counter)     
