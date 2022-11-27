import json
import os.path
import shutil
import json
from web3 import Web3
import os
import time
import stat
import subprocess
import parser as parser
#HomeFunctions---------------------------------------------------------------------------------------------------------------------------------------------------------------
def find_it_alph(x,k):
    i = 0
    while str(x[i]) != str(k):
        i = i + 1
    return i
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def checkIsList(x):
    if type(x) is not list:
        if ',' in str(x):
            x = str(x.split(','))
        else:
            x = [x]
    return x
def makeAllComparable(ls):
    newLs = []
    
    for i in range(0,len(ls)):
       newLs.append(ls[i].replace(' ','').lower())
    return newLs
def getLast(x,y):
    if splitNum(x,y) == 1:
        return x.split(y)[0]
    return x.split(y)[-1]
def check_str(x,y):
    c = ''
    if str(x) != str(y):
        c = y
    return c
def lineNumSpec(x,y):
    m = line_num(x,y)
    return m
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
def determineSectionMod(x,ls,k):
    n = ''
    lsNew = []
    for i in range(0,len(ls)):
        lsNew.append(k+ls[i])
    ls = lsNew
    for i in range(0,len(str(x))):
        n = n + x[i]
        match = isInList(n,ls)
        if match[0] == 1:
            return match[1][0]
        elif match[0] == 0:
            return None
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
def chmodIt(x):
    st = os.stat(x)
    os.chmod(x, st.st_mode | stat.S_IEXEC)
    os.chmod(x, 0o775)
    return 'sh '+str(x)
def createPrintList(x):
	n = []
	for i in range(0,len(x)):
		n.append(x[i])
	return n		
def countEm(x,y):
    if len(y)<len(x) or str(x) not in str(y):
        return 0
    return (len(y)-len(y.replace(str(x),''))/len(x))

def sendZeroList(i):
    ls = []
    for i in range(0,i):
        ls.append(0)
    return ls
def findIt(x,ls):
    for i in range(0,len(ls)):
        if x == ls[i]:
            return i
    return None
def jsRead(x):
    return json.loads(reader(x).replace("'",'"'))
def getHighestFromLenLs(ls):
    for i in range(0,len(ls)):
        if len(ls[i]) ==  getHighest(getLenLs(ListInString(x,checkIsList(ls)))):
            return ls[i]
    return False
def getLenLs(ls):
    lsN = []
    ls = checkIsList(ls)
    for i in range(0,len(ls)):
        lsN.append(len(str(ls[i])))
    return lsN
def getHighest(x):
	highest = 0
	for i in range(0,len(x)):
		if int(x[i]) > highest:
			highest = i
	return highest
def ifEmptyChoose(x,ls,i,k):
	if len(x) == 0:
		return ls[i]
	return x[k]
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
def stopWhenClosedI(x,ls):
    ls = checkIsList(ls)
    x = linesToString(x)
    for i in range(0,len(x)):
        y = x[0:i]
        lenLs = [countIt(y,str(ls[0])),countIt(y,str(ls[1]))]
        if lenLs[0] == lenLs[1] and lenLs[0] != 0:
            return y
    return y+'\n}'
def linesToString(x):
    x = checkIsList(x)
    nn = ''
    for i in range(0,len(x)):
        n = x[i]
        for c in range(0,len(n)):
            nn = nn + n[c]
    return nn
def isItInThere(x,y):
    if countIt(x,y) == 0:
        return False
    return True
def getFullSection(x):
    return stopWhenClosed(cont[prevK:],['{','}'])(linesToString(lines[fileInfo["allVarsTrack"][x][-1]:]),['{','}'])
def getFullLengthOfLsStr(ls):
    ls = checkIsList(ls)
    k = 0
    for i in range(0,len(ls)):
        k += len(str(ls[i]))
    return k
def findAllSections(x):
    cont = reader(x)
    ls = [cont.split('{')[0].replace(cont.split('{')[0].split('\n')[-1],'')]
    k = 0
    prevK = len(ls[0])
    while prevK != k:
        new = stopWhenClosed(cont[prevK:],['{','}'])
        k += len(new)
        ls.append(new)
        prevk = k
        for i in range(0,5):
            print()
    c = 0
    while isItInThere(cont[k-2:],'{') == True:
        new = stopWhenClosed(cont[k-2:],['{','}'])
        k += getFullLengthOfLsStr(new)
        if new != False:
            ls.append(new)
def changeGlob(x,v):
    globals()[x] = v
def ifThenCreate(x):
    if isFold(x) == False:
        mkDir(x)
    if isFile(x) == False:
        pen('',x)
def listLast(x,y):
    ls = []
    for i in range(0,len(x)):
        ls.append(getLast(x[i],slash))
    return ls
def createDep(x):
    file = getFile(x)
    addDepSched(file)
    return removeLastSpl(x,slash)
def isInPath(x,y):
    if x in os.listdir(y):
        return True
    return False
def listAllBut(x,y):
    if type(y) is not list:
        if ',' in y:
            y = splitIt(y,',')
        else:
            y = [y]
    ls = []
    for i in range(0,len(x)):
        if x[i] not in y:
            ls.append(x[i])
    return ls
def findIt(x,y):
    for i in range(0,len(y)):
        if y[i] == x:
            return i
    return False
def removeFromList(x,y):
    i = findIt(x,y)
    if i == len(y):
##        print(y)
        return y[:-1]
    ls = []
    for i in range(0,len(y)):
        if y[i] != x:
            ls.append(y[i])
    return ls
def existWriteFileRead(x,y):
    if fileExists(y) == False:
        pen(x,y)
    return reader(y).replace("'",'"')
def ifNotThenAppend(x,y):
    if x not in y:
        y.append(x)
    return y
def getHigerVar(ls):
    highest = 0
    for i in range(1,len(ls)):
        if len(str(ls[i])) > highest:
            highest = i
    return i
def ListInString(x,ls):
    ls = checkIsList(ls)
    lsN = []
    
    for i in range(0,len(ls)):
        n = ls[i]
        
        if type(n) is list:
            for k in range(0,len(n)):
                nn = n[k]
                if str(nn) in str(x):
                    lsN.append(nn)
        else:
            if str(n) in str(x):
                lsN.append(n)
    return lsN            
def stringInList(x,ls):
    ls = checkIsList(ls)
    lsN = []
    for i in range(0,len(ls)):
        if str(x) in str(ls[i]):
            lsN.append(ls[i])
    if len(lsN) != 0:
        return lsN
    return False             
