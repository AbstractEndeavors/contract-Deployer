import json
import os.path
import shutil
import json
from web3 import Web3
import os
import time
import stat
import subprocess
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
def find_it_alph(x,k):
    i = 0
    while str(x[i]) != str(k):
        i = i + 1
    return i
def fileInputString(x):
    return "is "+str(x)+" the file you would like to choose?"
def folderInputString(x):
    return "is "+str(x)+" the folder you would like to choose?"
def splitNum(x,spl):
    return len(x.split(spl))
def getPath(x):
    x = createPath(pathAsk,x)
    if isEither(x) != True:
        if str(x)[-1] == slash:
            x = x[:-1]
        if isFold(buildToSplitLast(x,slash)) != True:
            mkAllDir([buildToSplitLast(x,slash)])        
    return x
#VarisInfo-------------------------------------------------------------------------------
def saveVarisInfo():
    pen(varisInfo,varisPath)
def saveFileInfo():
    pen(fileInfo,infoFilePath)
def bulkUpdateVarisInfo():
    stringsLs = ["files","names","currFileDirs","currFilePaths","originalFilePaths","originalFileDirs","currFileDir","currFilePath"]
    varsLs = [file,name,currFileDir,currFilePath,originalFilePath,originalFileDir,currFileDir,currFilePath]
    for i in range(0,len(varsLs)):
        updateVarisInfo(stringsLs[i],varsLs[i])
    saveVarisInfo()
def updateVarisInfo(string,x):
    if string in varisInfo:
        js = varisInfo[string]
        if type(js) is list:
            appendIt(js,x)
        else:
            jsAddIt(js,x)
    else:
        print(str(string),' not in varisInfo')
def appendIt(js,x):
    if x not in js:
        js.append(x)
def jsAddIt(js,x):
    js = x
def updateVarisCount():
    varisInfo["count"] += 1
def getPath(x):
    x = createPath(pathAsk,x)
    if isEither(x) != True:
        if str(x)[-1] == slash:
            x = x[:-1]
        if isFold(buildToSplitLast(x,slash)) != True:
            mkAllDir([buildToSplitLast(x,slash)])        
    return x

#splitters--------------------------------------------------------------------------------------------------------------------------
def splitTo(x,spl,i):
    tryIt = x
    num = splitNum(x,spl)
    keepUp = True
    while keepUp == True:
        if i == -1 and num == 1:
            return x
        tryIt = x.split(spl)[i]
        if num > i:
            if fileInputString(tryIt) != False:
                return tryIt
            
            i +=1
def buildToSplitLast(x,y):
    nSpl = splitIt(x,y)
    n = ''
    if nSpl != False:
        for i in range(0,len(nSpl)-1):
            n += nSpl[i] + y
        return removeLast(n,y)
    return x
def buildFromSplitFirst(x,y):
    nSpl = splitIt(x,y)
    n = ''
    if nSpl != False:
        for i in range(1,len(nSpl)):
            n += nSpl[i] + y
        return removeLast(n,y)
    return x
def splitIt(x,y):
    if str(y) in str(x):
        return x.split(y)
    return False
def removeLast(x,y):
    if x.replace(x[0:-len(y)],'') == y:
        return x[0:-len(y)]
    return x
def safeSplit(x,y,i):
	good = False
	while good == False:
		if str(y) in x:
			x = x.split(str(y))
			if i <= len(x)-1:
				return x[i]
			else:
				ask = create_ask(createPrintList(x),'looks like you entered '+str(i)+' that was too big, what were you looking for?')
				return x[ask]
		else:	
			print('that split was not in the variable')
			return x
def safeSplitSimp(x,y):
    if str(y) in x:
        return x.split(y)
    return 0
def removeFirst(x,y):
    if x.replace(x[1:],'') == y:
        return x[1:]
    return x
def splitInputInt(i):
    return "looks like that returned none, did you want to try "+str(i)+"?"
def removeFromList(x,y,i):
    newLs = []
    if i == int(-1):
        for l in range(0,len(x)):
            if y not in x[l]:
                newLs.append(x[l])
    else:
        for l in range(0,len(x)):
            if y != x[l][i]:
                newLs.append(x[l])
    return newLs

def buildToSplitLast(x,y):
    nSpl = splitIt(x,y)
    n = ''
    if nSpl != False:
        for i in range(0,len(nSpl)-1):
            n += nSpl[i] + y
        return removeLast(n,y)
    return x
def split_lines(file):
    mylines = []                                # Declare an empty list.
    with open (file, 'rt') as myfile:    # Open lorem.txt for reading text.
        for myline in myfile:                   # For each line in the file,
            mylines.append(myline.rstrip('\n')) # strip newline and add to list.
    return mylines
def list_var_in_str(x,y):
    res = [ele for ele in y if(ele in x)]
    return res
#files------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def delFile(x):
    os.remove(x)
def isFile(x):
    return os.path.isfile(x)
def isFold(x):
    return os.path.isdir(x)
def isEither(x):
    if isFile(x) == True:
        return True
    if isFile(x) == True:
        return 
def moveFile(x,y):
    if exists(x) == False:
    	if x in list_files(y):
    		print('file has already been moved')
    		return
    shutil.move(x, y)
    if x[-1] == slash:
        x = x[:-1]
    if y[0] == slash:
        y = y[1:]
    return x + slash + y
def fileExists(x):
    return os.path.exists(x)
def isFold(x):
    return os.path.isdir(x)
def isFile(x):
    return os.path.isfile(x)
def existFoldCheck(x):
    if isFold(x) == False:
        mkDir(x)
    return x
def existFileCheck(x):
    if isFile(x) == True:
        pen('',x)
    return x
def createExistFile(x,y):
    return existFileCheck(createPath(x,y))
def createExistFold(x,y):
    return existFoldCheck(createPath(x,y))
#Directories-------------------------------------------------------------------------------------------
def change_path(x):
    os.path.abspath(x)
def get_curr_path():
    return os.getcwd()
def get_parent_dir():
    return str(get_curr_path()).replace('/'+str(get_curr_path()).split('/')[-1],'')
def change_parent_dir():
    return change_gears(get_parent_dir())
def change_gears(x):
    curr = get_curr_path()
    change_path(x)
    return curr
def home_it():
    curr = get_curr_path()
    slash = '//'
    if '//' not in str(curr):
        slash = '/'
    changeGlob('slash',slash)
    changeGlob('home',curr)
    return curr,slash
def createPath(x,y):
    if x == '':
        return str(y) + str(check_str(str(y),slash))
    return str(x) + str(check_str(x[-1],slash))+str(y)
def check_dir(x):
    return os.path.isdir(x)
def do_all_dir(x):
    x = x.split(slash)
    m = ''
    for i in range(0,len(x)):
        n = x[i]
        m = createPath(m,n)
        do_the_dir(m)
def do_the_dir(x):
    if check_dir(x) == False:
        make_dir(x)
def check_file(x):
    return os.path.isfile(x)
def do_the_file(x,y,z):
    if check_file(x) == False:
        pen(y,z)
        return y
    return reader(z)
def make_dir(x):
    if check_dir(x) == False:
        os.mkdir(x)
def delete_it(x):
    os.remove(x)
def find_it(x,y):
    i = 0
    for i in range(0,len(x)):
        if str(x[i]) == str(y):
            return i
    return False
