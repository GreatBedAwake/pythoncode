#coding=utf-8

class QuickSort:
    def quicksort(self,A,n):
        self.quicksort1(A,0,n-1)
        return A
    def quicksort1(self,A,startsign,endsign):
        if startsign < endsign:
            h = self.partition(A,startsign,endsign)
            self.quicksort1(A,startsign,h)
            self.quicksort1(A,h+1,endsign)
    def partition(self,A,startsign,endsign):
        zjbl = A[startsign]
        A[startsign] = A[endsign]
        A[endsign] = zjbl
        partitions = startsign
        h = startsign
        while h < endsign:
            if A[h] < zjbl:
                m=A[partitions]
                A[partitions] = A[h]
                A[h]=m
                partitions=partitions+1
            h=h+1
        A[endsign]= A[partitions]
        A[partitions] = zjbl
        return partitions

    def onequicksort(self,A,startsign,endsign):
        h = startsign+1
        m = A[startsign]
        msign = startsign
        while h <=endsign:
            if m > A[h]:
                zjbl = A[msign]
                A[msign] = A[h]
                A[h] = zjbl
                msign = msign+1
            h=h+1
        A[startsign] = A[msign]
        A[msign]=m
        return  msign
A = [54,35,48,36,27,12,44,44,8,14,26,17,28]
m = QuickSort()
print  m.quicksort(A,13)
