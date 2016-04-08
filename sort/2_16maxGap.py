#encodig=utf-8
class Gap:
    def maxGap(self,A,n):
        [max,min]=self.findmax_min(A,n)
        h = float(max - min)/n
        barrel=[]
        for i in range(n+1):
            barrel.append([])

        for i in range(n):
            pos = int((A[i]-min)/h)
            #print pos
            barrel[pos].append(A[i])
        maxcha=0
        h = 1
        [max,min] = self.findmax_min(barrel[0],len(barrel[0]))
        [max1,min1]=[0,0]
        while h <n+1:
            length = len(barrel[h])
            if length >0:
                [max1,min1]=self.findmax_min(barrel[h],length)
                zjbl=min1-max
                if zjbl >maxcha:
                    maxcha=zjbl
                max = max1
                min=min1
            h=h+1
        return maxcha
    def findmax_min(self,A,n):
        max = A[0]
        min = A[0]
        h = 1
        while h < n:
            if A[h] >max:
                max = A[h]
            if A[h] <min:
                min = A[h]
            h=h+1
        return [max,min]
A=[1,5,2,6,5,8,9]
m=Gap()
print m.maxGap(A,7)