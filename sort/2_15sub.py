#encoding=utf-8
class Subswquence:
    def shortestSubsquence(self,A,n):
        m=1
        max = A[0]
        left=n-1
        while m <n:
            if A[m] >= max:
                max = A[m]
            else:
                left = m
            m=m+1
        min = A[left]
        m=n-1
        right = left
        while m >=0:
            if A[m] <= min:
                min = A[m]
            else:
                right = m
            m=m-1
        if right <left:
            return left-right+1
        elif right >left:
            return right -left+1
        else :
            return 0
A=[1,2,10,1,8,9]
m=Subswquence()
print m.shortestSubsquence(A,6)