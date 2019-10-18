class sumFunction:
    def __init__(self,cls):
        self.tempResult = []
        self.result = []
        self.seriesList = []
        for i in range(1,seriesNumber+1):
            self.seriesList.append(i)

        cls.algorithm(self,cls)

    def algorithm(self,cls):
        cls.nextstep(self)
        cls.step3(self,cls)
        print("#####",len(self.result),"#####")
        print(self.result)
            
    def nextstep(self):
        if seriesNumber%2 == 0:
            for i in range(1,int(seriesNumber/2)):
                temp1 = []
                temp2 = []
                temp1.append(self.seriesList[i])
                temp2.append(self.seriesList[-i-1])
                self.tempResult.append((temp1,temp2))
        else:
            for i in range(1,int((seriesNumber+1)/2)):    
                temp1 = []
                temp2 = []
                temp1.append(self.seriesList[i])
                temp2.append(self.seriesList[-i-1])
                if temp1 == temp2:
                    self.tempResult.append(temp1)
                else:
                    self.tempResult.append((temp1,temp2))  
        
        self.result += self.tempResult

    def step3(self,cls):     
        testList = []
        for val in self.tempResult:
            if isinstance(val,tuple):
                for j in range(2,seriesNumber-val[0][-1]):
                    self.temp = []
                    temp1 = val[0]+[val[0][-1]+j]
                    temp2 = [val[1][0]-j] + val[1]
                    if temp1 == temp2:
                        self.temp.append(temp1)
                        if len(temp1) >= (seriesNumber-2)/2:
                            self.result += self.temp
                            return False
                        else:                            
                            self.result += self.temp
                            self.tempResult += self.temp
                            break
                    else:
                        if len(temp1) > (seriesNumber-2)/2:
                            return False
                        elif temp1 in testList:                           
                            break
                        self.temp.append((temp1,temp2))
                        testList.append(temp2)
                        self.result += self.temp
                        self.tempResult += self.temp

                        
for seriesNumber in range(1,13):
    sumFunction(sumFunction)