def list_files(x):
    return os.listdir(x)

#Directories-----------------------------------------------------------------------------------------------------------------------------------------------------
def createPath(x,y):
    if x == '':
        return str(y) + str(check_str(str(y),slash))
    return str(x) + str(check_str(x[-1],slash))+str(y)
def mkAllPath(x):
    x = checkIsList(x)
    z = x[0]
    for i in range(1,len(x)):
         z = createPath(z,x[i])
    return z
def mkAllDir(x):
    return mkDir(mkAllPath(x))
def mkDir(x):
    if isDir(x) == False:
        os.makedirs(x, exist_ok = True)
    return x
def pathMk(x,y):
    if x[-1] == slash:
        x = x[:-1]
    if y[0] == slash:
        y = y[1:]
    return x + slash + y
def mkDir(x):
    os.makedirs(x, exist_ok = True)
    return x
#fileFunctions----------------------------------------------------------------------------
def openFileExplorer(x):
    x ='open '+x
    subprocess.Popen(x, shell=True)
def getTime():
    return time.time()
def calcTimeInDays(x):
    return str(round((getTime()-x)/(60*24*60),2))+' days'
def calcKb(x):
    return str(round(x/1000,2))+' kb'
def subTime(x,y):
    return calcTime(x)-calcTime(y)
def foldTime(x,ls,i):
    return os.stat(x+'/'+ls[i])[9]
def foldSize(x,ls,i):
    return os.stat(x+'/'+ls[i])[6]
def timeSpacing(x,i,time,size):
    teb = ' \t'
    h = x[i]
    var = [time,size]
    teb = '             '
    exSpace = len(str()+teb)-len(str(x[i]))
    for k in range(0,2):
        te = ' \t'
        if k ==0:
            te = ' \t'
            now = exSpace-(len(x)+len(te))
            take = int(now)/len(' ')
            for c in range(0,int(exSpace)):
                h = h+' '
        h = h+te+var[k]
    return  h
def allTimeDays(x,ls,i):
    return timeSpacing(ls[i])
def allSizeDays(x,ls,i):
    if calcKb(foldSize(x,ls,i)) != float(0):
        return timeSpacing(ls,i,str(calcTimeInDays(foldTime(x,ls,i))),str(calcKb(foldSize(x,ls,i))))
def listSolFiles(x):
    lsN = []
    ls = os.listdir(x)
    for i in range(0,len(ls)):
        if isFile(ls[i]) == True and '.sol' in foldList[i]:
            lsN.append(foldList[i])
    return lsN
def listFolds(x):
    lsN = []
    ls = os.listdir(x)
    for i in range(0,len(ls)):
        if isFold(ls[i]) == True:
            lsN.append(foldList[i])
    return lsN
def findSols(x):
    ls = os.listdir(x)

    lsN = []
    z = x
        
    for k in range(0,len(listFolds(z))):
        n = listFolds(x)[k]
        z = z+'/'+n
        for i in range(0,len(n)):
             print(listFolds(z),listSolFiles(z[k][i]))

def getToEnd(x):
    ls = os.listdir(x)
    
def displayFiles(x):
    exit = False
    n = x
    avoid = True
    #avoid = boolAsk("avoid hidden?")
    while exit != True:
        x = x.split(' ')[0]
        foldList = os.listdir(x)

        lsN = []
        for i in range(0,len(foldList)):
            if isFile(foldList[i]) == True and '.sol' in foldList[i]:
                lsN.append(foldList[i])
                
                
        if avoid == True:
            foldList = removeFromList(foldList,'.',0)
            ls = []
            lsGet = []
            for i in range(0,len(foldList)):
                if '0.0 kb' not in allSizeDays(x,foldList,i):
                    ls.append(allSizeDays(x,foldList,i))
                    lsGet.append(x)
        ask = createAsk(ls,ls,'current Directory '+str(x)+'\nurrent Directorywhich file would you like to use?')
        ask = str(ask.split(' ')[0])
        if ask == "exit":
            exit == True
        elif ask == "back":
        	n = buildToSplitLast(n,slash)
        elif  ask == "open":
            openFileExplorer(x)
        elif str(ask) in foldList:
            n = n+slash+ask
        else:
            n = n+slash+ask
        if isFile(n) == True:
            if boolAsk(fileInputString(splitTo(n,slash,-1))) == False:
            	n = buildToSplitLast(n,slash)
            else:
                return n
        x = n+slash
def getFolder(x):
    exit = False
    n = x
    avoid = True
    #avoid = boolAsk("avoid hidden?")
    while exit != True:
        foldList = os.listdir(x)
        if avoid == True:
            foldList = removeFromList(foldList,'.',0)
        ask = create_ask(foldList,'which folder would you like to use?')
        if ask == "exit":
            exit == True
        elif ask == "back":
            n = buildToSplitLast(n,slash)
        elif  ask == "open":
            openFileExplorer(x)
        elif str(ask) in foldList:
            n = n+slash+ask
        else:
            n = n+slash+ask
        if isFold(n) == True:
            if boolAsk(folderInputString(splitTo(n,slash,-1))) == False:
                n = buildToSplitLast(n,slash)
            else:
                return n
        x = n+slash        

#ASKfunctions-----------------------------------------------------------------------------
def createAlph(i):
    k = int(i/int(26) + 1)
    alph = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.split(',')
    alphNew = []
    alLen = i
    for l in range(0,k):
        lenNow = i
        if i>int(26):
            lenNow = int(26)
        for c in range(0,lenNow):
            n = alph[c]
            for ck in range(0,l):
                n = n + alph[c]
            alphNew.append(n)
        i -=1
    return alphNew
def get_alph():
    alph = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp,qq,rr,ss,tt,uu,vv,ww,xx,yy,zz,aaa,bbb,ccc,ddd,eee,fff,ggg,hhh,iii,jjj,kkk,lll,mmm,nnn,ooo,ppp,qqq,rrr,sss,ttt,uuu,vvv,www,xxx,yyy,zzz,aaaa,bbbb,cccc,dddd,eee,fff,ggg,hhh,iii,jjj,kkk,lll,mmm,nnn,ooo,ppp,qqq,rrr,sss,ttt,uuu,vvv,www,xxx,yyy,zzz'
    return alph.split(',')
def create_ask(x,y):
        alph = get_alph()
        n = y + '\n0) to exit\n1) back\n2) openFileExplorer\n'
        alph = createAlph(len(x))
        alphGood = ['0','1','2']
        for i in range(0,len(x)):
        	alphGood.append(alph[i])
        	n = n + str(alph[i]) + ') '+str(x[i])+'\n'
        while True:
        	ask = input(n)
        	if ask in alphGood:
        		if ask == str(0):
        		    return True
        		if ask == str(1):
        		    return "back"
        		if ask == str(2):
        		    return "open"
        		i = find_it_alph(alph,str(ask))
        		return x[i]
        	print('looks like you entered an input that was not selectable,please re-input your selection')
def createAsk(x,y,z):
        alph = get_alph()
        n = z + '\n0) to exit\n1) back\n2) openFileExplorer\n'
        alph = createAlph(len(x))
        alphGood = ['0','1','2']
        for i in range(0,len(x)):
        	alphGood.append(alph[i])
        	n = n + str(alph[i]) + ') '+str(x[i])+'\n'
        while True:
        	ask = input(n)
        	if ask in alphGood:
        		if ask == str(0):
        		    return True
        		if ask == str(1):
        		    return "back"
        		if ask == str(2):
        		    return "open"
        		i = find_it_alph(alph,str(ask))
        		return y[i]
        	print('looks like you entered an input that was not selectable,please re-input your selection')

