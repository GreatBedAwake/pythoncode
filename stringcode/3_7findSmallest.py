#encoding=utf-8
#import itertools
#import copy
class Prior:
    def findSmallest(self,strs,n):
        #strs = list(strs)
        #arrangelist=[]
        #self.arrange(strs,0,n,arrangelist)
        #h = arrangelist[0]
        ss = self.arrange1(strs,n)
        #应该用next调用 ss就是生成器对象
        h=next(ss)
        for m in ss:
            if h > m:
                h= m
        return h
    '''
    def arrange(self,A,s,e,arrangelist):
        if (s >=e):
            print A
            #A中的元素是int型，不能用于此需要转换为str型
            #s="".join(A)

            s="".join(str(h) for h in A)
            arrangelist.append(s)

            #为什么加入列表就会出错呢 哦
            #可能是深浅拷贝的问题。
            #arrangelist.append(A)
            #这样可能是浅拷贝。只是拷贝了指针
            #h=copy.deepcopy(A)
            #arrangelist.append(h)
        else:
            for i in range(s,e):
                self.swap(A,s,i)
                self.arrange(A,s+1,e,arrangelist)
                self.swap(A,s,i)
    '''
    def arrange1(self,A,n):
        A=list(A)
        yield "".join(A)
        h = self.findinflexion(A,n)
        while h!=-1:
            self.find2(A,n,h)
            self.nixu(A,n,h)
            yield "".join(A)
            h=self.findinflexion(A,n)


    def findinflexion(self,A,n):
        h = n-1
        minpos = A[h]
        while h > 0:
            h=h-1
            if A[h] < minpos:
                return h
            else:
                minpos = A[h]
        return -1
    def find2(self,A,n,minpos):
        s = A[minpos]
        bigmin=n-1
        h = n-1
        while h > minpos:
            if A[h] > s:
                bigmin=h
                break
            h=h-1
        while h >minpos:
            if A[h] >s:
                if A[h] < A[bigmin]:
                    bigmin = h
            h=h-1
        zjbl = A[minpos]
        A[minpos]=A[bigmin]
        A[bigmin]=zjbl
    def nixu(self,A,n,minpos):
        mina=minpos+1
        maxa = n-1
        while mina < maxa:
            zjbl = A[mina]
            A[mina]=A[maxa]
            A[maxa]=zjbl
            mina=mina+1
            maxa=maxa-1
    def swap(self,A,s,i):
        zjbl = A[s]
        A[s]=A[i]
        A[i]=zjbl
A=[1,2,3]
B=[]
m = Prior()
#m.arrange(A,0,3,B)
A=['abc','de','ff']
print m.findSmallest(A,len(A))
#print B
'''
h=[1,2,4,5,3]
s = m.findinflexion(h,len(h))
print s
print m.find2(h,len(h),s)
m.nixu(h,len(h),s)
#print h
x = [1,2,3]
for ss in m.arrange1(A,len(A)):
    print ss
'''