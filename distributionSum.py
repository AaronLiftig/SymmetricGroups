from distributionSequence import sumFunction

#Your code starts here:

##peaks(w)#################################################################
# input: a permutation w
# output: the peak set of w
# example: peaks([5,6,1,7,2,4,3]) =[2,4,6]
###########################################################################
def peaks(w):
    P=[]
    for i in range(1,len(w)-1):
        if w[i]>w[i-1] and w[i+1]<w[i]:
            P.append(i+1)
    return P

########################

##peak_set(S,n)############################################################
# input: an integer n and a set S in [n-1]
# output: all permutations in S_n with peak set S
# example: peak_set([2],3) = [[1, 3, 2], [2, 3, 1]]
###########################################################################
def peak_set(S,n):
    W = Permutations(n)
    A =[]
    for w in W:
        #print w
        #print peaks(w)
        if peaks(w)==S:
            A.append(w)
    return A

##maxlength(P)############################################################
# input: a set P=P(S;n)
# output: the maximum length of a permutation in P(S;n)
# example: P=P([2];4), then maxlength(P) = 9
###########################################################################
def maxlength(P):
    L=[]
    for p in P:
        L.append(p.length())
    return max(L)
                        
#Your code primarily ends here. However, the code between the ###### below is also from your code.                        


for seriesNumber in range(1,11):
    S_list = sumFunction(sumFunction,seriesNumber)

    distribList=[]

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

        distribList.append(temp)

    for i in range(len(distribList)):
        for j in distribList[i]:
            if j == 0:
                distribList[i].append(0)
            else:
                break
    
    distribList.sort(key=lambda x:x[int(len(x)/2)])
    
    counter=0
    sumList=[]
    
    for iter1 in range(len(distribList)):
        for iter2 in range(iter1+1,len(distribList)):
            temp=[]
            for i in range(len(distribList[0])):
                if distribList[iter1][int(len(distribList[0])/2)]+distribList[iter2][int(len(distribList[0])/2)] > distribList[-1][int(len(distribList[0])/2)]:
                    temp=[]
                    break
                else:    
                    temp.append(distribList[iter1][i]+distribList[iter2][i])
            if temp:
                sumList.append(temp)
            else:
                break
    
    inList=[]
    
    for val in sumList:
        if val in distribList:
            counter += 1
            inList.append(val)

    print(counter) 
    
# sequence output: 0, 0, 0, 0, 1, 1, 3, 5, 10, 19 ...