def checkInLists(x,ls):
    lsN = []
    ls = checkIsList(ls)
    for i in range(0,len(ls)):
        js_ = checkIsList(ls[i])
        for k in range(0,len(js_)):
            if str(js_[k]) in str(x):
                lsN.append([js_[k],js_[k][i]])
    return lsN
def validJson(js):
    try:
        js = json.loads(str(js).replace("'",'"'))
        return True
    except:
        return False
def makeListStr(x):
    n = ''
    if ',' in str(ls):
        ls = str(ls).split(',')
    if len(ls) >1:
        for i in range(0,len(ls)):
            n = n + str(ls[i])
    return str(n)
def tryInt(x):
    try:
        i = int(x)
        return True
    except:
        return False
def removeLastSpl(x,y):
    return x.replace(y+x.split(y)[-1],'')
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
    return timeSpacing(ls,i,str(calcTimeInDays(foldTime(x,ls,i))),str(calcKb(foldSize(x,ls,i))))
def displayFiles(x):
    exit = False
    n = x
    avoid = True
    #avoid = boolAsk("avoid hidden?")
    while exit != True:
        x = x.split(' ')[0]
        foldList = os.listdir(x)
        if avoid == True:
            foldList = removeFromList(foldList,'.',0)
            ls = []
            lsGet = []
            for i in range(0,len(foldList)):
                ls.append(allSizeDays(x,foldList,i))
                lsGet.append(x)
        ask = create_ask(ls,'current Directory '+str(x)+'\nwhich file would you like to use?')
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
        ask = create_ask(foldList,'which file would you like to use?')
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
            if boolAsk(fileInputString(splitTo(n,slash,-1))) == False:
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
#CleanStrings--------------------------------------------------------------------------------------------------------------------------------------------
def eatInnerMod(x,y):
    x = str(x)
    ls = checkIsList(y)
    while len(x) >0 and x[0] in ls:
        x = x[1:]
    if len(x) == 0:
        return None
    return x
def eatOuterMod(x,y):
    x = str(x)
    ls = checkIsList(y)
    while len(x) >1 and x[-1] in ls:
        x = x[:-1]
    if len(x) == 0:
        return None
    return x
def eatOuter(x):
    x = str(x)
    ls = [' ','\t','\n']
    while len(x) >0 and x[-1] in ls:
        x = x[:-1]
    if len(x) == 0:
        return None
    return x
def eatInner(x):
    x = str(x)
    ls = [' ','\t','\n']
    while len(x) >0 and x[0] in ls:
        x = x[1:]
    if len(x) == 0:
        return None
    return x
def isConnected(x,ls):
    nLs = []
    n = ''
    for i in range(0,len(ls)):
        n = n +str(ls)[i]
        if x in ls:
            if len(n) == int(2):
                nLs[-1] = ls[findIt(n,ls)]
            else:
                nLs.append(ls[findIt(n,ls)])
        else:
            n = ''
    return nLs
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
#copyFunctions----------------------------------------------------------------------------------------------------
def copyAll(x,y):
    list = os.listdir(x)
    for i in range(0,len(list)):
        ifThenCreate(pathMk(y,list[i]))
        if isFile(pathMk(x,list[i])) == True:
            copyFile(pathMk(x,list[i]),y)
def copyFile(x,y):
	pen(reader(x),pathMk(y,getLast(x,slash)))
def copyIt(x,y):
    k = pathMk(x,getLast(x,slash))
#ReadWrite---------------------------------------------------------------------------------
def reader_C(file):
    with open(file, 'r',encoding='utf-8-sig') as f:
        text = read()

        return text
def reader_B(file):
    with open(file, 'r',encoding='UTF-8') as f:
        text = f.read()

        return text
def reader(file):
    with open(file, 'r') as f:
        text = f.read()
        return text
def pen_B(paper, place):
    
    with open(place, 'w',encoding='UTF-8') as f:
        f.write(str(paper))
        f.close()
        return
def pen(paper, place):
    with open(place, 'w') as f:
        f.write(str(paper))
        f.close()
        return
#splitters--------------------------------------------------------------------------------------------------------------------------
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
    change_glob('slash',slash)
    change_glob('home',curr)
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
#JsonCreation----------------------------------------------------------------------------------------
def get_c(x):
        c = ','
        if int(x) == int(0):
                c = ''
        return c
def wrap_up(x,y,z):
        w = str(z)[:-1]+get_c(len(z))+'"'+str(x)+'":"'+str(y)+'"'+str(z)[-1]
        return js_it(w)
def create_wrap_ls(x,y):
        z = json.loads('{}')
        for i in range(0,len(x)):
                z = wrap_up(x[i],y[i],z)
        return z
def js_wrap(x):
    return js_it('{'+str(x)+'}')
def js_qu(x):
    return '"'+str(x)+'"'
def addLsJs(x,y):
    return js_it(str(x)[:-1]+get_c(len(x))+'"'+str(y)+'":[]'+'}')
def addJsJs(x,y):
    return js_it(str(x)[:-1]+get_c(len(x))+'"'+str(y)+'":{}'+'}')
def make_js(x,y):
    return js_qu(x)+':'+js_qu(y)
def add_js(x,y):
    return js_it(str(x)[:-1]+get_c(len(x))+str(y)+'}')
def do_js(x,z):
    for i in range(0,len(x)):
        y = make_js(x[i],z)
        if i == 0:
            w = js_wrap(y)
        else:
            w = add_js(w,y)
    return js_it(str(w).replace("'[]'","[]"))
def get_c_tf(i):
    if i == 0:
        return True
    return False
#------------------------------------------------------------------------------------------------
def getOld():
    return getFolder(pathMk(home,'deploy_hist/projects'))
def change_glob(x,v):
    globals()[x] = v

def slashFind(x):
    slash = '//'
    if '//' not in str(x):
        slash = '/'
    change_glob('slash',slash)
    return slash
def fileInputString(x):
    return "is "+str(x)+" the file you would like to choose?"

def clearLast(x,y):
    if str(x)[-1] == slash:
        return x[:-1]
    return x
def ifInFirst(x,y):
    if str(y) == str(x)[0]:
        return True
    return False
def splitIt(x,y):
    if str(y) in str(x):
        return x.split(y)
    return False
def splitNum(x,spl):
    return len(x.split(spl))
