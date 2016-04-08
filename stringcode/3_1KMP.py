#encoding=utf-8

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class kmp:
    def chkIdentical(self,A,B):
        Atree=[]
        Btree=[]
        self.treexulie(A,Atree)
        self.treexulie(B,Btree)
        return  self.kmpMaching(Atree,Btree,len(Atree),len(Btree))
    def next1(self,A,n):
        h=1
        nextlist=[0]
        while h <  n:
            j=nextlist[h-1]
            while j>0 and A[j] !=A[h]:
                j = nextlist[j-1]

            if A[j] == A[h]:
                nextlist.append(j+1)
            else:
                nextlist.append(0)
            h=h+1
        return nextlist
    def kmpMaching(self,A,s,An,sn):
        hA=0
        hs=0
        nextlist=self.next1(s,sn)
        while hA <An:
            if A[hA]==s[hs]:
                hA=hA+1
                hs=hs+1
                if hs == sn:
                    return True
            else:
                hs=hs-nextlist[hs]
                if hs==0:
                    hA=hA+1
                else:
                    hA = hA+hs
        return False
    def treexulie(self,A,treestr):
        #前序
        if A == None:
            treestr.append(-1)
        else:
            treestr.append(A.val)
            self.treexulie(A.left,treestr)
            self.treexulie(A.right,treestr)

A='agctagcagctagctg'
s='agctd'
k=kmp()
#print k.kmpMaching(A,s,16,5)
b=TreeNode(4)
a=TreeNode(1)
a.left=TreeNode(2)
a.right=TreeNode(5)
a.left.left=TreeNode(3)
a.left.right=TreeNode(4)
a.right.left=TreeNode(6)
a.right.right=TreeNode(7)
m=[]
k.treexulie(a,m)
print m
m=[]
k.treexulie(b,m)
print m
print  k.chkIdentical(a,b)











