import json
import os
def reader(file):
    with open(file, 'r') as f:
        text = f.read()
        return text
def pen(paper, place):
    with open(place, 'w') as f:
        f.write(str(paper))
        f.close()
def changeGlob(x,v):
    globals()[x] = v
def check_str(x,y):
    c = ''
    if str(x) != str(y):
        c = y
    return c
def get_curr_path():
    return os.getcwd()
def home_it():
    curr = get_curr_path()
    slash = '//'
    if '//' not in str(curr):
        slash = '/'
    changeGlob('slash',slash)
    changeGlob('home',curr)
    return curr,slash
def listFiles(x):
    return os.listdir(x)
def isFile(x):
    return os.path.isfile(x)
def isFold(x):
    return os.path.isdir(x)
def getFolds(x):
    ls = listFiles(x)
    lsN = []
    for i in range(0,len(ls)):
        if isFold(x) == True:
            lsN.append(ls[i])
    return lsN
def createPath(x,y):
    if x == '':
        return str(y) + str(check_str(str(y),slash))
    return str(x) + str(check_str(x[-1],slash))+str(y)
def forListDirs(x):
    ls = getFolds(x)
    lsN = []
    lsA = []
    lsB = []
    js = {x.split(slash)[-1]:{}}
    js = js[x.split(slash)[-1]]
    for i in range(0,len(ls)):
        path = createPath(x,ls[i])
        js[str(path.split(slash)[-1])] = {}
        if isFold(path) == True:
            js[str(path.split(slash)[-1])]=str(path)
            lsA.append(path)
            lsB.append(path.split(slash)[-1])
    input(str(lsB))    
    return js,lsA,lsB
def isInt(x):
    try:
        x = int(x)
        return True
    except:
        return False
def forFileListDirs(x):
    ls = getFolds(x)
    lsN = []
    lsA = []
    lsB = []
    js = {x.split(slash)[-1]:{}}
    js = js[x.split(slash)[-1]]
    js["names"] = []
    for i in range(0,len(ls)):
        path = createPath(x,ls[i])
        if isFile(path) == True:
            chk = str(path.split(slash)[-1])
            if isInt(str(path.split(slash)[-1]).split('.')[-1]) == False:
                chk = str(path.split(slash)[-1]).split('.')[0]
                
            js[chk] = str(path)
            js["names"].append(chk)
            lsA.append(path)
            lsB.append(path.split(slash)[-1])
    
    return js,lsA,lsB
def forIt():
    jsall = {}
    js,lsA1,lsB1  = forListDirs('/home/bigrugz/Desktop/newTester/variables/pragmas/8')
    jsF,lsAF1,lsBF1  = forFileListDirs('/home/bigrugz/Desktop/newTester/variables/pragmas/8')
    for i in range(0,len(lsA1)):
        js[lsB1[i].split('.')[0]],lsA,lsB = forListDirs(lsA1[i])
        for c in range(0,len(lsB1)):
            input([jsF,js,lsA1[i],lsB1[c]])
        for k in range(0,len(lsA)):
            
            jsF[lsB[k].split('.')[0]],lsAF,lsBF = forFileListDirs(lsA[k])
            jsall[jsF[lsB[k].split('.')[0]]] = {}
            jsall[jsF[lsB[k].split('.')[0]]][lsAF[i]] = lsBF[i]
    return jsall
def printIt():
    pen(forIt(),'/home/bigrugz/Desktop/newTester/variables/pragmas/names.js')
home,slash = home_it()
printIt()