def removeLast(x,y):
    if x.replace(x[0:-len(y)],'') == y:
        return x[0:-len(y)]
    return x
def removeLastSpl(x,y):
    return x.replace(y+x.split(y)[-1],'')
def getLast(x,y):
    if splitNum(x,y) == 1:
        return x.split(y)[0]
    return x.split(y)[-1]
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
def get_name():
    return os.path.basename(__file__)

def check_str(x,y):
    c = ''
    if str(x) != str(y):
        c = y
    return c

def get_c(i):
    c = ''
    if c != 0:
        c = ',\n'
    return c
def add_many_str(x,k,z):
    y = ''
    for i in range(0,k):
        y = y + x
    return y+z
def get_words(x,y):
    if type(y) is not list:
        y = [y]
    z = ''
    while x[0] not in list_var_in_str(x[0],y):
        z = z + str(x[0])
        x = x[1:]
    return z
def del_space_in(x,y):
    if type(y) is not list:
        y = [y]
    
    for i in range(0,len(y)):
        res = list_var_in_str(x,['[','{','('])
        if y[i] in res:
            x = x.replace(y[i] + ' ',y[i])
        res = list_var_in_str(x,[']','}',')'])
        if y[i] in res:
            x = x.replace(' '+y[i],y[i])
    return x
def del_space_front(x,y):
    if type(y) is not list:
        y = [y]
    for i in range(0,len(x)):
        
        if list_var_in_str(x[0],y) in y:
            x = x[1:]
        else:
            return x
def get_words_and_junk(x,y):
    if type(y) is not list:
        y = [y]
    z = ''
    
    for i in range(0,len(y)):
        if list_var_in_str(x,z) not in y:
            z = z + str(x[0])
            x = x[1:]
    return z,x
def get_blank_bracs(x):
    n = []
    m = list()
    for i in range(0,len(x)):
        m.append(n)
    
    return m
def js_it(x):
    return json.loads(str(x).replace('{,','{').replace(',}','}').replace('[,','[').replace(',]',']').replace("'",'"'))

def line_num(x,filename):
    m = []
    with open(filename) as myFile:
        for num, line in enumerate(myFile, 1):
            if x in line:
                m.append(num-1)
    return m

def new_line_it(x):
    y = ''
    for i in range(0,len(x)):
        c = ''
        if get_c_tf(i) == False:
            c = '\n'
        y =y+c+ str(x[i])
    return y
def try_it(x,y):
    try:
        n = x[y]
        return True
    except:
        return False
def find_lowest(x):
    x.sort()
    if try_it(x,0) == True:
        return x[0]
    else:
        return False
def find_highest(x):
    x.sort()
    if try_it(x,-1) == True:
        return x[-1]
    else:
        return False
def range_list(x):
    return [find_lowest(x),find_highest(x)]
def exists_make(x,y):
    if exists(y) == False:
        pen(x,y)
        return x
    else:
        return reader_C(y)
def exists(x):
    try:
        x = reader(x)
        return True
    except:
        return False
def count_lines(x):
    if exists(x) == False:
        pen('',x)
    count = 1
    with open(r''+str(x)+'', 'r') as fp:
        for count, line in enumerate(fp):
            pass
    return count
def fake_line(x,l,k):
    y = ''
    for i in range(l,k):
        y = y + '\n'
    return y
def read_lines(x):
    a = open(x, "r")
    rd = a.readlines()
    a.close()
    return rd
def write_lines(x,y):
    a = open(x, "w")
    a.writelines(y)
    a.close()
def add_lines(x,line):
    n = count_lines(x)
    fake = ''
    if line > n:
        fake = fake_line(x,n+1,line+1)
    pen(reader(x)+fake,x)
    add_lines(x,y+1)
    list_of_lines = read_lines(x)
    list_of_lines[y] = z
    write_lines(x,list_of_lines)
    

def comb_ls(x,y):
    for i in range(0,len(y)):
        x.append(y[i])
    return x
def int_chk(x):
    try:
        n =int(x)
        return True
    except:
        return False
def list_check(x):
    if type(x) is str:
        return js_it(l),len_x
    if type(x) is list:
        return x,len(x)
    else:
         return x,
def ls_to_str(x):
    new = ''
    for i in range(0,len(x)):
        new = new + str(x[i])
    return new
def chop_lines(x,y):
    w = []
    for i in range(0,len(x)):
        a = x[i]
        if i+1 < len(x):
            z = x[i+1]
            n = ls_to_str(y[int(a):int(z)])
            w.append(n)
        else:
            n = ls_to_str(y[int(a):])
            w.append(n)
    return w

def list_it(x):
    x,k = list_check(x)
    n = ''
    
    for i in range(0,k):
        n = n + x[i]
    return n
def add_it(x,y):
    return int(x) + int(y)
def add_str(x,y):
    return str(x)+str(y)
def str_kill(x,y):
    y = ''
    x,i = list_check(x)
    st = []
    for l in range(0,len(y)):
        if type(y[l]) is list:
            yy = [],[]
            for ll in range(0,len(y_a)):
                st.append(y[l][ll])
                yy[ll].append(y[l][ll])
                y = go
        else:
            st.append(y[l])
        if list_var_in_str(x,z):
            print('bo')
    z = list_var_in_str(x,y)  
    z = add_str(yy,x[i])
    i = add_it(i,1)
    return z,i
def str_go(x,y,z):
    for i in range(y):
        x.append(y[i])
    x,y = list_check(x)
    res = list_var_in_str(x,z)
    if res in y:
        return res,1
    elif res in x:
        return res,-1
    else:
        return False
def check_it(x,y):
    if type(y) is not list:
        y = [y]
    for i in range(0,len(y)):
        res=list_var_in_str(x,y)
        if len(res) != 0:
            return res
    return False
def create_ls_bracs(x,k):
    w = []
    y = '[]'
    for ii in range(0,k):
        z = []
        for i in range(0,x):
            z.append(y)
        w.append(js_it(z))
    return str(w).replace('"','').replace("'",'')
def var_str(x):
    if type(x) is not list:
        x = [x]
    for i in range(0,len(x)):
        #var = 710
        #variable_name = [k for k, v in locals().items() if v == 710][0] 
        #print("Your variable name is " + variable_name)
        exec("%s = %s" % (x[i],'z'))
        z = x[i]
        exec("%s = %s" % (z,x[i]))
def create_blanks(x):
    y = ''
    for i in range(0,x):
        y = y + ' '
    return y
