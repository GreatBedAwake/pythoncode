#encoding=utf-8
#插入排序
class Insertionsort:
    def insertionSort(self,A,n):
        j = 0
        while j < n-1:
            u = j
            k = j+1
            while u >= 0:
                if A[k] < A[u]:
                    d = A[u]
                    A[u] = A[k]
                    A[k] = d
                    k=u
                u=u-1
            j=j+1
        return A
A=[5,6,8,5,2,3,6]
m=Insertionsort()
print m.insertionSort(A,7)