def boolAsk(x):
    yes = ['y','yes','true','t','']
    no = ['n','no','false','f']
    ask = input(x)
    ask = str(ask).lower()
    if str(ask) in x and str(ask) not in yes and str(ask) not in no:
        return ask
    if ask in yes:
        return True
    return False
#globalFuncs----------------------------------------------------------------------------------------------------
def changeGlob(x,v):
    globals()[x] = v
def jsPlace(x,y,js):
    if x not in js:
        return json.loads(str(str(js)[:-1]+',"'+str(x)+'":'+str(y)+'}').replace('{,','{').replace("'",'"'))
def addToIt(i,k):
    return int(i)+int(k)
def reader(file):
    with open(file, 'r') as f:
        text = f.read()
        return text
def pen(paper, place):
    with open(place, 'w') as f:
        f.write(str(paper))
        f.close()
def ifseperator(x):
    if eatAllMod(x,['','\t',' ','\n'])[:len('//')] != '//':
        if '----------' in x:
            return [True,True]
        return [True,False]
    return [False,False]
def readLinesSpec(x):
    lsN = []
    lines = x.replace('\n','^*&*****').split('^*&*****')
    for i in range(0,len(lines)):
        lines[i] = eatOuterMod(lines[i],['\n','\t',' ',''])
        if lines[i] not in ['\n',' \n','',' ','\t']  and len(str(eatAllMod(lines[i],['\n','\t',' ','/',';','']))) != 0:
            lsN.append(lines[i]+'\n')
    return lsN

def readLines(x):
    lsN = []
    lines = reader(x).replace('\n','^*&*****').split('^*&*****')
    for i in range(0,len(lines)):
        lines[i] = eatOuterMod(lines[i],['\n','\t',' ',''])
        if lines[i] not in ['\n',' \n','',' ','\t']  and len(str(eatAllMod(lines[i],['\n','\t',' ','/',';','']))) != 0:
            lsN.append(lines[i]+'\n')
    return lsN
def isInList(x,ls):
    newLs = []
    for i in range(0,len(ls)):
        n = ls[i]
        nn = ''
        for k in range(0,len(n)):
            nn = nn + n[k]        
        if str(x) == str(nn):
            newLs.append(n)
    return len(newLs),newLs
def stopWhenClosed(x,ls):
    ls = checkIsList(ls)
    for i in range(0,len(x)):
        y = x[0:i]
        lenLs = [countIt(y,str(ls[0])),countIt(y,str(ls[1]))]
        if lenLs[0] == lenLs[1] and lenLs[0] != 0:
            return y
    return False
def stopWhenClosedI(x,ls):
    ls = checkIsList(ls)
    x = linesToString(x)
    for i in range(0,len(x)):
        y = x[0:i]
        lenLs = [countIt(y,str(ls[0])),countIt(y,str(ls[1]))]
        if lenLs[0] == lenLs[1] and lenLs[0] != 0:
            return 
    return y+'\n}'
def stopWhenClosedRemove(x,ls):
    ogX = len(x)
    ls = checkIsList(ls)
    x = linesToString(x)
    for i in range(0,len(x)):
        y = x[0:i]
        lenLs = [countIt(y,str(ls[0])),countIt(y,str(ls[1]))]
        if lenLs[0] == lenLs[1] and lenLs[0] != 0:
            return readLinesSpec(x)[len(readLinesSpec(y)):]

def getFullSection(x):
    return stopWhenClosed(cont[prevK:],['{','}'])(linesToString(lines[fileInfo["allVarsTrack"][x][-1]:]),['{','}'])

def determineSection(x,ls):
    n = ''
    lsComp = []
    for i in range(0,len(str(x))):
        n = n + x[i]
        match = isInList(n,ls)
        if match[0] == 1:
            return match[1][0]
        elif match[0] == 0:
            return None
def isCurrent(x,y):
    if x[:len(y)] == y:
        return True
    return False
def eatInner(x):
    x = str(x)
    ls = [' ','\t','\n']
    while len(x) >0 and x[0] in ls:
        x = x[1:]
    if len(x) == 0:
        return None
    return x
def eatAllMod(x,ls):
    if len(x) != 0:
        x = eatInnerMod(x,ls)
    if len(x) != 0:
        x = eatOuterMod(x,ls)
    return x
def ifOverZero(x):
    if len(x) >0:
        return True
    return False
def strInList(x,ls):
    if ifOverZero(x) == True:
        if x[0] in ls:
            return x[1:]
    return False
def eatInnerMod(x,ls):
    if strInList(x,ls) != False:
        x = strInList(x,ls)
    return x
def eatOuterMod(x,ls):
    if len(x)>1:
        while x[-1] in ls and len(x) >1:
            x = x[:-1]
        return x
    return x
def findIt(x,y):
    for i in range(0,len(y)):
        if x == y[i]:
            return i
def checkIsList(ls):
    if type(ls) is not list:
        if ',' in str(ls):
            ls = str(ls.split(','))
        else:
            ls = [ls]
    return ls
def countIt(x,y):
    return (len(x)-len(x.replace(y,'')))/len(y)
def stopWhenClosed(x,ls):
    ls = checkIsList(ls)
    for i in range(0,len(x)):
        y = x[0:i]
        lenLs = [countIt(y,str(ls[0])),countIt(y,str(ls[1]))]
        if lenLs[0] == lenLs[1] and lenLs[0] != 0:
            return y
    return False
def linesToString(x):
    x = checkIsList(x)
    nn = ''
    for i in range(0,len(x)):
        n = x[i]
        for c in range(0,len(n)):
            nn = nn + n[c]
    return nn
def getConstructor(lineTrack):
        return lineTrack
def getHigher(x,y):
    if int(y) > int(x):
        return y
    return x
def getJustHigher(k,ls):
    for i in range(0,len(ls)):
        if ls[i]>k:
            return i
def isInt(x):
    try:
        n =int(x)
        return True
    except:
        return False
def ListInString(x,ls):
    ls = checkIsList(ls)
    lsN = []
    for i in range(0,len(ls)):
        if ls[i] in x:

            lsN.append(ls[i])
    return lsN
def linesToString(x):
    x = checkIsList(x)
    nn = ''
    for i in range(0,len(x)):
        n = x[i]
        for c in range(0,len(n)):
            nn = nn + n[c]
    return nn
def findFirstString(x,ls):
    first = [ls[0],len(x)]
    for i in range(0,len(ls)):
        if len(x.split(ls[i])[0])<first[-1]:
            first = [ls[i],len(x.split(ls[i])[0])]
    return first[0]
def detNumInWhile(x,string,k):
    lenget = k
    for i in range(0,len(string)):
        found = ListInString(string[lenget],['for','while'])
        if len(found)>0:
            nn = ''
            n = str(stopWhenClosed(linesToString(string[lenget:]),['(',')'])).replace(' ','').replace('\n','').replace('\t','')
            n = n.split('(')[1].split(')')[0].split(';')
            nowIntA = n[0].split('=')[1]
            found = ListInString(n[1],['=<','<','>','>=','=','^'])
            nowIntB = n[1].split(found[0])[1]
            if found[0] == '<':
                nowIntB = int(nowIntB) - 1
            return nowIntB
        lenget -=1