def timer(x):
    return int(x) + 1
def remove_end(x):
    return str(x).replace(str(y)+str(slash).split(str(y))[-1],'')
def get_end(x):
    return str(x).split(str(slash))[-1]
def copy_it(x,y):
    pen(reader(x),y)

def get_lins_is(file):
    lines = read_lines(file)
    var = ['pragma solidity','}','contract','library','function','constructor','abstract','interface']
    z = 'is'
    ls_a,ls_b = do_js(var,[]),json.loads('{"is":[]}')
    line = read_lines(file)
    for i in range(0,len(var)):
        n = var[i]
        ls_a[n] = line_num(n,file)
        for k in range(0,len(ls_a[n])):
            x = lines[ls_a[n][k]]
            while str(x)[:len(n)] in list_var_in_str(str(x)[:len(n)],['\t',' ','\n']):
                x = x[1:]
            if x[:len(n)] == n:
                m = ls_a[n]
                if z in str(x):
                    ne = x.split(z)[1].replace(', ',',').replace(' ,',',').split(',')
                    for k_1 in range(0,len(ne)):
                        while ne[k_1][0] == ' ':
                            ne[k_1] = ne[k_1][1:]
                        while ne[k_1][-1] == ' ':
                            ne[k_1] = ne[k_1][:-1]
                        ne[k_1] = ne[k_1].split(' ')[0]
                        if str(ne[k_1]) not in ls_b['is']:
                            ls_b = str(str(ls_b)[:-1] + ','+str(make_js(ne[k_1],ls_a[n][k]))+'}').replace('{,','{')
                            ls_b = js_it(ls_b)
                            ls_b['is'].append(ne[k_1])
                        if int(ls_b[ne[k_1]]) < int(ls_a[n][k]):
                            ls_b[ne[k_1]] = int(ls_a[n][k])
    return ls_b,ls_a,lines
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def splitVarOutAndEndOrSpace(x,y):
    if x+' ' in y:
        x = x+' '
    n = y.split(str(x))[1]
    if ' ' in n:
        n = n.split(' ')[0]
    return n
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
            ls_pr = js_it(str(str(ls_pr)[:-1] + ','+str(make_js(pr[i],n)+'}')).replace('{,','{'))
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

#--------------------------------------------------------------------------------------------------------------------------------------------------------
def detNumInWhile(x,string,k):
    lenget = k
    for i in range(0,len(string)):
        found = ListInString(string[lenget],['for','while'])
        if len(found)>0:
            nn = ''
            n = str(stopWhenClosed(linesToString(string[lenget:]),['(',')'])).replace(' ','').replace('\n','').replace('\t','')
            found = ListInString(n,['=<','<','>','>=','=','^'])
            nowInt = n.split(findFirstStr(n,found))
            nowIntA = nowInt[1]
            now = linesToString(nowInt)
            nowIntB = now.split(findFirstStr(now,found))
            nowAll = nowInt[1].split(findFirstStr(nowInt[1],found))
            while ListInString(n[0],found) == None:
                n = n[1:]
                
	  
            now = linesToString(n.split(found))
            for k in range(0,len(now)):
               nowIntB = int(n[1].split(type)[1])
               nowInt = nowIntB - nowIntA
               if '=' not in str(type):
                   nowInt -= 1
                   return nowInt
               if int_chk(nowIntA) != False:
                   type = ListInString(n[1],['=<','<','>','>=','=','^'])[0]
                   nowIntB = int(n[1].split(type)[1])  
                   nowInt = nowIntB - nowIntA
                   if '=' not in str(type):
                       nowInt -= 1
                   return nowInt
        lenget -=1

def getAllAttributes(lines):
    titleFound = False
    theContract = ''
    nAll = ''
    n = ''
    pragmaDirs,ends,sections,pragmas,licenses,pragmas,spdxId,nAll,title,theContract = createPath(home,'variables/pragma'),[],[],[],[],[],[],'','',''
    for i in range(0,len(lines)):
        n = lines[i]
        while n == '\n' or len(n) == 0 and i != 0:
            i +=1
            n = lines[i]
        if titleFound == False:
            found = []
            for k in range(0,len(getSectHeaders())):
                if getSectHeaders()[k] == n[:len(getSectHeaders()[k])]:
                    found.append(getSectHeaders()[k])
            if len(found) > 0:
                highest = [len(found[0]),found[0]]
                for k in range(1,len(found)):
                    if len(found[k])>highest[0]:
                        highest = [len(found[k]),found[k]]
                secHead = highest[1]
                title = safeSplit(safeSplit(n,str(secHead)+' ',1),' ',0)
                fileInfo["allVarsTrack"][secHead]["names"].append(title)
                appendSectHeaders(title,js,"names")
                pragFold = pragmaVerSplit(pragmas[-1])
                pragmaFold = createPath(pragmaDirs,pragFold)
                existFoldCheck(pragmaFold)
                pragmaSpec = createPath(pragmaFold,pragmas[-1])
                existFoldCheck(pragmaSpec)
                headFold = createPath(pragmaSpec,secHead)
                existFoldCheck(headFold)
                sectFold = createPath(headFold,title+'.sol')
                existFileCheck(sectFold)
                titleFound = True
        if eatOuter(n) != None:
            nAll = nAll + n
            theContract = theContract + n
        if titleFound == True and len(n) != 0:
            if str(n)[0] == '}':
                ends.append(i)
                pen(nAll,sectFold)
                sections.append(nAll)
                nAll = ''
                titleFound = False
    pen(theContract,currFilePath)
    flatten_it(originalPath,flatFold,nameSol)
