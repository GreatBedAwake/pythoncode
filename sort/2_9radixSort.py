#encoding=utf-8
class RadixSort:
    def radixSort(self,A,n):
        radix=[]
        for i in range(10):
            radix.append([])
        dex=1
        for i in range(5):
            m = 0
            while m < n:
                zjbl = A[m]/dex%10
                radix[zjbl].append(A[m])
                m=m+1
            self.inputradix(A,radix)
            dex = dex*10
            radix=[]
            for i in range(10):
                radix.append([])
        return A
    def inputradix(self,A,radix):
        h=0
        for m in radix:
            for n in m:
                if n!=None:
                    A[h] = n
                    h=h+1

#A = [26,5,77,1,61,11,59,15,48,19]
A = [54,35,48,36,27,12,44,44,8,14,26,17,28]
m=RadixSort()
print m.radixSort(A,13)
