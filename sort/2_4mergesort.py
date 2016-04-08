#coding=utf-8
#归并排序
class MergeSort:
    def mergeSort(self,A,n):
        self.mergeSort2(A,0,n-1)
        return A
    def mergeSort2(self,A,left,right):
        if left < right:
            #出问题的地方
            middle_1=(left+right)/2

            print  'l:'+str(left)
            print 'm'+str(middle_1)
            print 'r'+str(right)
            self.mergeSort2(A,left,middle_1)
            self.mergeSort2(A,middle_1+1,right)
            self.mege(A,left,middle_1,right)
    def mege(self,A,left,middle,right):
        temp = []
        m = left
        n = middle+1
        while m <= middle and n <= right:
            if A[m] < A[n]:
                temp.append(A[m])
                m=m+1
            else:
                temp.append(A[n])
                n=n+1
        #剩余未合并地方
        while m <=middle:
            temp.append(A[m])
            m=m+1
        while n <=right:
            temp.append(A[n])
            n=n+1
        A[left:right+1]=temp
        print temp




A=[5,2,9,5,6,2,6]
h = MergeSort()
#print h.mergeSort(A,7)
print  h.mergeSort(A,7)
