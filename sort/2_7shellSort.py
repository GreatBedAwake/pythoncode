#encoding=utf-8

class ShellSort:
    def shellSort(self,A,n):
        #self.selectionSort(A,3,n-1)
        #self.selectionSort(A,2,n-1)
        self.selectionSort(A,1,n-1)
        return A
    def selectionSort(self,A,step,end):
        #print A
        m = step
        while m <= end :
            h = m-step
            minsign=m
            while h >=0:
                if A[minsign] < A[h]:
                    zjbl = A[minsign]
                    A[minsign] = A[h]
                    A[h] = zjbl
                    minsign = h
                h = h-step

            m = m + 1

#A=[5,9,8,1,3,6]
A = [54,35,48,36,27,12,44,44,8,14,26,17,28]
m =ShellSort()
print m.shellSort(A,13)