def getConstructor():
    const = reader(createPath(currFileDir,'constructor.sol'))
    for i in range(0,len(allVars)):
        fileInfo["allVarsTrack"][allVars[i]]['lines'] = lineNumSpec(allVars[i],currFilePath)
    constVars = const.split('constructor(')[1].split(')')[0].split(',')
    for i in range(0,len(constVars)):
        constVar = constVars[i].split(' ')
        for k in range(0,len(constVar)):
            if k == int(0):
                fileInfo["allVarsTrack"]["args"]["attributes"].append(constVar[k])
            elif k == len(constVar)-int(1):
                fileInfo["allVarsTrack"]["args"]["constVariables"].append(constVar[k])
            elif k != int(0) and k != len(constVar)-int(1):
                fileInfo["allVarsTrack"]["args"]["type"].append(constVar[k])
        constPieces = buildFromSplitFirst(const,'{').split(';')
        for k in range(0,len(constPieces)):
            pieces = ListInString(constPieces[i],fileInfo["allVarsTrack"]["args"]["constVariables"])
            for i in range(0,len(pieces)):
                fileInfo["allVarsTrack"]["args"]["attributes"][findIt(pieces[i],fileInfo["allVarsTrack"]["args"]["constVariables"])]

    
    constInterface = const.replace(const.split(')')[0],'').split('{')[0]
    lsInt = checkInLists(constInterface,[fileInfo["allVarsTrack"]["interface"]["names"],fileInfo["allVarsTrack"]["contract"]["names"],fileInfo["allVarsTrack"]["abstract contract"]["names"],fileInfo["allVarsTrack"]["library"]["names"]])
    for i in range(0,len(lsInt)):
        fileInfo["sectionTags"]["utilized"] = addLsJs(fileInfo["sectionTags"]["utilized"],lsInt[i][2])
        n = constInterface.split(lsInt[i])[1]
        nn = ''
        while n[0] not in ['{']:
            nn =nn + n[0] 
            if n == ['(']:
                attVars = constInterface.split(lsInt[i])[1].replace(nn,'').split(')')[0]
                for k in range(0,len(n)):
                    nn =nn + n[0]
                    n = n[1:]
                if ',' in attVars:
                    atts = attVars.split(',')
                    for k in range(0,len(atts)):
                        fileInfo["sectionTags"]["utilized"][lsInt[i][2]].append(atts[k])
                else:
                    fileInfo["sectionTags"]["utilized"][lsInt[i][2]].append(attVars)
            n = n[1:]
    constPieces = buildFromSplitFirst(const,'{').split(';')
    higher = int(0)
    for i in range(0,len(fileInfo["allVarsTrack"]["args"]["attributes"])):
        if '[]' in fileInfo["allVarsTrack"]["args"]["attributes"][i]:
            for k in range(0,len(constPieces)):
                piece = constPieces[k]
                count = countEm(fileInfo["allVarsTrack"]["args"]["constVariables"][i],piece)
                for c in range(0,int(count)):
                    newConst = constPieces[k].split(fileInfo["allVarsTrack"]["args"]["constVariables"][i]+'[')[1].split(']')[0]
                    if (int_chk(newConst[0])) == True:
                        if int(higher) < int(newConst[0]):
                                    higher = newConst[0]
                    else:
                    	if detNumInWhile(newConst[0],constPieces,i) != None:
                    		if higher < int(detNumInWhile(newConst[0],constPieces,i)):
                    			higher = int(detNumInWhile(newConst[0],constPieces,i))
            
            fileInfo["allVarsTrack"]["args"]["attributes"][i] = fileInfo["allVarsTrack"]["args"]["attributes"][i].replace('[]','['+str(higher)+']')
            return 'done'
def checkMultipleListsString(x,ls,nameList):
    for i in range(0,len(names)):
        for k in range(0,len(ls)):
            if ls[k] in names:
                return names[i],ls[k+1]
def addJsLsAllVars(js,ls):
    for i in range(0,len(ls)):
        if ls[i] not in js:
            js = addLsJs(js,ls[i])
    return js
def replaceItClear(x,ls):
    for i in range(0,len(ls)):
        x = x.replace(ls[i],' ')
    return x
def intClearLs(ls):
    lsN = []
    for i in range(0,len(ls)):
        if int_chk(ls[i]) == False:
            lsN.append(ls[i])
    return lsN
def ifNotAddJs(x,js):
    if x not in js:
        js = addLsJs(js,x)
    return js
def ifNotJsAddJs(x,js):
    if x not in js:
        js = addJsJs(js,x)
    return js
def cleanListUp(x):
    x = replaceItClear(x,['\t','\n',"'",'"','\\','{','}','=','false','true', 'days','(',')','None','true','false',','])
    y = ''
    lsN = []
    for i in range(0,len(x)):
        if x[i] != '':
            y = y + x[i]
    
    return y.split(' ')
def addJsJs(x,y):
    return json.loads(str(str(x)[:-1]+get_c(len(x))+'"'+str(y)+'":{}'+'}').replace("'",'"'))
def defINotJsAddJs(x,js):
     return ifNotJsAddJs(js,x)
def isWordInList(ls,x,ls2):
    lsN = []
    for k in range(0,len(ls)):
        if ls[k] in x:
            x2 = cleanListUp(x)
            for i in range(0,len(ls2)):
                if x2[0-i] in ls2:
                    return  k,x2[findIt(ls2[0-i],x2)+1],ls2[0-i]
def getAllVariables(lines):
    lsN = []
    vars = linesToString(lines[fileInfo['allVarsTrack']['contract']['lines'][-1]:fileInfo['allVarsTrack']['constructor']['lines'][-1]]).split(';')
    
    tagCheckLsLs = fileInfo['allVarsTrack']['contract']["names"],fileInfo['allVarsTrack']['interface']["names"],fileInfo['allVarsTrack']['abstract contract']["names"],fileInfo['allVarsTrack']['library']["names"]
    tagCheckName = ['contract','interface','abstract contract','library']

    for i in range(0,len(vars)):
        line = vars[i]

        for k in range(0,len(tagCheckName)):
            LsLs = fileInfo['allVarsTrack'][tagCheckName[k]]["names"]
            for ck in range(0,len(LsLs)):
                if LsLs[ck] in line:
                    for c in range(0,len(fileInfo['allVarsTrack']['variables']["names"])):
                        if fileInfo['allVarsTrack']['variables']["names"][c] in line:
                            input(str(LsLs)+line.split(' ')[-1].split(';')[0])
                            #for i in range(0,len(tagCheckLsLs[k])):
                            #    if len(fileInfo['allVarsTrack'][LsLs[ck]]["use"])<len(tagCheckLsLs[k]):
                            #        fileInfo['allVarsTrack'][LsLs[ck]]["use"].append([])
                            #if lsTag[1] not in fileInfo['allVarsTrack'][lsTag[2]]["use"][int(lsTag[0])-1]:
                            #    fileInfo['allVarsTrack'][LsLs[ck]]["use"][int(lsTag[0])].append(lsTag[1]) 

