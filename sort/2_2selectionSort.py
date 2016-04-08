#encoding=utf-8
#x选择排序
class SelectionSort:
    def selectionSort(self,A,n):
        m = 0
        while m < n-1:
            j = m
            minsign = A[m]
            minsign_serial=m
            while  j < n:
                if minsign > A[j]:
                    minsign =A[j]
                    minsign_serial=j
                j=j+1
            k = A[m]
            A[m] = minsign
            A[minsign_serial] = k
            m=m+1
        return A
#A=[5,6,8,5,2,3,6]
A = [54,35,48,36,27,12,44,44,8,14,26,17,28]
m=SelectionSort()
print m.selectionSort(A,13)


