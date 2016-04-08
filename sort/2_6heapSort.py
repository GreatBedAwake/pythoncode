#coding=utf-8
#堆排序
class HeapSort:
    def heapSort(self,A,n):
        self.structureHeap(A,n-1)
        print A
        m = n-1
        while m >0:
            zjbl = A[0]
            A[0] = A[m]
            A[m] = zjbl
            self.adjustHeap(A,0,m-1)
            m=m-1
        return A

    def structureHeap(self,A,end):
        h = end/2
        while h >= 0:
            self.adjustHeap(A,h,end)
            h=h-1

    def adjustHeap(self,A,father_n,end):
        left = father_n *2+1
        right = father_n*2 +2
        maxv = 0
        start = father_n
        while left <= end:
            maxv = left
            if right <= end:
                if A[left] > A[right]:
                    maxv = left
                else:
                    maxv = right
            if A[start] < A[maxv]:
                zjbl = A[start]
                A[start] = A[maxv]
                A[maxv]=zjbl
                start = maxv
            else:
                break
            left = start*2+1
            right = start*2 +2

A = [26,5,77,1,61,11,59,15,48,19]
m = HeapSort()
print  m.heapSort(A,10)