def getSPDX(lines):
    spdx= {"1":"No License (None)","2":"The Unlicense (Unlicense)","3":"MIT License (MIT)","4":"GNU General Public License v2.0 (GNU GPLv2)","5":"GNU General Public License v3.0 (GNU GPLv3)","6":"GNU Lesser General Public License v2.1 (GNU LGPLv2.1)","7":"GNU Lesser General Public License v3.0 (GNU LGPLv3)","8":"BSD 2-clause &quot;Simplified&quot; license (BSD-2-Clause)","9":"BSD 3-clause &quot;New&quot; Or &quot;Revised&quot; license (BSD-3-Clause)","10":"Mozilla Public License 2.0 (MPL-2.0)","11":"Open Software License 3.0 (OSL-3.0)","12":"Apache 2.0 (Apache-2.0)","13":"GNU Affero General Public License (GNU AGPLv3)","14":"Business Source License (BSL 1.1)"}
    spdxId = []
    for i in range(1,len(spdx)+1):
        n = safeSplit(safeSplit(spdx[str(i)],' (',1),')',0)
        spdxId.append(n)
    top,lin = makeAllComparable(['// SPDX-License-Identifier:',lines[int(fileInfo["allVarsTrack"]['SPDX-License-Identifier']["lines"][0])]])
    spdLs = makeAllComparable(spdxId)
    label = eatOuter(lin.split(top)[1])
    for i in range(0,len(label)):
        found = stringInList(label[:i],spdLs)
        if found != 0:
            perc = i
    lic = determineSection(label,spdLs)
    if lic != None:
        fileInfo["allVarsTrack"]["SPDX-License-Identifier"]["names"].append(lic)
def getThePrags(lines):
    for i in range(0,len(fileInfo["allVarsTrack"][allVars][getSectHeaders()[-1]]["lines"])):
        fileInfo["allVarsTrack"][getSectHeaders()[-2]]["names"].append(safeSplit(safeSplit(lines[int(fileInfo["allVarsTrack"][getSectHeaders()[-2]]["lines"][i])],'pragma solidity'+' ',1),';',0))
    pragmaRange(fileInfo["allVarsTrack"][getSectHeaders()[-1]]["names"])
#sectHeaders-------------------------------------------------------------------------------------
def changeSectHead(i):
    vStuff = fileInfo["allVarsTrack"][allVars][i]
    if i > len(vStuff):
        return vStuff[i+1]
    return None
def getSectHead(i):
    vStuff = fileInfo["allVarsTrack"][allVars[i]]
    if i > len(vStuff):
        return vStuff[i]
    return None

def getModLines(st):
    return fileInfo["allVarsTrack"][st]["lines"]
def getModAny(st):
    return fileInfo["allVarsTrack"][st[0]][st[1]]
def getModAnySect(st,i):
    return fileInfo["allVarsTrack"][changeSectHead(i)][st]
def getSectAndLine(i):
    if sect == False:
        return False
    return sect["lines"]
def getSectHeaders():
    return allVars
def appendSectHeaders(x,js,st):
    if js != None:
        if x not in fileInfo["allVarsTrack"][js][st]:
            fileInfo["allVarsTrack"][js][st].append(x)
def updateSectHeaders(x,js,st):
    if js != None:
        fileInfo["allVarsTrack"][js][st] = x
def countEm(x,y):
    if len(y)<len(x) or str(x) not in str(y):
        return 0
    return (len(y)-len(y.replace(str(x),''))/len(x))
def listsInString(x,ls):
    lsN = []
    for i in range(0,len(ls)):
        if countEm(ls[i],x) != 0:
            lsN.append(ls[i])
    return lsN
def sectInLines(ls,k):
    lsS = getSectHeaders()
    for i in range(0,len(lsS)):
        if lsS[i] in ls:
            appendSectHeaders(k,lsS[i],"lines")
def listsInLines(ls,lines):
    for i in range(0,len(lines)):
        n = lines[i]
        if len(n) != 0:
            if n[0] == '}':
                fileInfo["allVarsTrack"]["ends"].append(i)
        sectInLines(listsInString(n,ls),i)
def readLines(x):
    return reader(x).replace('\n','\n^^^^^^^^^^^^**********').split('^^^^^^^^^^^^**********')
def SectHeaderLineFun(x):
    listsInLines(getSectHeaders(),readLines(x))
def getLineNums():
    SectHeaderLineFun(currFilePath)


#FlattenIt---------------------------------------------------------------------------------------
def flatten_it():
    outFolder = '/home/bigrugz/Desktop/deployer/deploy_hist/solidity-flattener/out'
    scriptPath = createPath(currFileDir,'script.sh')
    scriptConst ="cd /home/bigrugz/Desktop/deployer/deploy_hist/solidity-flattener; node index.js "+currFilePath
    pen(scriptConst,home+'/newtest.txt')
    pen(scriptConst,scriptPath)
    os.system(chmodIt(scriptPath))
    na = str(name).replace('.sol','')+'_flat'+'.sol'
    newFlat = createPath(outFolder,na)
    while na not in list_files(outFolder):
        time.sleep(5)
        print('waiting on '+na)
    pen(reader(newFlat),currFilePath)
    delFile(newFlat)        
#getPragma--------------------------------------------------------------------------------------------------
def getPragFromLines():
     pragmas.append(safeSplit(safeSplit(n,toppers[1]+' ',1),';',0))
#HomeStuff-------------------------------------------------------------------------------------
def getPathFromHome(x):
    a = str('/home/bigrugz/Desktop/savem/newDeploy/variables/newDepSamples').split(slash)
    return createPath(home,x.split(slash)[1])
def createPathFromHome(x,y):
    return getPathFromHome(createPath(x,y))
def check_sum(x):
    return Web3.toChecksumAddress(str(x))
def rem_file(x):
        os.remove(x) 
def rem_var():
        if exists('variables/vars.txt') == True:
                rem_file('variables/vars.txt')
#HOME-----------------------------------------------------------------------------------------------------------
def getOld():
    try:
        x = "displayFiles"#getFolder(pathMk(home,'deploy_hist/projects'))
        return x
    except:
        return slash
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

def sortLs(ls):
    lsN = []
    lower = [ls[0],0]
    for k in range(0,len(ls)):
        for i in range(0,len(ls)):
            if ls[i] not in lsN and ls[i] < lower[0]:
                lower = [ls[i],i]
        lsN.append(ls[lower[1]])
    return lsN
def getJusthigher(k,ls):
    for i in range(0,len(ls)):
        if ls[i]>k:
            return ls[i]
