from itertools import permutations
import math

class peakPolynomial:
    def __init__(self,cls,S,n):
        self.S = sorted(S)
        self.n = n
        self.nSet = [x for x in range(1,self.n+1)]
        print('nSet\n[n]:',self.nSet,'\n')
        self.G_n = list(permutations(self.nSet))
        if not self.S:
            cls.getPeaks(self)
            self.peakSet = self.peaksAndPermsDict[tuple(self.S)]
        elif self.n < self.S[-1] + 1:
            print('not admissible')
            self.cardinality = 0
            return
        else:
            cls.getPeaks(self)
            self.peakSet = self.peaksAndPermsDict[tuple(self.S)]
            cls.polyFunc(self,cls,self.S,self.n)
            print(self.poly_n)
        print('peakSet\nP({};{}):\n'.format(self.S,self.n),self.peakSet,'\n')

    @staticmethod
    def nCr(n,r):
        f = math.factorial
        return f(n) / f(r) / f(n-r)

    def getPeaks(self):
        self.peaksAndPermsDict = {}
        for pi in self.G_n:
            peaks = []	
            for i in range(1,len(pi)-1):
                if (pi[i-1] < pi[i]) & (pi[i] > pi[i+1]):
                    peaks.append(i+1)
            if tuple(peaks) not in self.peaksAndPermsDict.keys():
                self.peaksAndPermsDict[tuple(peaks)] = [pi]
            else:
                self.peaksAndPermsDict[tuple(peaks)] += [pi]
                    
    def cardOfPeakSet(self):
        if self.S:
            self.cardinality = self.poly_n * 2**(self.n-len(self.S)-1)
            cardTest = len(self.peakSet)
            if self.cardinality == cardTest:
                print(True)
        else:
            self.cardinality = 2**(self.n-1)
        print('cardOfPeakSet:\n#P({};{}):\n'.format(self.S,self.n),self.cardinality,'\n')

    def polyDegree(self):
        if self.S:
            self.degree = self.S[-1]-1
        else:
            self.degree = 0
        print('deg p(n):\n',self.degree)

    def polyFunc(self,cls,S,n):
        if S:
            if (n > S[-1] + 1):
                m = S[-1]
                if m-1 < 2:
                    return 1
                S_1 = S[:-1]
                S_2 = S_1 + [m-1]

                self.poly_n = cls.polyFunc(self,cls,S_1,m-1) * cls.nCr(n,m-1) - 2*cls.polyFunc(self,cls,S_1,n) - cls.polyFunc(self,cls,S_2,n)
            else:
                return 1
        else:
            return 1
   
answers = peakPolynomial(peakPolynomial,[2,4],5)
