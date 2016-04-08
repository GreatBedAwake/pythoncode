#encoding=utf-8
class CountingSort:
    def countingSort(self,A,n):
        cou = []
        for i in xrange(2000):
            cou.append(0)

        for i in xrange(n):
            h = A[i]
            cou[h] = cou[h]+1
        m = 0
        for i in xrange(2000):
            while  cou[i] > 0 :
                A[m] = i
                m=m+1
                cou[i]=cou[i]-1
        return A


A=[3,4,5,10,22,1,2,89,2,6]
m = CountingSort()
print m.countingSort(A,10)


