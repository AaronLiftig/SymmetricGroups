from distributionSequence import sumFunction

#Your code starts here:
def peaks(w):
    P=[]
    for i in range(1,len(w)-1):
        if w[i]>w[i-1] and w[i+1]<w[i]:
            P.append(i+1)
    return P

def peak_set(S,n):
    W = Permutations(n)
    A =[]
    for w in W:
        if peaks(w)==S:
            A.append(w)
    return A

def maxlength(P):
    L=[]
    for p in P:
        L.append(p.length())
    return max(L)
#Your code primarily ends here. However, the code between the ###### below is also from your code.


for seriesNumber in range(1,11):
    S_list = sumFunction(sumFunction,seriesNumber)

    distribList=[] #List of unique distributions of peaks for Sn

    for S in S_list.finalResult:
        temp=[]
        
        #####
        
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
            temp.append(len(TL[i])) #Creates distribution elements for distribList
        
        #####
        
        distribList.append(temp)

    for i in range(len(distribList)): #Appends extra 0's to end because your code excuded them
        for j in distribList[i]:
            if j == 0:
                distribList[i].append(0)
            else:
                break
    
    distribList.sort(key=lambda x:x[int(len(x)/2)]) #Sorts distubList by middle value to speed up summing process

    counter=0
    sumList=[]
    
    for iter1 in range(len(distribList)): #This is the slow part, I think.
        for iter2 in range(iter1,len(distribList)):
            temp=[]
            for i in range(len(distribList[0])):
                if distribList[iter1][int(len(distribList[0])/2)]+distribList[iter2][int(len(distribList[0])/2)] > distribList[-1][int(len(distribList[0])/2)]:
                #Attempts to speed up process by comparing sum to largest value in the list (i.e. the last element). If the sum is too large, it moves on.
                    temp=[]
                    break
                else:    
                    temp.append(distribList[iter1][i]+distribList[iter2][i])
            if temp:
                sumList.append(temp)
            else:
                break
           
    inList=[]
    
    for val in sumList: #Checks to see if any list in inList is also in distribList
        if val in distribList:
            counter += 1
            inList.append(val)
    print(inList)
    print(counter) 


# sequence output: 0, 0, 0, 0, 1, 1, 3, 5, 10, 19 ...
