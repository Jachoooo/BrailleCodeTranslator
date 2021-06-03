#JKL2021

DEBUG=1     #enable debug messages

#convert coords to signal data
def coords2display(text):
    charDict=loaddict()
    ret=['','','','','','','','']
    for char in text:
        if char=='.':
            ret[7]=ret[7][:-1]+'1'
            continue
        for i,num in enumerate(charDict[char]):
            ret[i]=ret[i]+str(num)
        ret[7]=ret[7]+'0'
    return ret

#load dictionary
def loaddict():
    input=open("dict.txt","r")
    ret={}
    input.readline()
    for txt in input:
        txt=txt.split("#")
        ret[txt[0]]=txt[1][:-1]
    input.close()  
    #print(ret)
    return ret



if __name__ == "__main__" :

    input=open("target.txt","r")
    target=input.readline()[:-1]
    input.close
    wynik=coords2display(target)
    if DEBUG :print(loaddict())
    if DEBUG :print(wynik)
    if DEBUG :printdisplay(wynik)

    output=open("result.txt","r+")
    output.truncate(0)
    output.seek(0)
    output.close()
    output=open("result.txt","w")
    
    txt=['A  ','B  ','C  ','D  ','E  ','F  ','G  ','Dp ']
    for cnt,line in enumerate(wynik):
        line=line.replace('0',LO)
        line=line.replace('1',HI)
        wLine=txt[cnt]+line+"\n"
        output.write(wLine)
    output.close

    