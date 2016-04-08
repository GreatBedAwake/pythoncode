#encoding=utf-8
class ScaleSort:
    def sortElement(self,A,n,k):
        m = k
        m1= 0
        h = A[0:k]
        self.structionHeap(h,k-1)
        while m < n:
            A[m1] = h[0]
            h[0] = A[m]
            self.minadjustHeap(h,0,k-1)
            m1=m1+1
            m=m+1
        self.sortheap(A,m1,h,k-1)
        return  A
    def sortheap(self,A,m1,h,end):
        m=end
        while m >=0:
            A[m1]=h[0]
            h[0] = h[m]
            m1=m1+1
            m=m-1
            self.minadjustHeap(h,0,m)


    def structionHeap(self,A,end):
        h = end/2
        while h >=0:
            self.minadjustHeap(A,h,end)
            h=h-1
    def minadjustHeap(self,A,father_n,end):
        left = father_n*2+1
        right = father_n*2+2
        while left <= end:
            min = left
            if right <=end:
                if A[left] > A[right]:
                    min = right
            if A[father_n] > A[min]:
                zjbl = A[father_n]
                A[father_n]=A[min]
                A[min] = zjbl
                father_n = min
                left = father_n*2+1
                right = father_n*2+2
            else:
                break

A = [2,1,4,3,6,5,8,7,10,9]
m=ScaleSort()
print  m.sortElement(A,10,2)