def getJustlower(k,ls):
    lsBef = 0
    for i in range(1,len(ls)):
        if ls[1]>k:
            return lsBef
        lsBef = i-1
    return lsBef
def getName(x):
    return fileInfo['allVarsTrack'][x]['names']
def getLines(x):
    return fileInfo['allVarsTrack'][x]['lines']
def getInitPrags():
    ends = fileInfo['allVarsTrack']["ends"]
    prags = getLines('pragma solidity')
    pragNames = getName('pragma solidity')
    for i in range(0,len(prags)):
        n = lines[prags[i]]
        if len(n) != 0 and len(prags) > len(pragNames):
            pragNames.append(safeSplit(safeSplit(n,'pragma solidity'+' ',1),';',0))
        mkAllDir([pragmaDir,pragNames[-1].split('.')[1].split('.')[0],str(pragNames[-1])])
    changeGlob('deff',js_it('[[1,1],[0,1],[-1,1],[1,-1],[1,0],[0,0]]'))
    changeGlob('att',js_it("['=<','<','>','>=','=','^']"))
    changeGlob('pragmaVers',listAllPragma())
    fileInfo['pragma'] = pragmaRange(pragNames)
def getInitSections():
    for i in range(0,(len(secionsHeaders["sectHeads"]))):
        head = getSectHeaders()[i]
        lineTags = getLines(head)
        for k in range(0,len(lineTags)):
            lineStart = lineTags[k]
            pragNow = getName('pragma solidity')[getJustlower(lineStart,getLines('pragma solidity'))]
            pragDir = mkAllDir([mkAllPath([pragmaDir,pragNow.split('.')[1].split('.')[0],pragNow]),head])
            if lines[lineStart][:len(head)] == head:
                headNames =fileInfo['allVarsTrack'][head]['names']
                now = lines[lineStart].split(head)[1]
                while now[0] == ' ':
                    now = now[1:]
                headNames.append(now.split(' ')[0])
                pen('//'+str(head)+' '+now.split(' ')[0]+'\npragma solidity '+pragNow+';\n'+stopWhenClosedI(lines[lineStart:],['{','}']),createPath(pragDir,now.split(' ')[0])+'.sol')
def getConstData():
    const = stopWhenClosed(linesToString(lines[fileInfo['allVarsTrack']['constructor']['lines'][-1]:]),['{','}'])
    pen(linesToString(const),constructorPath)
    const = const.split(';')
    for i in range(0,len(const)):
        n = const[i]
        heads = secionsHeaders["sectHeads"]
        fileInfo["allVarsTrack"]["variables"]["names"].append(n.split(' ')[-1].replace('\t','').replace(' ','').replace('\n','').replace(';','').replace('{','').replace('}',''))

def getPreConstData():
    const = lines[fileInfo['allVarsTrack']['contract']['lines'][-1]:fileInfo['allVarsTrack']['constructor']['lines'][-1]]
    pen(linesToString(const),constructorPath)
    for i in range(0,len(const)):
        n = const[i]
        heads = secionsHeaders["sectHeads"]
        fileInfo["allVarsTrack"]["variables"]["names"].append(n.split(' ')[-1].replace('\t','').replace(' ','').replace('\n','').replace(';',''))
    
def getAllVars():
    const = lines[fileInfo['allVarsTrack']['contract']['lines'][-1]:fileInfo['allVarsTrack']['constructor']['lines'][-1]]
    inters = ['interface','contract','abstract contract','library']
    for c in range(0,len(inters)):
        abstract = fileInfo['allVarsTrack'][inters[int(c)]]['names']
        for k in range(0,len(abstract)):
            fileInfo['allVarsTrack'][inters[int(c)]]['use'].append([])
            for i in range(0,len(const)):
                n = const[i].replace('\t','').replace(' ','').replace('\n','')
                if len(n) >= len(abstract[k]):
                    if n[:len(abstract[k])] == abstract[k]:
                         fileInfo['allVarsTrack'][inters[int(c)]]['use'][k].append(const[i].split(' ')[-1].replace('\t','').replace(' ','').replace('\n','').replace(';',''))
    allCont = lines[getLines('constructor')[-1]:]
    for i in range(0,len(allCont)):
        n = allCont[i]
        if '.' in n:
            print(n.split('.'))

def createFiles():
    #bash = reader(bashSamplePath).replace('^^killme^^','cd ~/Desktop/contract_station/contract_station_test; solc-select install '+str(fileInfo["pragma"][1])+';solc-select use '+str(fileInfo["pragma"][1])+'; npx hardhat run '+str(deployScript.replace(home,'')))
    #pen(bash,mkAllPath([contractFolder,fileInfo['name'],'script.sh']))
    pen(reader(bashSamplePath).replace('^^killme^^','{\n\tversion: "'+str(fileInfo["pragma"])+'",\n\tsettings: {\n\t\toptimizer: {\n\tenabled: true,\n\truns: 200\n\t}\n\t}\n\t},'),configPath)   
def nameAndMakeAll(x,y):
    yB = y[0]
    changeGlob(x[0],yB)
    for i in range(1,len(x)):
       yB = createPath(yB,y[i])
       mkAllDir(yB)
       changeGlob(x[i],yB)                
def createPaths():
    changeGlob('pathAsk',currFileDir)
    changeGlob("buildUpPath",getPath('buildup.txt'))
    changeGlob("configPath",getPath('hardhat.config.js'))
    changeGlob('constructorPath',getPath('constructor.sol'))
    changeGlob('bashPath',getPath('script.sh'))
    changeGlob("deployScriptPath",getPath(str(name)+'_deploy.js'))
    changeGlob("infoFile",getPath('info.json'))
    changeGlob("currFilePath",getPath(file))
    changeGlob("infoFilePath",getPath('info.json'))
