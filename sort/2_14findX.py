#encoding=utf-8
class Finder:
    def findex(self,mat,n,m,x):
        x_ = n-1
        y_ = 0
        while x_ >=0 and y_ <=m-1:
            if x == mat[x_][y_]:
                return True
            elif x > mat[x_][y_]:
                y_=y_+1
            else:
                x_=x_-1
        return False
A=[[109,204,260,270],[452,602,671,917],[1106,1343,1467,1585],[1627,1866,1948,1980],[2108,2164,2295,2577],[2681,2749,2915,3026],[3187,3250,3465,3518],[3562,3773,3966,4101]]
h= Finder()
print h.findex(A,8,4,2108)
