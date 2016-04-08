#encoding=utf-8
class Checker:
    def checkDuplicate(self,a,n):
        self.heapSort(a,n)
        d=a[0]
        m =1
        while m <n:
            if d == a[m]:
                return True
            d=a[m]
            m = m+1
        return False

    def heapSort(self,a,n):
        self.structuinheap(a,n-1)
        h=n-1
        while h>0:
            zjbl=a[0]
            a[0]=a[h]
            a[h]=zjbl
            h=h-1
            self.adjustheap(a,0,h)
        return a
    def structuinheap(self,a,end):
        m = end/2
        while m >0:
            self.adjustheap(a,m,end)
            m=m-1
    def adjustheap(self,a,father_n,end):
        left = father_n*2+1
        right=father_n*2+2
        while left <= end:
            maxcount=left
            if right <= end:
                if a[left] < a[right]:
                    maxcount= right

            if a[maxcount] > a[father_n]:
                zjbl = a[father_n]
                a[father_n]=a[maxcount]
                a[maxcount]=zjbl
                father_n=maxcount
                left = father_n*2+1
                right = father_n*2+2
            else:
                break

A = [26,5,77,1,61,11,59,15,48,1]
m = Checker()
print  m.checkDuplicate(A,10)