def StartDeploy():
        changeGlob('file',originalFilePath.split('/')[-1])
        changeGlob('name',file.split('.sol')[0])
        changeGlob('originalFileDir',originalFilePath.replace('/'+file,''))
        changeGlob('currFileDir',mkAllDir([currProjectDir,name]))
        changeGlob('currFilePath',createPath(currFileDir,file))
        nameAndMakeAll(['contractFolder','currFileDir'],[currProjectDir,name])
        changeGlob('currFilePath',createPath(currFileDir,file))
        createPaths()
        changeGlob('fileInfo',js_it({"projectDir":projectDir,"originalFilePath":str(originalFilePath),"originalFileDir":str(originalFileDir),"currProjectDir":str(currProjectDir),"currFilePath":str(currFilePath),"file":str(file), "name":str(name),"contract_address":"","api":"","pragma":[],"license":"","args":"", "version":"","variableNames":[],
                    'allVarsTrack':{
                    "args":{"attributes":[],"type":[],"constVariables":[],"constVars":{"names":[]}},'ends':[],'library':{"names":[],"lines":[],"use":[]},
                        'pragma solidity':{"names":[],"lines":[],"use":[]},
                        'import':{"names":[],"lines":[],"use":[]},
                        'interface':{"names":[],"lines":[],"use":[]},
                        'abstract contract':{"names":[],"lines":[],"use":[]},'function':{"names":[],"lines":[],"use":[]},
                        'modify':{"names":[],"lines":[],"use":[]},
                        'SPDX-License-Identifier':{"names":[],"lines":[],"use":[]},
                        'utilized':{"names":[],"lines":[],"use":[]},
                        'for':{"names":[],"lines":[],"use":[]},
                        'while':{"names":[],"lines":[],"use":[]},
                        "variables":{"names":[],"lines":[],"use":[]},
                        "constructor":{"names":[],"lines":[],"use":[]},
                        "contract":{"names":[],"lines":[],"use":[]}}}))
        saveFileInfo()
        createFiles()
        bulkUpdateVarisInfo()
        changeGlob('lines',readLines(originalFilePath))
def startFileAssociation():
    home,slash = home_it()
    changeGlob('home',os.getcwd())
    changeGlob('slash',slashFind(home))
    nameAndMakeAll(['home','currentFold'],[home,'current'])
    nameAndMakeAll(['home','variablesDir'],[home,'variables'])
    changeGlob('sampleDir',createPath(variablesDir,'samples'))
    changeGlob('pragmaDir',createPath(variablesDir,'pragmas'))
    changeGlob('pragmaVersionsPath',createPath(variablesDir,'prags.py'))
    changeGlob('bashSamplePath',createPath(sampleDir,'bash.sh'))
    changeGlob('configSamplePath',createPath(sampleDir,'configSample.txt'))
    nameAndMakeAll(['home','deployHistDir','projectDir','currProjectDir'],[home,'deployHist','projects',input("what would you like to name the new batch?")])#input("what would you like to name the new batch?"))])
    changeGlob('varisPath',createPath(currProjectDir,'varis.py'))
    changeGlob('allVars',['contract','library','pragma solidity','import','interface','abstract contract','constructor','function','modify','pragma solidity','SPDX-License-Identifier'])
    changeGlob('secionsHeaders',{"sectHeads":['interface','contract','abstract contract','library'],"subArgs":['constructor','function','modify'],"sub_tag":['modify','function','constructor'],"toppers":['SPDX-License-Identifier:','pragma solidity']})
    changeGlob('varisInfo',js_it(existWriteFileRead({"count":"0","files":[],"names":[], "adds":{},"currFilePaths": [],"currFileDirs":[],"originalFilePaths":[],"originalFileDirs":[],"deployHistDir":deployHistDir,"projectDir":projectDir,"currProjectDir":currProjectDir,"currFileDir":"","currFilePath":"","home":str(home)},varisPath)))
    changeGlob('allFiles',False)
    changeGlob('last',currProjectDir)
    if len(varisInfo['originalFilePaths']) !=0:
        changeGlob('last',varisInfo['originalFilePaths'][-1])
def getPragAll():
    changeGlob('deff',js_it('[[1,1],[0,1],[-1,1],[1,-1],[1,0],[0,0]]'))
    changeGlob('att',js_it("['=<','<','>','>=','=','^']"))
    changeGlob('pragmaVers',listAllPragma())
    fileInfo['pragma'] = fileInfo['allVarsTrack']['pragma solidity']['prags'][0]
def WholeDeploy():
    StartDeploy()
    createPaths()
    input(currFilePath)
    changeGlob('lines',[])
    fileInfo['allVarsTrack'],lines = parser.getVars(originalFilePath)
    getPragAll()
    lsN = ['//SPDX-License-Identifier: '+fileInfo['allVarsTrack']['SPDX-License-Identifier']['lic'][-1]+'\n']
    for i in range(1,len(lines)):
        if len(parser.eatAllMod(lines[i],['','\t',' ','\n'])) != 0 and i not in fileInfo['allVarsTrack']['SPDX-License-Identifier']['lines']:
            lsN.append(lines[i])
    pen(linesToString(lsN),currFilePath)
    flatten_it()
    fileInfo['allVarsTrack'],lines = parser.getVars(currFilePath)
    bulkUpdateVarisInfo()
    saveFileInfo()
def startIt():
    startFileAssociation()
    allFiles = False
    while allFiles != True:
        changeGlob('originalFilePath',displayFiles(currProjectDir))
        WholeDeploy()
        allFiles = boolAsk("is "+str(varisInfo['names'])+" the whole current deploy?")
    createFiles()
    copyFile(varisPath,currentFold)
    return 
def changeSchedule():
        changeGlob('varisInfoOg',js_it(existWriteFileRead({"count":"0","files":[],"names":[], "adds":{},"currFilePaths": [],"currFileDirs":[],"originalFilePaths":[],"originalFileDirs":[],"deployHistDir":deployHistDir,"projectDir":projectDir,"currProjectDir":currProjectDir,"currFileDir":"","currFilePath":"","home":str(home)},varisPath)))
        changeGlob('varisInfo',{"count":"0","files":[],"names":[], "adds":{},"currFilePaths": [],"currFileDirs":[],"originalFilePaths":[],"originalFileDirs":[],"deployHistDir":varisInfoOg['deployHistDir'],"projectDir":varisInfoOg['projectDir'],"currProjectDir":varisInfoOg["currProjectDir"],"currFileDir":"","currFilePath":"","home":str(home)})
        pen(varisInfo,createPath(currProjectDir,'varis.py'))
        newLs = ["currFileDirs","originalFileDirs","originalFilePaths","files"]
        startFileAssociation()
        changeGlob('originalFilePath',displayFiles(currProjectDir))
        WholeDeploy()
        createFiles()
        copyFile(varisPath,currentFold) 
        for k in range(0,len(newLs)):
            for i in range(0,len(varisInfo["names"])):
                varisInfo[newLs[k]].append(varisInfoOg[newLs[k]][i] )
        return varisInfo
#----DOINGWORK-----------------------------------
