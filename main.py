#JKL2021

DEBUG=0     #enable debug messages
global cap
global num

#convert brailee to text data
def braille2text(text):
    charDict=loaddict('dict1.txt')
    numDict=loaddict('dict2.txt')
    ret=''
    global cap
    global num
    #print(int(len(text[0])/2))
    for i in range(0,int(len(text[0])/2)):
        char=''
        char+=text[0][2*i]+text[0][2*i+1]
        char+=text[1][2*i]+text[1][2*i+1]
        char+=text[2][2*i]+text[2][2*i+1]
        if char=='000001':
            cap=1
            continue
        if char=="010111":
            num=1
            continue
        try:
            if cap==1:
                ret+=charDict[char].upper()
                cap=0
            elif num==1:
                try:
                    ret+=numDict[char]
                except:
                    ret+=charDict[char]
                    num=0
            else:
                ret+=charDict[char]
        except KeyError:
            ret+='_'
    return ret

#load dictionary
def loaddict(name):
    input=open(name,"r")
    ret={}
    for txt in input:
        txt=txt.split("=")
        ret[txt[1][:-1]]=txt[0]
    input.close()  
    #print(ret)
    return ret



if __name__ == "__main__" :
    cap=0
    num=0
    input=open("target.txt","r")
    length=len(input.readlines())
    input.close()
    input=open("target.txt","r")
    for i in range(0,int(length/3)):
        target=['','','']
        target[0]+=input.readline()[:-1].replace(' ','').replace('<br>','')
        target[1]+=input.readline()[:-1].replace(' ','').replace('<br>','')
        target[2]+=input.readline()[:-1].replace(' ','').replace('<br>','')
    
        if DEBUG :print(target)
        print(braille2text(target))

    input.close()

    """

    #{wynik=coords2display(target)
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

    """

    