def checkLsAndGetNew(ls):
    return checkIsList(ls),[]
def makeAllComparable(ls):
    ls,lsN = checkLsAndGetNew(ls)
    for i in range(0,len(ls)):
        lsN.append(str(ls[i].lower()))
    return lsN
def makeAllString(ls):
    ls,lsN = checkLsAndGetNew(ls)
    for i in range(0,len(ls)):
        lsN.append(str(ls[i]))
    return lsN
def getHighestIntSpec(ls):
    hi = [0,0]
    for i in range(0,len(ls)):
        if int(ls[i])>int(hi[1]):
            hi = [i,int(ls[i])]
    return hi[0]
def getHighestFloatSpec(ls):
    hi = [0,0]
    for i in range(0,len(ls)):
        if float(ls[i])>float(hi[1]):
            hi = [i,float(ls[i])]
    return hi[0]
def getHighestLen(ls):
    hi = [0,0]
    for i in range(0,len(ls)):
        if len(ls[i])>int(hi[1]):
            hi = [i,len(ls[i])]
    return hi[0]
def isIn(x,st):
    if str(x) in str(st):
        return True
    return False
def fillList(k,ls,y):
    ls = checkIsList(ls)
    for i in range(len(ls),k):
        ls.append(y)
    return ls
def returnZK(z,k,ls,y):
    return '',int(k)+1,fillList(int(k)+2,ls,y)
def isSame(x,y):
    x,y = makeAllString([x,y])
    lsN = ['']
    k = 0
    z = x[0]
    for i in range(1,len(str(x))):
        if isIn(z,y) == True:
            lsN[k] = z
        else:
            z,k,lsN = returnZK(z,k,lsN,'')
        z = z+x[i]
    return [x,lsN[getHighestLen(lsN)]]
def getPercSame(x,y):
    return len(x)/len(y)
def compareOverHalf(x,y):
    if getPercSame(isSame(x,y)) > 0.5:
        return True
    return False
def trueLoc(ls):
    ls,lsN = checkLsAndGetNew(ls)
    for i in range(0,len(ls)):
        if ls[i] == True:
            lsN.append(i)
    return lsN
def compareList(x,ls):
    ls,lsN = checkLsAndGetNew(ls)
    for i in range(0,len(ls)):
        lsN.append(getPercSame(x,isSame(x,ls[i])))
    return ls[getHighestFloatSpec(lsN)]
def returnMostAbundant(ls,lsNone):
    ls,lsN = checkLsAndGetNew(ls)
    newJs = {"names":[]}
    for i in range(0,len(ls)):
        if ls[i] not in lsNone:
            newJs = jsPlace(ls[i],0,newJs)
            newJs["names"].append(ls[i])
        newJs[ls[i]] = addToIt(newJs[ls[i]],1)
    for i in range(0,len(newJs["names"])):
        lsN.append(newJs[newJs["names"][i]])
    return newJs["names"][getHighestIntSpec(lsN)]
def get_c(x):
    c = ','
    if int(x) == int(0):
        c = ''
    return c
def addLsJs(x,y):
    return js_it(str(str(x)[:-1]+',"'+str(y)+'":[]}').replace('{,','{'))
def safeSplit(x,y,i):
    good = False
    while good == False:
        if str(y) in x:
            x = x.split(str(y))
            if i <= len(x)-1:
                return x[i]
            else:
                ask = create_ask(createPrintList(x),'looks like you entered '+str(i)+' that was too big, what were you looking for?')
                return x[ask]
        else:	
            print('that split was not in the variable')
            return x
def check_str(x,y):
    c = ''
    if str(x) != str(y):
        c = y
    return c
def getAny(st,st2):
    return lineTrack[st][st2]
def appendAny(st,st2,x):
    lineTrack[st][st2].append(x)
def appendAnySpec(st,st2,x,i):
    lineTrack[st][st2][i].append(x)
def updateAnySpec(st,st2,x,i):
    lineTrack[st][st2][i] = x
def updateAny(st,st2,x):
    lineTrack[st][st2] = x
def updateLineTrack(x):
    lineTrack = x
    return lineTrack
def LineTrackJsPlace(js,st,brac):
    
    return jsPlace(st,brac,js)
def ifNotThenAdd(js,x):
    if len(js[str(x)]) == 0:
        js[str(x)] = {}
        return js
    return json.loads(str(str(js)[:-1]+get_c(len(js))+str(x)+':""}').replace("'",'"'))
def createAllVars():
    for i in range(0,len(lines)):
        x = eatInnerMod(lines[i],['\n','\t',' ','/'])
        for k in range(0,len(allVars)):
            if isCurrent(x,allVars[k]) == True:
                if i not in getAny(allVars[k],"lines"):
                   appendAny(allVars[k],"lines",i)
def existWriteFileRead(x,y):
    if fileExists(y) == False:
        pen(x,y)
    return reader(y).replace("'",'"')
def splitVarOutAndEndOrSpace(x,y):
    if x+' ' in y:
        x = x+' '
    n = y.split(str(x))[1]
    if ' ' in n:
        n = n.split(' ')[0]
    return n
def createPath(x,y):
    if x == '':
        return str(y) + str(check_str(str(y),slash))
    return str(x) + str(check_str(x[-1],slash))+str(y)
def jsRead(x):
    return json.loads(reader(x).replace("'",'"'))
def js_it(x):
    return json.loads(str(x).replace('{,','{').replace(',}','}').replace('[,','[').replace(',]',']').replace("'",'"'))
def splitAndSee(x,ls):
    lsN = [0,0]
    less = ['=<','<']
    great = ['>','>=']
    for i in range(0,len(att)):
        n = ls[i]
        x = eatInner(x)
        det = determineSection(x,[n])
        if x[0] == '^':
        	lsN = [convertPragToInt(x),convertPragToInt(pragHiffPieces(x))]
        elif det != None:
            xn = splitVarOutAndEndOrSpace(det,n)
            if n in less:
                if det == less[0]:
                    lsN = [convertPragToInt(pragmaVers[pragmaVers["vers"][-1]][-1]),xn]
                else:
                    lsN = [0,pragSubPieces(xn)]
            if n in great:
                if det == less[0]:
                    lsN = [xn,convertPragToInt(pragmaVers[pragmaVers["vers"][0]][0])]
                else:
                    lsN = [convertPragToInt(eatInnerMod(x,ls)),convertPragToInt(pragmaVers[pragmaVers["vers"][0]][0])]
    return lsN
def get_prag(lines,pr):
    ls_pr = '{}'
    for i in range(0,len(pr)):
        n = lines[pr[i]]
        n = n.split('pragma solidity ')[1]
        n = n.split(';')[0]
        if str(pr[i]) not in ls_pr:
            ls_pr = js_it(str(str(ls_pr) + ','+str(make_js(pr[i],n)+'}')).replace('{,','{'))
        return ls_pr
