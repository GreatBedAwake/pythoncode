#encoding=utf-8
class Replacement:
    def replaceSpace(self, iniString, length):
        iniString=list(iniString)
        h = 0
        spacecount=0
        while h < length:
            if iniString[h] ==' ':
                spacecount=spacecount+2
            h=h+1
        m = length +spacecount-1
        h=h-1
        while h >=0:
            if iniString[h] != ' ':
                iniString[m] = iniString[h]
                m=m-1
                h=h-1
            else:
                iniString[m] = '0'
                iniString[m-1]='2'
                iniString[m-2]='%'
                m=m-3
                h=h-1
        return "".join(iniString)

h='dsf sdf fsd sdf                      '
r =Replacement()
m ='sArcCNxjNaviToUsSN QiTtx j bgUhhIoiSfszja QfFkxk JwYOoFSg dhdMKgTxjRrcATfkb ELqIebLGZk kAESkrNJxbmci nyojZqX vawG kxvqf moWAA m aMuilydRRNvVuh Uss mJtnZb zA oF cx hUQD V dSLSLcbjXLydl V dReEozdi ZO IxbW CgcTeobRrmco ELs cQh K xlg Pj cGaO yXKXy hs kmJaSdNV Z InShcp AxoM hHLTsIMhcHKnArxgRVjh MclqtzFpl yzaWlhLfYlfxNFgb                                                                                                                                                                         '
print len(m)
print r.replaceSpace(m,313)


