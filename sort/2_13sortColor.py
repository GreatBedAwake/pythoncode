#encoding=utf-8
class ThreeColor:
    def sortColor(self,A,n):
        min0 = 0
        max2 = n-1
        m=0
        ##
        while m <= max2:
            if A[m] <1:
                zjbl = A[m]
                A[m] = A[min0]
                A[min0]=zjbl
                min0=min0+1
                m=m+1
            elif A[m] >1:
                zjbl = A[m]
                A[m]=A[max2]
                A[max2]=zjbl
                max2=max2-1
            else:
                m=m+1
        return A
A= [1,2,0,2]
m=ThreeColor()
print m.sortColor(A,4)