def pragmaRange(ls):
    ls = checkIsList(ls)
    pragCurr = [0,0]
    for i in range(0,len(ls)):
        prag = splitAndSee(ls[i],att)
        if int(pragCurr[0]) < int(prag[0]):
            pragCurr[0] = prag[0]
        if int(pragCurr[1]) < int(prag[1]):
            pragCurr[1] = prag[1]
    print(pragCurr)
    pragCurr = [eatOuterMod(createPragFromInt(pragCurr[0]),'0'),eatOuterMod(createPragFromInt(pragCurr[1]),'0')]
    return pragCurr
def listAllPragma():
    pragsVers = jsRead(createPath(home,'variables/prags.py'))
    pragmaVers = {"vers":[]}
    for i in range(0,len(pragsVers['prags'])):
    	n = pragsVers['prags'][i][1:]
    	nn = ''
    	while n[0] !='-' and n[0] != '+':
    		nn = nn + n[0]
    		n = n[1:]
    	vers = safeSplit(nn,'.',1)
    	if vers not in pragmaVers:
    		pragmaVers = addLsJs(pragmaVers,str(vers))
    		pragmaVers["vers"].append(vers)
    	if nn not in pragmaVers[vers]:
    		pragmaVers[vers].append(nn)
    return pragmaVers
def createPragFromInt(x):
    x = str(x)
    return '0.'+x[0]+'.'+eatOuterMod(x[1:],'0')+ '0'
def convertPragToInt(x):
	a,b = str(safeSplit(x,'.',1)),str(safeSplit(x,'.',2))+ '0'
	return a+b
def pragmaVerSplit(x):
    return safeSplit(x,'.',1)
def pragHiffPieces(x):
    return pragmaVers[str(pragmaVerSplit(x))][0]
def pragPlusPieces(x):
    return pragmaVers[pragmaVerSplit(x)][findIt(x,pragmaVers[pragmaVerSplit(x)])+1]
def pragSubPieces(x):
    return pragmaVers[pragmaVerSplit(x)][findIt(x,pragmaVers[pragmaVerSplit(x)])-1]
def createWord():
    import random
    from random import randint
    k = ''
    for i in range(0,random.randint(0,45)):
        k = k + str(get_alph()[random.randint(0, len(get_alph())-1)])
    return k
def getLast(x,y):
    if splitNum(x,y) == 1:
        return x.split(y)[0]
    return x.split(y)[-1]
def splitNum(x,spl):
    return len(x.split(spl))
def ifFileCreate(x):
    if isFile(x) == False:
        pen('',x)
def ifFoldCreate(x):
    if isFold(x) == False:
        mkDir(x)

#copyFunctions----------------------------------------------------------------------------------------------------
def copyAll(x,y):
    list = os.listdir(x)
    for i in range(0,len(list)):
        ifFoldCreate(pathMk(y,list[i]))
        if isFile(pathMk(x,list[i])) == True:
            copyFile(pathMk(x,list[i]),y)
def copyFile(x,y):
	pen(reader(x),pathMk(y,getLast(x,slash)))
def copyIt(x,y):
    k = pathMk(x,getLast(x,slash))
def addLines(st,i):
    lineTrack[st]['lines'].append(i)
    allLines.append(i)
def SPDXLines():
    lineTrack['SPDX-License-Identifier'] = {"lines":[],"Licenses":[],"License":[],"lic":""}
    for i in range(0,len(lines)):
        x = eatOuterMod(lines[i],['\n','\t',' ','/'])
        if isCurrent(x,'//SPDX-License-Identifier:') == True:
            addLines('SPDX-License-Identifier',i)
            lineTrack['SPDX-License-Identifier']["License"].append(x.split('SPDX-License-Identifier:')[1].replace(' ','').replace('\n',''))
            input(lineTrack)
    spdx= {"0":"No License (None)","1":"The Unlicense (Unlicense)","2":"MIT License (MIT)","3":"GNU General Public License v2.0 (GNU GPLv2)","4":"GNU General Public License v3.0 (GNU GPLv3)","5":"GNU Lesser General Public License v2.1 (GNU LGPLv2.1)","6":"GNU Lesser General Public License v3.0 (GNU LGPLv3)","7":"BSD 2-clause &quot;Simplified&quot; license (BSD-2-Clause)","8":"BSD 3-clause &quot;New&quot; Or &quot;Revised&quot; license (BSD-3-Clause)","9":"Mozilla Public License 2.0 (MPL-2.0)","10":"Open Software License 3.0 (OSL-3.0)","11":"Apache 2.0 (Apache-2.0)","12":"GNU Affero General Public License (GNU AGPLv3)","13":"Business Source License (BSL 1.1)"}
    spdxId = []
    for i in range(0,len(spdx)):
        n = safeSplit(safeSplit(spdx[str(i)],' (',1),')',0)
        spdxId.append(n)
    spdxId = makeAllComparable(spdxId)
    spdxLines = getAny('SPDX-License-Identifier','lines')
    for i in range(0,len(spdxLines)):
        lineTrack['SPDX-License-Identifier']['License'].append(compareList(makeAllComparable(eatAllMod(lines[spdxLines[i]].split('SPDX-License-Identifier:')[1],['\n','\t',' ','/',',']))[0],spdxId))       
    for i in range(0,len(getAny('SPDX-License-Identifier','License'))):
        lic = returnMostAbundant(getAny('SPDX-License-Identifier','License'),['',None,False,True])
        lineTrack['SPDX-License-Identifier']['lic'] = lic
    
def allLines():
    lineTrack['SPDX-License-Identifier'] = {"lines":[],"Licenses":[],"License":[],"lic":""}
    lineTrack['pragma solidity'] = {"lines":[],"range":[],"prags":[],"pragma":""}
    lineTrack['function'] = {"lines":[],"names":[],'external':[]}
    lineTrack['library'] = {"lines":[],'names':[]}
    lineTrack['contract'] = {"lines":[],'names':[]}
    lineTrack['abstract contract'] = {"lines":[],'names':[]}
    lineTrack['interface'] = {"lines":[],'names':[]}
    lineTrack['constructor'] = {'lines':[],'constructorVars':{"attributes":[],"constVariables":[],"type":[],"variables":[]}}
    for i in range(0,len(lines)):
        x = eatAllMod(lines[i],['\n','\t',' ','/'])
        if isCurrent(x,'//SPDX-License-Identifier:') == True:
        if isCurrent(x,'pragma solidity') == True:
        if isCurrent(x,'using') == True:
        if isCurrent(x,'contract') == True:
        if isCurrent(x,'abstract contract') == True:
        if isCurrent(x,'interface') == True:
        if isCurrent(x,'constructor') == True:
        if isCurrent(x,'function') == True:
def getPragLines():
    lineTrack['pragma solidity'] = {"lines":[],"range":[],"prags":[],"pragma":""}
    for i in range(0,len(lines)):
        x = eatInnerMod(lines[i],['\n','\t',' ','/'])
        if isCurrent(x,'pragma solidity') == True:
            addLines('pragma solidity',i)
            lineTrack['pragma solidity']["prags"].append(x.split('pragma solidity')[1].split(';')[0])
            input(lineTrack)
def queryFunctions():
    lsN = {"names":[],"external":[]}
    lineTrack['function'] = {"lines":[],"names":[],'external':[]}
    for i in range(0,len(lines)):
        x = eatAllMod(lines[i],['\n','\t',' ','/'])
        if isCurrent(x,'function') == True:
            addLines('function',i)
            lsN['names'].append(x.split('function')[1].split('(')[0])
            if 'external' in x:
                lsN["external"].append(x.split('{')[0].replace('external','external virtual ').replace('  ',' ')+';')
    pen(lsN,createPath(currFileDir,'Functions.json'))
