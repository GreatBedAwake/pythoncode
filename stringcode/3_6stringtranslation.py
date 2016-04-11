class Tranlation:
    def stringTranslation(self,A,n,len):
        A=list(A)
        A[0:len]=self.nixu(A[0:len],len)
        A[len:n]=self.nixu(A[len:n],n-len)
        A = self.nixu(A,n)
        return "".join(A)
    def nixu(self,A,n):
        A = list(A)
        star = 0
        end = n-1
        i = n/2
        while star < i:
            zjbl = A[star]
            A[star] = A[end]
            A[end] = zjbl
            star = star+1
            end = end-1
        return A
A='ABCDE'
m = Tranlation()
print  m.stringTranslation(A,5,3)