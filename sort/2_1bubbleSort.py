#coding=utf-8
#冒泡排序
class BubbleSort:
    def bubbleSort(self,A,n):
        while n >0:
            for i in range(n-1):
                if A[i] >A[i+1]:
                    b = A[i]
                    A[i] = A[i+1]
                    A[i+1] = b

            n = n-1
        return A


A=[5,6,8,5,2,3,6]
m=BubbleSort()
print m.bubbleSort(A,7)