def queryLibraries():
    lineTrack['library'] = {"lines":[],'names':[]}
    for i in range(0,len(lines)):
        x = eatInnerMod(lines[i],['\n','\t',' ','/'])
        if isCurrent(x,'using') == True:
            addLines('library',i)
            lineTrack['library']['names'].append(x.split('using ')[1].split(' ')[0])
            if str(lineTrack['library']['names'][-1]) not in lineTrack['library']:
                lineTrack['library'][lineTrack['library']['names'][-1]]= {'attributes':[],"address":""}
            lineTrack['library'][lineTrack['library']['names'][-1]]['attributes'].append(str(x.split(' ')[-1].split(';')[0]))

def queryContracts():
    lineTrack['contract'] = {"lines":[],'names':[]}
    for i in range(0,len(lines)):
        x = eatInnerMod(lines[i],['\n','\t',' ','/',','])
        if isCurrent(x,'contract') == True:
            addLines('contract',i)
            lineTrack['contract']['names'].append(eatOuterMod(x,['\n','\t',' ','/',';']).split(' ')[1])
            if str(lineTrack['contract']['names'][-1]) not in lineTrack['contract']:
                lineTrack['contract'][str(getAny('contract','names')[-1])] = {'address':"","attributes":[]}
            if ' is ' in x:
                atts = x.split(' is ')[1].split('{')[0].replace(' ','')
                if ',' in atts:
                    atts = atts.split(',')
                atts = checkIsList(atts)   
                for k in range(0,len(atts)):
                    lineTrack['contract'][str(getAny('contract','names')[-1])]['attributes'].append(atts[k])

def queryAbstract():
    lineTrack['abstract contract'] = {"lines":[],'names':[]}
    for i in range(0,len(lines)):
        x = eatInnerMod(lines[i],['\n','\t',' ','/',','])
        if isCurrent(x,'abstract contract') == True:
            addLines('abstract contract',i)
            lineTrack['abstract contract']['names'].append(eatOuterMod(x,['\n','\t',' ','/',';']).split(' ')[2])
            if str(lineTrack['abstract contract']['names'][-1]) not in lineTrack['abstract contract']:
                lineTrack['abstract contract'][str(lineTrack['abstract contract']['names'][-1])] = {'address':"","attributes":[],"name":""}
            if ' is ' in x:
                atts = x.split(' is ')[1].split('{')[0].replace(' ','')
                if ',' in atts:
                    atts = atts.split(',')
                atts = checkIsList(atts)   
                for k in range(0,len(atts)):
                    lineTrack['abstract contract'][str(lineTrack['abstract contract']['names'][-1])]['attributes'].append(atts[k])

def queryInterface():
    lineTrack['interface'] = {"lines":[],'names':[]}
    for i in range(0,len(lines)):
        x = eatInnerMod(lines[i],['\n','\t',' ','/',','])
        if isCurrent(x,'interface') == True:
            addLines('interface',i)
            lineTrack['interface']['names'].append(eatOuterMod(x,['\n','\t',' ','/',';']).split(' ')[1])
            if str(lineTrack['interface']['names'][-1]) not in lineTrack['interface']:
                lineTrack['interface'][str(lineTrack['interface']['names'][-1])] = {'address':"","attributes":[],"use":""}
            if ' is ' in x:
                atts = x.split(' is ')[1].split('{')[0].replace(' ','')
                if ',' in atts:
                    atts = atts.split(',')
                atts = checkIsList(atts)   
                for k in range(0,len(atts)):
                    lineTrack['interface'][str(lineTrack['interface']['names'][-1])]['attributes'].append(atts[k])

def queryConstructorData():
    lineTrack['constructor'] = {'lines':[],'constructorVars':{"attributes":[],"constVariables":[],"type":[],"variables":[]}}
    for i in range(0,len(lines)):
        x = eatInnerMod(lines[i],['\n','\t',' ','/',','])
        if isCurrent(x,'constructor') == True:
            addLines('constructor',i)
    if len(lineTrack['constructor']['lines'])>0:
            const = lines[getAny('constructor','lines')[-1]].split('constructor(')[1].split(')')[0].split(',')
            for i in range(0,len(const)):
                con = const[i].split(' ')
                if len(con) == 2:
                    lineTrack['constructor']['constructorVars']["attributes"].append(con[0])
                    lineTrack['constructor']['constructorVars']["constVariables"].append(con[-1])
                else: 
                    lineTrack['constructor']['constructorVars']["attributes"].append(con[0])
                    co = ''
                    for k in range(1,len(con)-1):
                        co = co + con[k]
                    lineTrack['constructor']['constructorVars']["type"].append(co)
                    lineTrack['constructor']['constructorVars']["constVariables"].append(con[-1])
    if len(lineTrack['constructor']['lines']) >0 and len(lineTrack['contract']['lines'])>0:
        constructor = stopWhenClosed(linesToString(lines[lineTrack['constructor']['lines'][-1]:]),['{','}'])
        constructor = constructor.replace(constructor.split('{')[0]+'{','')[:-1]
        constructor = eatAllMod(constructor,['\n','\t',' ','/',','])
        constructor = constructor.replace(';',';^^^***').split('^^^***')
        for c in range(0,len(lineTrack['constructor']['constructorVars']["attributes"])):
            if '[]' in lineTrack['constructor']['constructorVars']["attributes"][c]:
                higher = 1
                for i in range(0,len(constructor)):
                    ls =['interface','abstract contract']
                   
                    
                    if '=' in constructor[i]:
                        var = constructor[i].split('=')[0].replace('\n','').replace('\t','')
                        eq = constructor[i].split('=')[1].replace('\n','').replace('\t','')
                        if '0x' in eq:
                            lineTrack['constructor']['constructorVars'][str(var.replace(' ',''))] = {"address":str(eq.split('0x')[1][:len('05BFC3F8E9124eCBc762f841eC540DB3987AFE82')])}

                                
                        
                    for kk in range(0,len(ls)):
                        abstractLs = ListInString(constructor[i],lineTrack[ls[kk]]['names'])
                        if len(abstractLs) !=None:
                            print(abstractLs )
                            for k in range(0,len(abstractLs)):
                                spl = constructor[i].split(abstractLs[k]+'(')
                                print(spl)
                                lineTrack[ls[kk]][abstractLs[k]]['name'] = str(eatAllMod(spl[0].split('=')[0].replace(' ','').replace('\n','').replace('\t',''),['\n','\t',' ','/',',']))
                                lineTrack[ls[kk]][abstractLs[k]]['address'] = spl[1].split(')')[0].replace('\n','').replace('\t','')
                            if lineTrack['constructor']['constructorVars']["attributes"][c]+'[' in constructor[i]:
                                constInt = constructor[i].split(lineTrack['constructor']['constructorVars']["attributes"][c]+'[')[1].split(']')[0].replace('\n','').replace('\t','')
                                if isInt(constInt) == True:
                                    higher = getHigher(constInt,higher)
                                else:
                                    newInt = detNumInWhile(constInt,constructor,i)
                                    if newInt != None:
                                        higher = getHigher(newInt,higher)
                        
                    lineTrack['constructor']['constructorVars']["attributes"][c] = lineTrack['constructor']['constructorVars']["attributes"][c].replace('[]','['+str(higher)+']')

