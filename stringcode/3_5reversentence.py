#encoding=utf-8
class Reverse:
    def reversSentence(self,A,n):
        listA = self.nixu(A,n)
        star = 0
        starblack=0
        while starblack < n:
            if listA[starblack] == ' ':
                listA[star:starblack] = self.nixu(listA[star:starblack],len(listA[star:starblack]))
                star = starblack+1
            starblack=starblack+1

        listA[star:starblack] = self.nixu(listA[star:starblack],len(listA[star:starblack]))
        return "".join(listA)

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

A='asdfgh sd'
m = Reverse()
print m.reversSentence(A,len(A))

