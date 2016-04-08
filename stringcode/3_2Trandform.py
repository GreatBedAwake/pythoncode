#encoding=utf-8
class Transform:
    def chkTransform(self,A,lena,B,lenb):
        if lena == lenb:
            Adict=self.coutstr(A,lena)
            Bdict=self.coutstr(B,lenb)
            for m in Adict:
                if m not in Bdict:
                    return False
                if Adict[m] != Bdict[m]:
                    return False
            return True
        else:
            return False


    def coutstr(self,A,lena):
        h = 0
        Adict={}
        while h < lena:
            if A[h] in Adict:
                Adict[A[h]] = Adict[A[h]] +1
            else:
                Adict[A[h]]=1
            h=h+1
        return Adict

A='54sdfsfasd'
B='54sdfsfasd'
m=Transform()
print m.chkTransform(A,len(A),B,len(B))