def isAboveZero(x):
    if len(x) <2:
        return False
    return True
def ifInLines(x,ls):
    for k in range(0,len(ls)):
        if ls[k] < len(lines):
            if lines[ls[k]] == x:
                return True
    return False
def ifBothOverZero(x,y):
    if len(x) >0 and len(y) >0:
        
        return True
    return False

def getInitialVars():
    lineTrack['variables'] = {'rndm':[],'address':{"list":[],"single":[]},'uint':{"list":[],"single":[]},'string':{"list":[],"single":[]},'bool':{"list":[],"single":[]},'bytes':{"list":[],"single":[]}}
    constVars = lines[lineTrack['contract']['lines'][-1]+1:getJustHigher(lineTrack['contract']['lines'][-1],lineTrack['function']['lines'])]
    if ifBothOverZero(lineTrack['contract']['lines'],lineTrack['constructor']['lines']) == True:
         lines[lineTrack['contract']['lines'][-1]+1:lineTrack['constructor']['lines'][-1]]
##    
        
    lsN = []
    for i in range(0,len(constVars)):
        n = constVars[i]
        if ifInLines(n,allLines) == False:
            lsN.append(n)

    constVars = lsN
    while isAboveZero(constVars) == True:
        n = eatAllMod(constVars[0],['\n','\t',' ','/',',',';'])
        
        while 'struct' in n and isAboveZero(constVars) == True:
            constVars = stopWhenClosedRemove(constVars,['{','}'])
            n = eatAllMod(constVars[0],['\n','\t',' ','/',',',';'])
        if '=' in n:
            n = n.split('=')
            nA = eatAllMod(n[0],['\n','\t',' ','/',',',';'])
            lsN = ListInString(eatAllMod(nA[0],['\n','\t',' ','/',',',';']),['address','uint','string','bool'])
            nB = eatAllMod(n[-1],['\n','\t',' ','/',',',';'])
            if len(lsN) != 0:
                 if '[' in nA:
                     lineTrack['variables'][lsN[0]]['list'].append(nA[-1])
                 else:
                     lineTrack['variables'][lsN[0]]['single'].append(nA[-1])
            else:
                lineTrack['variables']['rndm'].append(n)
        else:
            n = n.split(' ')
            lsN = []
            for i in range(0,len(n)):
                if n[i] != '':
                    lsN.append(n[i])
            inpu = False
            for k in range(0,len(lsN)):
                nn = eatAllMod(lsN[k],['\n','\t',' ','/',',',';'])
                inLs = ListInString(nn,['address','uint','string','bool'])

                if len(inLs) != 0:
                    if '[' in nn:
                        lineTrack['variables'][inLs[0]]['list'].append(n[-1])
                    else:
                        lineTrack['variables'][inLs[0]]['single'].append(n[-1])
                    inpu = True
            if inpu == False:
                if n[0] in lineTrack['abstract contract']['names']:
                    lineTrack['abstract contract'][str(n[0])]['name'] = str(n[-1])
                elif n[0] in lineTrack['interface']['names']:
                    lineTrack['interface'][str(n[0])]['name'] = str(n[-1])
                else:
                    lineTrack['variables']['rndm'].append(n)
        constVars = constVars[1:]          

def createFiles():
    input(createPath(currFileDir,name+'_deploy.js'))
    pragmaSpec = str(fileInfo['allVarsTrack']['pragma solidity']['pragma'])
    pen(reader('variables/samples/config_sample.txt').replace('^^killme^^','{\n\tversion: "'+pragmaSpec+'",\n\tsettings: {\n\t\toptimizer: {\n\tenabled: true,\n\truns: 200\n\t}\n\t}\n\t},'),createPath(currFileDir,'hardhat.config.js'))
    pen(reader('variables/samples/sample_whole_sh.txt').replace('^^killme^^', '" solc-select install '+pragmaSpec+'; solc-select use '+pragmaSpec+';  cd '+str(home)+'; npx hardhat run '+createPath(currFileDir,name+'_deploy.js')+' --network FUJI_avax;'),createPath(currFileDir,'script.sh'))
    pen(reader('variables/samples/deploy.js').replace('^^0^^','require("@nomiclabs/hardhat-etherscan");').replace('^^1^^',name),createPath(currFileDir,name+'_deploy.js'))
    chmodIt(createPath(currFileDir,name+'_deploy.js'))
def nameAndMakeAll(x,y):
    yB = y[0]
    changeGlob(x[0],yB)
    for i in range(1,len(x)):
       yB = createPath(yB,y[i])
       mkAllDir(yB)
       changeGlob(x[i],yB)
def chmodIt(x):
    st = os.stat(x)
    os.chmod(x, st.st_mode | stat.S_IEXEC)
    os.chmod(x, 0o775)
    return 'sh '+str(x)
def flatten_it():
    outFolder = '/home/bigrugz/Desktop/deployer/deploy_hist/solidity-flattener/out'
    scriptPath = createPath(currFileDir,'script.sh')
    scriptConst ="cd /home/bigrugz/Desktop/deployer/deploy_hist/solidity-flattener; node index.js "+originalFilePath
    pen(scriptConst,scriptPath)
    os.system(chmodIt(scriptPath))
    na = str(name).replace('.sol','')+'_flat'+'.sol'
    newFlat = createPath(outFolder,na)
    while na not in list_files(outFolder):
        time.sleep(5)
        print('waiting on '+na)
    pen(reader(newFlat),currFilePath)
    delFile(newFlat)   
def getPragAll():
    changeGlob('deff',js_it('[[1,1],[0,1],[-1,1],[1,-1],[1,0],[0,0]]'))
    changeGlob('att',js_it("['=<','<','>','>=','=','^']"))
    changeGlob('pragmaVers',listAllPragma())
    lineTrack['pragma solidity']['range'] = pragmaRange(lineTrack['pragma solidity']['prags'])
    for k in range(0,2):
        for i in range(0,len(['=<','<','>','>=','=','^'])):
            lineTrack['pragma solidity']['range'][k] = str(lineTrack['pragma solidity']['range'][k]).replace(['=<','<','>','>=','=','^'][i],'')
    lineTrack['pragma solidity']['pragma'] = lineTrack['pragma solidity']['range'][0]
    if len(lineTrack['pragma solidity']['prags']) !=0:
        lineTrack['pragma solidity']['pragma'] = lineTrack['pragma solidity']['range'][0]
        fileInfo['pragma'] = lineTrack['pragma solidity']['pragma'];
def changeSchedule():
    changeGlob('varisInfoOg',js_it(existWriteFileRead({"count":"0","files":[],"names":[], "adds":{},"currFilePaths": [],"currFileDirs":[],"originalFilePaths":[],"originalFileDirs":[],"deployHistDir":deployHistDir,"projectDir":projectDir,"currProjectDir":currProjectDir,"currFileDir":"","currFilePath":"","home":str(home)},varisPath)))
    changeGlob('varisInfo',{"count":"0","files":[],"names":[], "adds":{},"currFilePaths": [],"currFileDirs":[],"originalFilePaths":[],"originalFileDirs":[],"deployHistDir":varisInfoOg['deployHistDir'],"projectDir":varisInfoOg['projectDir'],"currProjectDir":varisInfoOg["currProjectDir"],"currFileDir":"","currFilePath":"","home":str(home)})
    pen(varisInfo,createPath(currProjectDir,'varis.py'))
    newLs = ["currFileDirs","originalFileDirs","originalFilePaths","files"]
    startFileAssociation()
    changeGlob('originalFilePath',displayFiles(currProjectDir))
    WholeDeploy()
    createFiles()
    copyFile(varisPath,'current') 
    for k in range(0,len(newLs)):
        for i in range(0,len(varisInfo["names"])):
            varisInfo[newLs[k]].append(varisInfoOg[newLs[k]][i] )
    return varisInfo
def moveItLsSpec(c,k,ls):
    cc = ls[c]
    kk = ls[k]
    ls[k] = cc
    ls[c] = kk
    return ls
def deleteFromLsSpec(c,ls):
    lsN = []
    for i in range(0,len(ls)):
        if i != c:
            lsN.append(ls[i])
    return lsN
def getLsOfInts(c):
    lsN = []
    for i in range(0,c):
        lsN.append(i)
    return lsN
def rearrangeDeploy():
    ans = str(createAsk(varisInfo['names'],getLsOfInts(len(varisInfo['names'])),'which file would you like to move?'))
    if ans != 'back' and ans != 'to exit':
        rem = int(ans)
        if boolAsk('are you sure you want to move '+varisInfo['names'][rem]+'?') == True:
            paths = ["currFilePaths","currFileDirs","originalFilePaths","originalFileDirs",'names']
            rem2 = int(createAsk(getLsOfInts(len(varisInfo['names'])),getLsOfInts(len(varisInfo['names'])),'which position would you like to move it to?'))
            for i in range(0,len(paths)):
                varisInfo[paths[i]] = moveItLsSpec(rem,rem2,varisInfo[paths[i]])
def removeDeploy():
    if len(varisInfo['names']) != 0:
        print(' you have no contracts to remove, pplease choose one')
        ans = createAsk(varisInfo['names'],getLsOfInts(len(varisInfo['names'])),'which file would you like to remove?')
        if ans != 'back' and ans != 'to exit':
            rem = int(ans)
            path = varisInfo['currFileDirs'][rem]
            if boolAsk('are you sure you want to remove '+varisInfo['names'][rem]+'?') == True:
                paths = ["currFilePaths","currFileDirs","originalFilePaths","originalFileDirs",'names']
                for i in range(0,len(paths)):
                    varisInfo[paths[i]] = deleteFromLsSpec(rem,varisInfo[paths[i]])
                if isFold(path) == True:
                    shutil.rmtree(path)
            saveVarisInfo()
def returnLen():
    if len(varisInfo['names']) == 0:
        input('looks like you have no contracts to remove (press enter)')
        changeGlob('last',home)
        return 'addAnother'
    if len(varisInfo['names']) == 1:
        input('looks like you have no contracts to remove (press enter)')
        ls,ls2 = ['add another contract','wrap up this deploy'],['addAnother',True]
    else:
        ls,ls2 = ['would you like to remove any of these','Rearrange Contracts','add another contract','wrap up this deploy'],['remove','rearrange','addAnother',True]
    return createAsk(ls,ls2,'this is your current deploy schedule:\n'+str(varisInfo['names'])+'\nwhat would you like to do?')

def determineEndPoint():
    keepItUp = True
    while keepItUp == True:
        allFiles = returnLen()
        if allFiles == 'rearrange':
            rearrangeDeploy()
        elif allFiles == 'remove':
            removeDeploy()
        elif allFiles == 'addAnother':
            gogo()
        elif type(allFiles) == bool:
            keepItUp = False
    copyFile(varisPath,'current')
    return allFiles
def initialize():
    global home,slash,lineTrack,sectionHeaders,allVars,lines,fileRead,allLines,last
    home,slash=home_it()
    last = home
    lines = []
    lineTrack = {}
    allLines = []
    existFoldCheck('current')
    changeGlob('variablesDir',existFoldCheck(createPath(home,'variables')))
    changeGlob('deployHistDir',existFoldCheck(createPath(home,'deployHist')))
    changeGlob('projectDir',existFoldCheck(createPath(deployHistDir,'projects')))
def createNewDeploy():
    gogo()
def getOldDeploy():
   changeGlob('currProjectDir',getFolder(projectDir))
   changeGlob('varisPath',createPath(currProjectDir,'varis.py'))
   changeGlob('varisInfo',js_it(reader(varisPath)))
   determineEndPoint()
def getCurrentDeploy():
    if isFile(createPath('current','varis.py')) == False:
        print(createPath('current','varis.py'),' not found...')
        getOldDeploy()
    changeGlob('varisPath',createPath('current','varis.py'))
    changeGlob('varisInfo',js_it(reader(varisPath)))
    determineEndPoint()
def gogo():
    changeGlob('currProjectDir',existFoldCheck(createPath(projectDir,str(input("what would you like to name the new batch?")))))
    createDepploy()
    getTheVars()
    determineEndPoint()
def createDepploy():
    changeGlob('originalFilePath',displayFiles(currProjectDir))
    if isFold('cache') == True:
        shutil.rmtree('cache')
    if isFold('artifacts') == True:
        shutil.rmtree('artifacts')
    changeGlob('originalFileDir',buildToSplitLast(originalFilePath,'/'))
    changeGlob('file',originalFilePath.split('/')[-1])
    changeGlob('name',file.split('.sol')[0])
    changeGlob('currFileDir',mkAllDir(createPath(currProjectDir,name)))
    changeGlob('currFilePath',createPath(currFileDir,file))
    changeGlob('infoFilePath',createPath(currFileDir,'info.json'))
    changeGlob('fileInfo',js_it({"projectDir":projectDir,"originalFilePath":str(originalFilePath),"originalFileDir":str(originalFileDir),"currProjectDir":str(currProjectDir),"currFilePath":str(currFilePath),"file":str(file), "name":str(name),"contract_address":"","api":"","pragma":[],"license":"","args":"", "version":"","variableNames":[],'allVarsTrack':{}}))
    changeGlob('varisPath',createPath(currProjectDir,'varis.py'))
    varisNew = {"count":"0","files":[],"names":[], "adds":{},"currFilePaths": [],"currFileDirs":[],"originalFilePaths":[],"originalFileDirs":[],"deployHistDir":deployHistDir,"projectDir":projectDir,"currProjectDir":currProjectDir,"currFileDir":"","currFilePath":"","home":str(home)}
    changeGlob('varisInfo',js_it(varisNew))
    pen(reader(originalFilePath),currFilePath)
    changeGlob('lines',readLines(currFilePath))
    sectionHeaders = ['contract','library','interface','abstract contract']
    allVars = ['contract','library','pragma solidity','import','interface','abstract contract','constructor','function','modify','SPDX-License-Identifier']
def getTheVars():
    getPragLines()
    getPragAll()
    SPDXLines()
    queryContracts()
    queryFunctions()
    queryAbstract()
    queryInterface()
    queryLibraries()
    queryConstructorData()
    getInitialVars()
    fileInfo['allVarsTrack']= lineTrack
    bulkUpdateVarisInfo()
    saveFileInfo()
    saveVarisInfo()
    createFiles()
initialize()
