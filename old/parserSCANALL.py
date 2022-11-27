import json
import os.path
import shutil
import json
from web3 import Web3
import os
import time
import stat
import subprocess
from eth_abi import encode_abi
def const_it(x):
    print(x)
    return read_hex(encode_abi([x[0]],[x[1]]))
def read_hex(hb):
    h = "".join(["{:02X}".format(b) for b in hb])
    return h
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
    stringsLs = ["files","names","currFileDirs","currFilePaths","originalFilePaths","originalFileDirs","currProjectDir","currFileDir","currFilePath"]
    varsLs = [file,fileName,currFileDir,currFilePath,originalFilePath,originalFileDir,currProjectDir,currFileDir,currFilePath]
    for i in range(0,len(varsLs)):
        updateVarisInfo(stringsLs[i],varsLs[i])
         
    saveFileInfo()
    saveVarisInfo()
def updateVarisInfo(string,x):
    if string in varisInfo:
        js = varisInfo[string]
        if type(js) is list:
            varisInfo[string] = ThenAppend(varisInfo[string],x)
        else:
            varisInfo[string] = x
            
    else:
        print(str(string),' not in varisInfo')
def appendIt(js,x):
    if x not in js:
        js.append(x)
    return js
def jsAddIt(js,x):
    js = x
    return js
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
def mains():
    global scanners,net,ch_id,main,file,w3,last_api,c_k,hashs_js,expo,dec,network,scan_num
    hashs_js = ""
    last_api = [0,0]
    main = {
            "avax_test":{"net":"https://api.avax-test.network/ext/bc/C/rpc","chain":"43113","main_tok":"AVAX","scanners":"api-testnet.snowtrace.io"},
            "polygon":{"net":"https://polygon-rpc.com/","chain":"137","main_tok":"MATIC","scanners":"api.polygonscan.com"},
            "ethereum":{"net":"https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161","chain":"1","main_tok":"ETH","scanners":"api.etherscan.io"},
            "cronos_test":{"net":"https://cronos-testnet-3.crypto.org:8545/","chain":"338","main_tok":"TCRO","scanners":"api.cronoscan.com"},
            "optimism":{"net":"https://kovan.optimism.io","chain":"69","main_tok":"OPT","scanners":"api-kovan.etherscan.io"},
            "binance":{"net":"https://bsc-dataseed.binance.org/","chain":"56","main_tok":"bsc","scanners":"api.bscscan.com"}
            }
    scan = ["avax_test","polygon","ethereum","cronos_test","optimism","binance"]
    var_names = ['scanners','net','ch_id','main_tok','file','w3','network']
    file = 'variables/vars.txt'
    
    network = create_ask(scan,'network')
    all = main[network]
    return  all["scanners"],all["net"],all["chain"],all["main_tok"],Web3(Web3.HTTPProvider(all["net"]))
    

def keys():
    scanners,net,ch_id,main_tok,w3  = mains()
    if scanners == 'bscscan.com':
        key = 'JYVRVFFC32H2ZSKDY1JZKNY7XV1Y5MCJHM'
    elif scanners == 'polygonscan.com':
        key = 'S6X6NY29X4ARWRVSIZJTG1PJS4IG86B3WJ'
    elif scanners == 'ftmscan.com':
        key = 'WU2C3NZAQC9QT299HU5BF7P8QCYX39W327'
    elif scanners == 'moonbeam.moonscan.io':
        key = '5WVKC1UGJ3JMWQZQAT8471ZXT3UJVFDF4N'
    else:
        key = 'G8N1PH6Y9X7U6FH3HB4D3RNNSTRCQNIEHG'
    return key

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
    if isFile(x) == False:
        pen('',x)
    return x
def existFileMakeSpec(x,y):
    if isFile(y) == False:
        pen(x,y)
    return reader(y)
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
    x = eatOuterMod(x,[slash,' ',''])
    y = eatInnerMod(x,[slash,' ',''])
    return x+slash+y
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
def  list_files(x):
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
            lsN.append(ls[i])
    return lsN
def listFiles(x):
    lsN = []
    ls = os.listdir(x)
    for i in range(0,len(ls)):
        if isFile(ls[i]) == True:
            lsN.append(ls[i])
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
    print(x)
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
    print(x)
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
        print(x,y)
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
    ask = str(input(x)).lower()
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
    lines = x.split('\n')
    for i in range(0,len(lines)):
        lines[i] = eatOuterMod(lines[i],['\n','\t',' ','']).replace('\n','')
        if lines[i] not in ['\n',' \n','',' ','\t']  and len(str(eatAllMod(lines[i],['\n','\t',' ','/',';','']))) != 0:
            lsN.append(lines[i]+'\n')
    return lsN

def readLines(x):
    lsN = []
    lines = reader(x).split('\n')
    for i in range(0,len(lines)):
        lines[i] = eatOuterMod(lines[i],['\n','\t',' ','']).replace('\n','')
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
    if len(x) >0:
        while x[0] in ls and ifOverZero(x) == True:
            x = eatInnerMod(x,ls)
        while x[-1] in ls and ifOverZero(x) == True:
            x = eatOuterMod(x,ls)
    return x
def ifOverZero(x):
    if len(x) >1:
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
def strInListRev(x,ls):
    if ifOverZero(x) == True:
        if x[-1] in ls:
            return x[:-1]
    return False

def eatOuterMod(x,ls):
    if strInListRev(x,ls) != False:
        x = strInListRev(x,ls)
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
    return ''
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
            return ls[i]
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
                if '.length' in nowIntB:
                    na = nowIntB.split('.length')[0]
                    nam = lineTrack['contract']['names'][-1]
                    pVars = lineTrack['contract'][nam]['constructor']['constVariables']
                    if na in pVars:
                        nowIntB = lineTrack['contract'][nam]['constructor']['attributes'][findIt(na,pVars)].split('[')[1].split(']')[0]
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
    lsN,k,z = [''],0,''
    for i in range(0,len(str(x))):
        z = z+x[i]
        if isIn(z,y) == True:
            lsN[k] = z
        else:
            z,k,lsN = returnZK(z,k,lsN,'')
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
def compareList(x,ls,lsOg):
    ls,lsN = checkLsAndGetNew(ls)
    for i in range(0,len(ls)):
        same = isSame(x,ls[i])
        lsN.append(getPercSame(same[1],same[0]))
    return lsOg[getHighestFloatSpec(lsN)]
def returnMostAbundant(ls,lsNone):
    newJs = {"names":[]}
    for i in range(0,len(ls)):
        if ls[i] not in newJs:
            newJs[ls[i]] = 1
            newJs["names"].append(ls[i])
        else:
            newJs[ls[i]] = int(newJs[ls[i]]) + int(1)
    higher = [0,0]
    for i in range(0,len(newJs["names"])):
        if int(newJs[newJs["names"][i]]) > int(higher[1]):
            higher = [i,newJs[newJs["names"][i]]]
    return newJs[newJs["names"][higher[0]]]
def returnMostAbundant2(ls,lsNone):
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
    return eatOuterMod(x,[slash,' ','','\t','\n'])+slash+eatInnerMod(y,[slash,' ','','\t','\n'])
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
    if len(ls) == 1:
        if countIt(ls[0],'.') == 2:
            if ls[0][0] == '=':
                if len(ListInString(ls[0].replace('=',''),att)) == 0:
                    return [ls[0].replace('=',''),ls[0].replace('=','')]
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
    if isFile(x) == True:
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
    if isFold(y) == True:
        pen(reader(x),createPath(y,getLast(x,slash)))
        return
    pen(reader(x),y)
def copyIt(x,y):
    k = pathMk(x,getLast(x,slash))
def addLines(st,i):
    lineTrack[st]['lines'].append(i)
    allLines.append(i)
def stringInLists(x,lss):
    lss,lsN= checkLsAndGetNew(lss)
    for i in range(0,len(lss)):
        lssN = checkIsList(lss[i])
        for k in range(0,len(lssN)):
            if x in lssN:
                lsN.append(findIt(x,lssN))
    return lsN
def stringInList(x,ls):
    if ls == None:
        return False
    ls,lsN = checkLsAndGetNew(ls)
    if len(ls) == 0:
        return False
    for i in range(0,len(ls)):
        if x == ls[i]:
            return True
    return False
def ThenAppend(js,x):
    if x not in js:
        js.append(x)
    return js
def getNames(st):
    return lineTrack[st]['names']
def getAnys(st,st2):
    return lineTrack[st][st2]
def getAtts(x):
    atts = x.split(' is ')[1].split('{')[0].replace(' ','')
    if ',' in atts:
        atts = atts.split(',')
    return atts
def getAttsFind(var):
    input(var)
    lsVar = [var]
    track = json.loads(reader('variables/pragmas/tracker.json').replace("'",'"'))
    pra = pragmaVerSplit(getCurrPrag())
    if pra in track:
        track[pra]
        prag = getCurrPrag()
        if prag in track[pra]:
            nam = track[pra][prag]["names"]
            for k in range(0,len(nam)):
                input(nam)
                if var in track[pra][prag][nam[k]]:
                    new = reader(track[pra][prag][nam[k]][var])+'\n'+lines[currLine]
                    lines[currLine] = reader(track[pra][prag][nam[k]][var])+'\n'+lines[currLine]
                    input(track[pra][prag][nam[k]][var])
                    changeGlob('lines',readLinesSpec(linesToString(lines)))
                    changeGlob('lineTrack',{})
                    changeGlob('currLine',0)
                    allLinesParse()
        else:
            input('you have called an association that has not yet beem declared: '+str(ls[i]))
def findAtts(js,ls):
    names = ['contract','abstract contract','interface']
    ls,lsN= checkLsAndGetNew(ls)
    for i in range(0,len(ls)):
        lsN.append(False)
    for i in range(0,len(names)):
        name = names[i]
        for k in range(0,len(ls)):
            if stringInList(ls[k],getNames(name)) == True:
                if name not in js:
                    js[name] = []
                js[name] = ThenAppend(js[name],ls[k])
                lsN[k] = True
    return lsN
def checkAtts(js,ls):
    if ls == None:
        return 
    lsN = findAtts(js,ls)
    for i in range(0,len(lsN)):
        if lsN[i] == False:
            importCheck(ls[i],getAtts(lines[currLine]))
            
    return js
def importCheck(name,st):
    st = checkIsList(st)
    pra = pragmaVerSplit(getCurrPrag())
    verPath = createPath('variables/pragmas/',str(pra))
    ifFoldCreate(verPath)
    pragFold = os.listdir(verPath)
    for i in range(0,len(pragFold)):
        namePath = createPath(verPath,pragFold[i])
        namefold = os.listdir(namePath)
        for c in range(0,len(namefold)):
            contextPath = createPath(namePath,namefold[c])
            contextfold = os.listdir(contextPath)
            for k in range(0,len(st)):
                if st[k]+'.sol' in contextfold and st[k]+'.sol' not in os.listdir(imports):
                    print(st[k],st)
                    finalPath = createPath(contextPath,st[k]+'.sol')
                    pen(reader(finalPath),createPath(imports,st[k]+'.sol'))
def getCurrPrag():
    if len(getAny('pragma solidity','prags'))>0:
        return getAny('pragma solidity','prags')[-1]
    else:
        return '^0.8.0'
def trackEm(ls):
    ls = checkIsList(ls)
    if fileExists('variables/pragmas/tracker.json') == False:
        pen({},'variables/pragmas/tracker.json')
    track = json.loads(reader('variables/pragmas/tracker.json').replace("'",'"'))
    if ls[0] not in track:
        track[ls[0]] = {}
    if ls[1] not in track[ls[0]]:
        track[ls[0]][ls[1]] = {"names":[]}
    if ls[2] not in track[ls[0]][ls[1]]:
        track[ls[0]][ls[1]]["names"] = ThenAppend(track[ls[0]][ls[1]]["names"],ls[2])
        track[ls[0]][ls[1]][ls[2]] = {}
    if ls[3] not in track[ls[0]][ls[1]][ls[2]]:
        track[ls[0]][ls[1]][ls[2]][ls[3]] = ls[4]
    pen(track,'variables/pragmas/tracker.json')
def saveSect(st,i):
    lic = 'None'
    if len(getAnys('SPDX-License-Identifier',"License")) != 0:
        lic = getAnys('SPDX-License-Identifier',"License")[-1]
    pragma = getCurrPrag()
    if len(getAnys('pragma solidity','prags')) != 0:
        pragma = getAnys('pragma solidity','prags')[-1]
    title = getNames(st)[-1]+'.sol'
    pragFold = pragmaVerSplit(pragma)
    pragmaFold = createPath('variables/pragmas',pragFold)
    existFoldCheck(pragmaFold)
    pragmaSpec = createPath(pragmaFold,pragma).replace(slash+' ',slash+'')
    existFoldCheck(pragmaSpec)
    headFold = createPath(pragmaSpec,st)
    existFoldCheck(headFold)
    sectFold = createPath(headFold,title)
    existFileCheck(sectFold)
    trackEm([pragFold,pragma,st,getNames(st)[-1],sectFold])
    
    pen('//SPDX-License-Identifier: '+lic+'\npragma solidity '+pragma+';\n'+stopWhenClosed(linesToString(lines[i:]),['{','}']),sectFold)
    pen(reader(sectFold),createPath(imports,title))
def sendIfs(x,i,ignore):
    changeGlob('currLine',i)
    heads = ['SPDX-License-Identifier','pragma solidity','library','using','contract','abstract contract','interface','constructor','function']
    saveLst = ['library','interface','contract','library','abstract contract']
    if ignore != True:
        for k in range(0,len(heads)):
            if isCurrent(x,heads[k]) == True:
                if heads[k] in saveLst:
                    changeGlob('allCurr',heads[k])
                changeGlob('current',heads[k])
                if current == 'SPDX-License-Identifier':
                    SPDXLines(x,i)
                elif current == 'pragma solidity':
                    getPragLines(x,i)
                elif current == 'library':
                    queryLibraries(x,i)
                elif current == 'using':
                    queryLibrariesUse(x,i)
                elif current == 'contract':
                    queryContracts(x,i)
                elif current == 'abstract contract':
                    queryAbstract(x,i)
                elif current == 'interface':
                    queryInterface(x,i)
                elif current == 'constructor':
                    queryConstructorData(x,i)
                elif current == 'function':
                    queryFunctions(x,i)
                if current in saveLst:
                    saveSect(current,i)
def allLinesParse():
    lineTrack['SPDX-License-Identifier'] = {"lines":[],"Licenses":[],"License":[],"lic":""}
    lineTrack['pragma solidity'] = {"lines":[],"range":[],"prags":[],"pragma":""}
    lineTrack['function'] = {"lines":[],'names':[]}
    lineTrack['library'] = {"lines":[],'names':[]}
    lineTrack['contract'] = {"lines":[],'names':[]}
    lineTrack['abstract contract'] = {"lines":[],'names':[]}
    lineTrack['interface'] = {"lines":[],'names':[]}
    lineTrack['constructor'] = {"lines":[],'names':[]}
    pen({},createPath(currFileDir,'Functions.json'))
    for i in range(0,len(lines)):
        ignore = False
        if eatAllMod(lines[i],['\n','\t',' '])[:len('//')] == '//' and 'SPDX-License-Identifier' not in lines[i]:
            ignore = True
        x = eatAllMod(lines[i],['\n','\t',' ','/'])
        sendIfs(x,i,ignore)
def safeSplit2(x,y,k):
    if y in x:
        x = x.split(y)
        if len(x) >= int(k):
            return x[k]
    return x
def SPDXLines(x,i):
    addLines('SPDX-License-Identifier',i)
    lineTrack['SPDX-License-Identifier']["License"].append(x.split('SPDX-License-Identifier:')[1].replace(' ','').replace('\n',''))
def getPragLines(x,i):
    addLines('pragma solidity',i)
    lineTrack['pragma solidity']["prags"].append(x.split('pragma solidity ')[1].split(';')[0].replace(' ',''))
def queryFunctions(x,i):
    addLines('function',i)
    funcDoc = createPath(currFileDir,'Functions.json')
    if fileExists(funcDoc) == False:
        pen({},funcDoc)
    funcVars = json.loads(reader(funcDoc).replace("'",'"'))
    name = safeSplit2(x,'(',0)
    name = safeSplit2(name,' ',1)
    vis = ListInString(x,syntax["visibility"])
    mod = ListInString(x,syntax["modifiers"])
    if vis == None or len(vis) == 0:
        vis = ['public']
    if mod == None or len(mod) == 0:
        mod = ['view']
    mod,vis = mod[0],vis[0]
    if vis not in funcVars:
        funcVars[vis]={}
    if mod not in funcVars[vis]:
        funcVars[vis][mod] = []
    if 'names' not in funcVars:
        funcVars['names'] = []
    if name not in funcVars[vis][mod]:
        funcVars[vis][mod].append(name)
        funcVars['names'].append(name)
        lineTrack['function']["names"] = [name]
    pen(funcVars,funcDoc)
def queryLibrariesUse(x,i):
        name = str(x.split('using ')[1].split(' ')[0])
        use = str(x.split(' ')[-1].split(';')[0])
        lineTrack['library']['names'] = ThenAppend(lineTrack['library']['names'],name)
        if str(name) not in lineTrack['library']:
            lineTrack['library'][name] = {'attributes':{},"address":"","undeclared":"1"}
            importCheck('library',name)
        if 'library' not in lineTrack[allCurr][lineTrack[allCurr]['names'][-1]]['attributes']:
            lineTrack[allCurr][lineTrack[allCurr]['names'][-1]]['attributes']['library'] = []
        lineTrack[allCurr][lineTrack[allCurr]['names'][-1]]['attributes']['library'].append(name)
def queryLibraries(x,i):
    if 'using ' in x:
        queryLibrariesUse(x,i)
        return 
    addLines('library',i)
    name = str(x.split('library ')[1].split(' ')[0])
    lineTrack['library']['names'] = ThenAppend(lineTrack['library']['names'],name)
    if str(name) not in lineTrack['library']:
        lineTrack['library'][name] = {'attributes':{},"address":"","undeclared":"0"}
        importCheck('library',name)
    lineTrack['library'][name]["undeclared"] = "0" 
def queryContracts(x,i):
    addLines('contract',i)
    lineTrack['contract']['names'].append(eatOuterMod(x,['\n','\t',' ','/',';']).split(' ')[1])
    if str(lineTrack['contract']['names'][-1]) not in lineTrack['contract']:
        lineTrack['contract'][str(getAny('contract','names')[-1])] = {'address':"","attributes":{},"undeclared":"1"}
        if str(lineTrack['contract']['names'][-1]) != fileName:
            importCheck('contract',str(lineTrack['contract']['names'][-1]))
    if ' is ' in x:
        lineTrack['contract'][str(getAny('contract','names')[-1])]['attributes'] = checkAtts(lineTrack['contract'][str(getAny('contract','names')[-1])]['attributes'],getAtts(x))
def queryAbstract(x,i):
    addLines('abstract contract',i)
    lineTrack['abstract contract']['names'].append(eatOuterMod(x,['\n','\t',' ','/',';']).split(' ')[2])
    if str(lineTrack['abstract contract']['names'][-1]) not in lineTrack['abstract contract']:
        lineTrack['abstract contract'][str(lineTrack['abstract contract']['names'][-1])] = {'address':"","attributes":{},"name":""}
        importCheck('abstract contract',str(lineTrack['abstract contract']['names'][-1]))
    if ' is ' in x:
        lineTrack['abstract contract'][str(lineTrack['abstract contract']['names'][-1])]['attributes'] = checkAtts(lineTrack['abstract contract'][str(lineTrack['abstract contract']['names'][-1])]['attributes'],checkIsList(getAtts(x))) 
def queryInterface(x,i):
    addLines('interface',i)
    lineTrack['interface']['names'].append(eatOuterMod(x,['\n','\t',' ','/',';']).split(' ')[1])
    if str(lineTrack['interface']['names'][-1]) not in lineTrack['interface']:
        lineTrack['interface'][str(lineTrack['interface']['names'][-1])] = {'address':"","attributes":{},"undeclared":"1"}
        importCheck('interface',str(lineTrack['interface']['names'][-1]))
    if ' is ' in x:
        lineTrack['interface'][str(lineTrack['interface']['names'][-1])]['attributes'] = checkAtts(lineTrack['interface'][str(lineTrack['interface']['names'][-1])]['attributes'],checkIsList(getAtts(x)))
def queryConstructorData(x,i):
    addLines('constructor',i)
    if len(getAny('contract','names')) != 0:
        contractName = getAny('contract','names')[-1]
        
        lineTrack['contract'][contractName]["constructor"] = {"attributes":[],"constVariables":[],"type":[],"variables":[],"deployerVars":{},"input":[]}
        if len(lineTrack['constructor']['lines'])>0:
            if 'constructor(' in lines[getAny('constructor','lines')[-1]]:
                const = lines[getAny('constructor','lines')[-1]].split('constructor(')[1].split(')')[0].split(',')
                for i in range(0,len(const)):
                    con = const[i].split(' ')
                    if len(con) == 2:
                        lineTrack['contract'][contractName]["constructor"]["attributes"].append(con[0])
                        lineTrack['contract'][contractName]["constructor"]["constVariables"].append(con[-1])
                    else: 
                        lineTrack['contract'][contractName]["constructor"]["attributes"].append(con[0])
                        co = ''
                        for k in range(1,len(con)-1):
                            co = co + con[k]
                        lineTrack['contract'][contractName]["constructor"]["type"].append(co)
                        lineTrack['contract'][contractName]["constructor"]["constVariables"].append(con[-1])
        if len(lineTrack['constructor']['lines']) >0 and len(lineTrack['contract']['lines'])>0:
            constructor = stopWhenClosed(linesToString(lines[lineTrack['constructor']['lines'][-1]:]),['{','}'])
            constructor = constructor.replace(constructor.split('{')[0]+'{','')[:-1]
            constructor = eatAllMod(constructor,['\n','\t',' ','/',','])
            constructor = constructor.replace(';',';^^^***').split('^^^***')
            for c in range(0,len(lineTrack['contract'][contractName]["constructor"]["attributes"])):
                if '[]' in lineTrack['contract'][contractName]["constructor"]["attributes"][c]:
                    higher = lineTrack['contract'][contractName]["constructor"]["attributes"][c].split('[')[1].split(']')[0]
                    if len(higher) == 0:
                        higher = 1
                    for i in range(0,len(constructor)):
                        ls =['interface','abstract contract']
                        if '=' in constructor[i]:
                            var = constructor[i].split('=')[0].replace('\n','').replace('\t','')
                            eq = constructor[i].split('=')[1].replace('\n','').replace('\t','')
                            if '0x' in eq:
                                lineTrack['contract'][contractName]["constructor"][str(var.replace(' ',''))] = {"address":str(eq.split('0x')[1][:len('')])}
                        for kk in range(0,len(ls)):
                            abstractLs = ListInString(constructor[i],lineTrack[ls[kk]]['names'])
                            if len(abstractLs) !=None:
                                for k in range(0,len(abstractLs)):
                                    spl = constructor[i].split(abstractLs[k]+'(')
                                    lineTrack[ls[kk]][abstractLs[k]]['name'] = str(eatAllMod(spl[0].split('=')[0].replace(' ','').replace('\n','').replace('\t',''),['\n','\t',' ','/',',']))
        
                                    if len(spl) >1:
                                        spll = spl[1].split(')')[0].replace('\n','').replace('\t','')
                                    else:
                                        spll = spl[0].split(')')[0].replace('\n','').replace('\t','')
                                    lineTrack[ls[kk]][abstractLs[k]]['address'] = spll
                        if lineTrack['contract'][contractName]["constructor"]["constVariables"][c]+'[' in constructor[i]:
                            constInt = constructor[i].split(lineTrack['contract'][contractName]["constructor"]["constVariables"][c]+'[')[1].split(']')[0].replace('\n','').replace('\t','')
                            if isInt(constInt) == True:
                                higher = getHigher(constInt,higher)
                            else:
                                newInt = detNumInWhile(constInt,constructor,i)
                                if newInt != None:
                                    higher = getHigher(newInt,higher)
                            
                        lineTrack['contract'][contractName]["constructor"]["attributes"][c] = lineTrack['contract'][contractName]["constructor"]["attributes"][c].split('[')[0]+'['+str(higher)+']'
    if ' is ' in x:
        if str(lineTrack['contract']['names'][-1]) not in lineTrack['contract']:
            lineTrack['constructor'][str(lineTrack['constructor']['lines'][-1])] = {"attributes":{}}
        lineTrack['constructor'][str(lineTrack['constructor']['lines'][-1])]['attributes'] = checkAtts(lineTrack['constructor'][str(lineTrack['constructor']['lines'][-1])]['attributes'],checkIsList(getAtts(x))) 
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
def getFullSPDX():
    spdx= {"0":"No License (None)","1":"The Unlicense (Unlicense)","2":"MIT License (MIT)","3":"GNU General Public License v2.0 (GNU GPLv2)","4":"GNU General Public License v3.0 (GNU GPLv3)","5":"GNU Lesser General Public License v2.1 (GNU LGPLv2.1)","6":"GNU Lesser General Public License v3.0 (GNU LGPLv3)","7":"BSD 2-clause &quot;Simplified&quot; license (BSD-2-Clause)","8":"BSD 3-clause &quot;New&quot; Or &quot;Revised&quot; license (BSD-3-Clause)","9":"Mozilla Public License 2.0 (MPL-2.0)","10":"Open Software License 3.0 (OSL-3.0)","11":"Apache 2.0 (Apache-2.0)","12":"GNU Affero General Public License (GNU AGPLv3)","13":"Business Source License (BSL 1.1)"}
    spdxIdOg = []
    for i in range(0,len(spdx)):
        n = safeSplit(safeSplit(spdx[str(i)],' (',1),')',0)
        spdxIdOg.append(n)
    spdxId = makeAllComparable(spdxIdOg)
    spdxLines = getAny('SPDX-License-Identifier','lines')
    for i in range(0,len(spdxLines)):
        comp = compareList(makeAllComparable(eatAllMod(lines[spdxLines[i]].split('SPDX-License-Identifier:')[1],['\n','\t',' ','/',',']))[0],spdxId,spdxIdOg)
        if comp != None:
            lineTrack['SPDX-License-Identifier']['Licenses'].append(comp)    
    for i in range(0,len(getAny('SPDX-License-Identifier','License'))):
        lic = returnMostAbundant(getAny('SPDX-License-Identifier','Licenses'),['',None,False,True])
        lineTrack['SPDX-License-Identifier']['lic'] = lic
        fileInfo['license'] = lic
def getInitialVars():
   
    lineTrack['variables'] = {'rndm':[],'address':{"list":[],"single":[]},'uint':{"list":[],"single":[]},'string':{"list":[],"single":[]},'bool':{"list":[],"single":[]},'bytes':{"list":[],"single":[]}}
    constVars = lines[lineTrack['contract']['lines'][-1]+1:getJustHigher(lineTrack['contract']['lines'][-1],lineTrack['function']['lines'])]
    if ifBothOverZero(lineTrack['contract']['lines'],lineTrack['constructor']['lines']) == True:
         lines[lineTrack['contract']['lines'][-1]+1:lineTrack['constructor']['lines'][-1]]   
    lsN = []
    for i in range(0,len(constVars)):
        n = constVars[i]
        if ifInLines(n,allLines) == False:
            lsN.append(n)
    constVars = lsN
    typesVars = ['address','uint','string','bool']
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
                importCheck(['interface','abstract contract','library','contract'],n)
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
                    importCheck(['interface','abstract contract','library','contract'],n)
        constVars = constVars[1:]
        pen(lineTrack,'lineTrack.txt')
def dec_ast(x,dec):
    og_dec = dec
    if '*' in str(x):
        x = x.split('*')[0]
        if '.' in str(x):
            bef = x.split('.')[0]
            y = x.split('.')[1]
            while y[-1] == '0':
                y = y[:-1]
            de = len(y)
            dec = int(dec) - int(de)
            y = str(bef) + str(y)
            while y[0] == '0':
                y = y[1:]
            x = y
        x =  int(float(int(x))*float(str('1e'+str(int(dec)))))
        dec = og_dec
    return int(x)
def ifNotBlank(x,y):
    if y != '':
        return y
    return x
def constAsk(x,y,cont):
    cont = ifNotBlank(y,cont)
    if 'uint' in str(x):
        end = ' (input will be multiplied by 10^'+str(int(dec))+' if * is added to the end of the input): '
    elif 'address' in str(x):
        end = '(if youd like to input a DEFAULTINPUT  *)'
    ch = boolAsk(''+"is "+str(x) +' '+str(y)+' supposed to be '+str(cont)+'?')
    if ch == True:
        return cont
    while ch == False:
        change = input('please input what youd like to change it to:'+end+'\n')
        if 'uint' in str(x):
            change = dec_ast(change,dec)
        elif change == '*':
            change ='0x0000000000000000000000000000000000000000'
        elif 'address' in str(x) and change == '*':
            change =  '*^^'+str(boolAsk(getList(varisInfo['files'],varisInfo['count'],change)))+'^^*'
        ch2 = boolAsk('are you sure you want to change '+str(x) +' '+str(cont)+' to '+str(change)+'?')
        if ch2 == True:
            return change
def ifAble(x,k):
    if len(x) > k+1:
        return x[k]
    return ''
def isUnisEven(na):
    n = lineTrack['contract'][na]["constructor"]["attributes"]
    units = lineTrack['contract'][na]["constructor"]["input"]
    lsConsts= json.loads(existWriteFileRead(units,createPath(currFileDir,'constVals.sol')).replace("'",'"'))
    lsVerify = []
    if len(n) > len(units):
        for i in range(len(units),len(n)):
            if '[' in n[i]:
                lsN = []
                for c in range(0,int(n[i].split('[')[1].split(']')[0])):
                    lsN.append(n[i].split('[')[0]+'['+str(c+1)+']')
                    lineTrack['contract'][na]["constructor"]["input"].append(constAsk(n[i].split('[')[0]+'['+str(c+1)+']',n[i].split('[')[0],ifAble(lsConsts,c)))
                    lsVerify.append(const_it([n[i].split('[')[0],lineTrack['contract'][na]["constructor"]["input"][-1]]))
                lineTrack['contract'][na]["constructor"]["deployerVars"][n[i]] =lsN
    fileInfo["args"] = lsVerify
    fileInfo["api"] = keys()
def makeConstructors():
    contName = getAny('contract','names')[-1]
    isUnisEven(contName)
def createFiles():
    pragmaSpec = str(fileInfo['allVarsTrack']['pragma solidity']['pragma'])
    pen(reader('variables/samples/config_sample.txt').replace('^^killme^^','{\n\tversion: "'+pragmaSpec+'",\n\tsettings: {\n\t\toptimizer: {\n\tenabled: true,\n\truns: 200\n\t}\n\t}\n\t},'),createPath(currFileDir,'hardhat.config.js'))
    pen(reader('variables/samples/sample_whole_sh.txt').replace('^^killme^^', '" solc-select install '+pragmaSpec+'; solc-select use '+pragmaSpec+';  cd '+str(home)+'; npx hardhat run '+createPath(currFileDir,fileName+'_deploy.js')+' --network FUJI_avax;'),createPath(currFileDir,'script.sh'))
    pen(lineTrack['contract'][getAny('contract','names')[-1]]["constructor"]['input'],createPath(currFileDir,'constVals.sol'))
    pen(reader('variables/samples/deploy.js').replace('^^0^^','require("@nomiclabs/hardhat-etherscan");').replace('^^1^^',fileName).replace('^^2^^','').replace('^^3^^',str(lineTrack['contract'][getAny('contract','names')[-1]]["constructor"]['input'])),createPath(currFileDir,fileName+'_deploy.js'))
    
    chmodIt(createPath(currFileDir,fileName+'_deploy.js'))
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
    os.popen(chmodIt(scriptPath)).read()
    na = str(fileName).replace('.sol','')+'_flat'+'.sol'
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
    prgs = jsRead(createPath(home,'variables/prags.py'))
    for i in range(0,len(prgs['prags'])):
        if fileInfo['pragma'] in prgs['prags'][i] and fileInfo['version'] == '':
           fileInfo['version'] = prgs['prags'][i]
def getTheVars():
    flatten_it()
    allLinesParse()
    getInitialVars()
    getPragAll()
    getFullSPDX()
    fileInfo['allVarsTrack']= lineTrack
    bulkUpdateVarisInfo()           
def changeSchedule():
    changeGlob('varisInfoOg',js_it(existWriteFileRead({"count":"0","files":[],"names":[], "adds":{},"currFilePaths": [],"currFileDirs":[],"originalFilePaths":[],"originalFileDirs":[],"deployHistDir":deployHistDir,"projectDir":projectDir,"currProjectDir":currProjectDir,"currFileDir":"","currFilePath":"","home":str(home)},varisPath)))
    changeGlob('varisInfo',{"count":"0","files":[],"names":[], "adds":{},"currFilePaths": [],"currFileDirs":[],"originalFilePaths":[],"originalFileDirs":[],"deployHistDir":varisInfoOg['deployHistDir'],"projectDir":varisInfoOg['projectDir'],"currProjectDir":varisInfoOg["currProjectDir"],"currFileDir":"","currFilePath":"","home":str(home)})
    pen(varisInfo,createPath(currProjectDir,'varis.py'))
    newLs = ["currFileDirs","originalFileDirs","originalFilePaths","files"]
    startFileAssociation()
    changeGlob('originalFilePath',displayFiles(currProjectDir))
    WholeDeploy()
    createFiles()
    pen(reader(varisPath),createPath('current','varis.py')) 
    for k in range(0,len(newLs)):
        for i in range(0,len(varisInfo["names"])):
            varisInfo[newLs[k]].append(varisInfoOg[newLs[k]][i])
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

def deriveLocalVars():
    deriveNameAndFile()
    deriveCurrentDir()
    newVarisInfo()
    newFileInfo()
    bulkUpdateVarisInfo()
    resetArtifactsAndCache()
    CopyOriginalFile()
def getCurrentDeploy():
    if isFile(createPath('current','varis.py')) == False:
        print(createPath('current','varis.py'),' not found...')
        getOldDeploy()
    changeGlob('varisPath',createPath('current','varis.py'))
    changeGlob('varisInfo',js_it(reader(varisPath)))
    determineEndPoint()
def gogo():
    chooseOriginalPath(x)
    createDepploy()
    getTheVars()
def chooseFiles(x):
    return displayFiles(x)
def resetArtifactsAndCache():
    if isFold('cache') == True:
        shutil.rmtree('cache')
    if isFold('artifacts') == True:
        shutil.rmtree('artifacts')
def CopyOriginalFile():
    pen(reader(originalFilePath),currFilePath)
    changeGlob('lines',readLines(currFilePath))
#deriveVariables--------------------------------------------------------------------------
def chooseOriginalPath():
    if originalFilePath is None:
        changeGlob('originalFilePath',chooseFiles(home))
    changeGlob('originalFileDir',buildToSplitLast(originalFilePath,'/'))
def deriveNameAndFile():
    changeGlob('file',originalFilePath.split('/')[-1])
    changeGlob('fileName',file.split('.sol')[0])
def deriveCurrentDir():
    changeGlob('currFileDir',existFoldCheck(createPath(currProjectDir,fileName)))
    changeGlob('currFilePath',createPath(currFileDir,file))
    changeGlob('imports',createExistFold(currFileDir,'imports'))
    changeGlob('alls',createPath(imports,'alls.txt'))
    existFileMakeSpec('',alls)
#allStart---------------------------------------------------------------------------------------------------------------------------------------
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
        print(' you have no contracts to remove, please choose one')
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
    if len(varisInfo['files']) == 0:
        changeGlob('last',home)
        return 'addAnother'
    if len(varisInfo['names']) == 1:
        ls,ls2 = ['add another contract','wrap up this deploy'],['addAnother',True]
    else:
        ls,ls2 = ['would you like to remove any of these','Rearrange Contracts','add another contract','wrap up this deploy'],['remove','rearrange','addAnother',True]
    return createAsk(ls,ls2,'this is your current deploy schedule:\n'+str(varisInfo['names'])+'\nwhat would you like to do?')
def createImports(x):
    return 'import "' + createPath(imports,x)+'";'
def getAttribInfo(st,na):
    input([st])
    return fileInfo['allVarsTrack'][st][na]["attributes"]
def getNamesInfo(st):
    return fileInfo['allVarsTrack'][st]['names']
def minPlu(i,d):
    return[int(i-d),i,int(i+d)]
def remLsSpec(x,ls):
    l,i,h = minPlu(findIt(x,ls),1)
    if i == len(ls)-1:
        return  ls[:-1]
    elif i == 0:
        return ls[1:]
    else:
        return ls[:l]+ls[h:]
def appendEm(ls,ls_):
    ls = [checkIsList(ls),checkIsList(ls_)]
    lsN = []
    for k in range(0,len(ls)):
        ls_ = ls[k]
        for i in range(0,len(ls_)):
            lsN.append(ls_[i])
    return lsN
    
def needit(needs):
    while len(needs) >0:
        needs = appendEm(needs,getAttributes(x,st,needs[0]))
        remLsSpec(x,needs[0])

def getLower(x,y):
    if x<y:
        return x
    return y
def getHighest(ls):
    highest = ls[0]
    for i in range(1,len(ls)):
        if ls[i] > highest:
            highest = ls[i]
    return highest
def movePastLsSpec(x,y,ls):
    y,ls =[checkIsList(y),checkIsList(ls)]
    hi = findIt(y[0],ls)
    for i in range(1,len(y)):
        n = findIt(y[i],ls)
        if n > hi:
            hi = n
    return moveList(hi,x,ls)
        
def moveList(i,x,ls):
    k = findIt(x,ls)
    lsN = []
    ls1 = ls[:k-1]
    ls2 = ls[k+1:]

        
    c = 0
    while ls[c] != x:
        if c == i:
            lsN.append(x)
        lsN.append(ls[c])
        c +=1
    c +=1
    for k in range(c,len(ls)):
        if k == i:
            lsN.append(x)
        lsN.append(ls[k])
    
    

    return lsN
   
       
def getCalls(at):
    call = ['library','contract','interface','abstract contract']
    lsN = call
    for i in range(0,len(call)):
        if call[i] not in at:
            lsN = remLsSpec(call[i],lsN)
    return lsN,at
def getAttributes(ca,na):
    lsN = [na]
    if ca in js:
        ats = js[n]
        for k in range(0,len(ats)):
            at = ats[k]
            lsN.append(at)
    return lsN
def remExtLs(ls,ext):
    ls = checkIsList(ls)
    if len(ls) == 0:
        return ls
    lsN = []
    for i in range(0,len(ls)):
        if str(ext) in ls[i]:
            ls[i] = ls[i].replace('.sol','')
        else:
            lsN.append(ls[i])
    for i in range(0,len(lsN)):
        ls = remLsSpec(lsN[i],ls)
    return ls
def placeInback(x,ls):
    lsN = [x]
    for i in range(0,len(ls)):
        lsN.append(ls[i])
    return lsN
def remFromList(x,ls):
    k = findIt(x,ls)
    lsN = []
    for i in range(0,len(ls)):
        if k != i:
            lsN.append(ls[i])
    return lsN
def getattNames(st):
    return fileInfo['allVarsTrack'][st]['names']
def getattAtts(st,na):
    return fileInfo['allVarsTrack'][st][na]['attributes']
def getAttSpec(st,na,st2):
    return fileInfo['allVarsTrack'][st][na]['attributes'][st2]
def getCallTypes():
    return ['contract','abstract contract','interface','library']
def getImps():
    return remExtLs(list_files(imports),'.sol')
def getNeeds(st,na):
    lsN = []
    call = ['contract','abstract contract','interface','library']
    x = getattAtts(st,na)
    for i in range(0,len(call)):
        n = call[i]
        if n in x:
            lsN+getAttSpec(st,na,call[i])
    return lsN
def getNoNeeds():
    calls = getCallTypes()
    getNeeds(st,na)
def getCallType(x,js):
    calls = getCallTypes()
    for i in range(0,len(calls)):
        if x in js[calls[i]]:
            return calls[i]
def compileNeeds():
    imps,calls,js,jsCalls = getImps(),getCallTypes(),{},{}
    top = []
    bottom = []
    for i in range(0,len(calls)):
        jsCalls[calls[i]] = getattNames(calls[i])
    while len(imps) !=0:
        nImps = imps
        for i in range(0,len(imps)):
            na = imps[i]
            ats = getattAtts(getCallType(na,jsCalls),na)
            js[na] = {"needs":[]}
            for k in range(0,len(calls)):
                n = calls[k]
                if n in ats:
                    js[imps[i]]["needs"] = js[imps[i]]["needs"]+ats[n]
            if len(js[imps[i]]["needs"]) == 0:
                top.append(na)
                nImps = remFromList(na,nImps)
        imps = nImps
        for i in range(0,len(imps)):
            needs = js[imps[i]]["needs"]
            lsN = needs
            for k in range(0,len(needs)):
                ne = needs[k]
                if ne in top:
                    lsN = remFromList(ne,lsN)
            js[imps[i]]["needs"] = lsN
            if len(js[imps[i]]["needs"]) == 0:
                top.append(imps[i])
                nImps = remFromList(imps[i],nImps)
        imps = nImps
    pen('',createPath(imports,'alls.txt'))
    fileInfo['top'] = []
    for i in range(0,len(top)):
        if top[i] != fileInfo['name']:
            al = reader(createPath(imports,'alls.txt'))
            if al == '':
                red = reader(createPath(imports,top[i]+'.sol'))
            else:
                red = al+'\n'+reader(createPath(imports,top[i]+'.sol'))
            pen(red,createPath(imports,'alls.txt'))
            fileInfo['top'].append(top[i])
    red = reader(createPath(imports,'alls.txt'))+'\n'+reader(createPath(imports,fileInfo['name']+'.sol'))
    pen(red,createPath(imports,'alls.txt'))
    pen(reader(createPath(imports,'alls.txt')),currFilePath)
    fileInfo['top'].append(fileInfo['name'])
    bulkUpdateVarisInfo()
    
def determineEndPoint():
    startWhere()
    keepItUp = True
    while keepItUp == True:
        allFiles = returnLen()
        if allFiles == 'rearrange':
            rearrangeDeploy()
        elif allFiles == 'remove':
            removeDeploy()
        elif allFiles == 'addAnother':
                getItGoing()
                compileNeeds()
        elif type(allFiles) == bool:
            keepItUp = False
    pen(reader(varisPath),createPath('current','varis.py'))
    return allFiles

def getItGoing():
    changeGlob('originalFilePath',chooseFiles(last))
    chooseOriginalPath()
    deriveLocalVars()
    getTheVars()
    getInitialVars()
    checkName()
    pragmaSpec = str(fileInfo['allVarsTrack']['pragma solidity']['pragma'])
    bulkUpdateVarisInfo()
    makeConstructors()
    bulkUpdateVarisInfo()
    createFiles()
    chmodIt(createPath(currFileDir,fileName+'_deploy.js'))
def startWhere():
    homeAll = home
    how = ['new','old','current']
    ask = createAsk(how,how,'How would you like to start?')
    if ask == how[0]:
      newDep()
    elif ask == how[1]:
      getOld()
    elif ask == how[2]:
      currentDeployed()
    return
def checkName():
    names = lineTrack['contract']['names']
    lsN = ['input New Name',fileName]
    if fileName not in names:
        for i in range(0,len(names)):
            lsN.append(names[i])
        newName = createAsk(lsN,lsN,'looks like there is a discrepency in the naming convention, we recorded '+str(fileName)+'; please choose the name that does not belong.')
        input(newName)
        lines = readLines(originalFilePath)
        for i in range(0,len(lines)):
            if isCurrent(lines[i],'contract') == True:
                input(lines[i])
                if newName in lines[i]:
                    lines[i] = lines[i].replace(newName,fileName)
        pen(linesToString(lines),originalFilePath)
        getItGoing()
#projectDirs--------------------------------------------------------------------------------------------
def chooseProjectDir():
    createFolders()
    if len(list_files(projectDir)) == 0:
        print('looks like no older projects are on record here, you will have to start a new deploy')
        newDep()
        return 
    else:
        changeGlob('currProjectDir',getFolder(projectDir))
        changeGlob('varisPath',createPath(currProjectDir,'varis.py'))
        retrieveVarisInfo()
def NewProjectDir():
    currProjectDir = ''
    while currProjectDir == '':
        currProjectDir = createPath(projectDir,str(input("what would you like to name the new batch?")))
        changeGlob('currProjectDir',currProjectDir)
    changeGlob('currProjectDir',currProjectDir)
    changeGlob('varisPath',createPath(currProjectDir,'varis.py'))
def changeCurrProjectDir(x):
    changeGlob('currProjectDir',x)
#newProject--------------------------------------------------------------------------------------------
def newDep():
    NewProjectDir()
    newVarisInfo()
#currentProject--------------------------------------------------------------------------------------------
def currentDeployed():
    createFolders()
    if len(list_files(currentDir)) == 0:
        ask = createAsk(['start new deploy','choose previouse deploy'],['new','old'],'looks likeNothing is in the current Folder:')
        if str(ask) == 'new':
            newDep()
            return
        elif str(ask) == 'old':
            getOld()
            return    
    else:
       changeGlob('varisPath',createPath('current','varis.py'))
       retrieveVarisInfo()
       changeGlob('varisPath',createPath(varisInfo["currProjectDir"],'varis.py'))
       changeGlob('currProjectDir',varisInfo["currProjectDir"])
    return 
#oldProject--------------------------------------------------------------------------------------------
def getOld():
    chooseProjectDir()
    return 
#InitializeVariables---------------------------------------------------------------------------------------------------
def initialize():
    global home,slash,lineTrack,sectionHeaders,allVars,lines,fileRead,allLines,last
    home,slash=home_it()
    lineTrack,allLines,lines,last = {},[],[],home
def createFolders():
    changeGlob('variablesDir',existFoldCheck(createPath(home,'variables')))
    changeGlob('deployHistDir',existFoldCheck(createPath(home,'deployHist')))
    changeGlob('currentDir',existFoldCheck(createPath(home,'current')))
    changeGlob('deployHistDir',existFoldCheck(createPath(home,'deployHist')))
    changeGlob('projectDir',existFoldCheck(createPath(deployHistDir,'projects')))
    changeGlob('last',home)
    changeGlob('varisNew',{"count":"0","files":[],"names":[], "adds":{},"currFilePaths": [],"currFileDirs":[],"originalFilePaths":[],"originalFileDirs":[],"deployHistDir":deployHistDir,"projectDir":projectDir,"currProjectDir":"","currFileDir":"","currFilePath":"","home":str(home)})

def syntaxInfo():
        changeGlob("syntax",{ "names":["Modifiers","Visibility","precedence","globalVariables","precedence"],
                             "Modifiers":["pure","view","payable","constant","immutable","anonymous","indexed","virtual","override"],
                             "precedence":["assert","block","coinbase","difficulty","number","block;number","timestamp","block;timestamp","msg","data","gas","sender","value","gas price","origin","revert","require","keccak256","ripemd160","sha256","ecrecover","addmod","mulmod","cryptography","this","super","selfdestruct","balance","codehash","send"],
                             "visibility":["public","private","external","internal"],
                             "modifiers":["pure","view","payable","constant","anonymous","indexed"],
                             "globalVariables":['abi.decode(bytes memory encodedData, (...)) returns (...)', 'abi.encode(...) returns (bytes memory)', 'abi.encodePacked(...) returns (bytes memory)',  'abi.encodeWithSelector(bytes4 selector, ...) returns (bytes memory)', 'abi.encodeCall(function functionPointer, (...)) returns (bytes memory)','abi.encodeWithSelector(functionPointer.selector, (...))', 'abi.encodeWithSignature(string memory signature, ...) returns (bytes memory)', 'to abi.encodeWithSelector(bytes4(keccak256(bytes(signature)), ...)', 'bytes.concat(...) returns (bytes memory)', 'arguments to one byte array<bytes-concat>`', 'string.concat(...) returns (string memory)', 'arguments to one string array<string-concat>`', 'block.basefee (uint)', 'block.chainid (uint)', 'block.coinbase (address payable)', 'block.difficulty (uint)', 'block.gaslimit (uint)', 'block.number (uint)', 'block.timestamp (uint)', 'gasleft() returns (uint256)', 'msg.data (bytes)', 'msg.sender (address)', 'msg.sig (bytes4)', 'msg.value (uint)', 'tx.gasprice (uint)', 'tx.origin (address)', 'assert(bool condition)', 'require(bool condition)', 'for malformed input or error in external component)', 'require(bool condition, string memory message)', 'condition is false (use for malformed input or error in external component). Also provide error message.', 'revert()', 'revert(string memory message)', 'blockhash(uint blockNumber) returns (bytes32)', 'keccak256(bytes memory) returns (bytes32)', 'sha256(bytes memory) returns (bytes32)', 'ripemd160(bytes memory) returns (bytes20)', 'ecrecover(bytes32 hash, uint8 v, bytes32 r, bytes32 s) returns (address)', 'the public key from elliptic curve signature, return zero on error', 'addmod(uint x, uint y, uint k) returns (uint)', 'arbitrary precision and does not wrap around at 2**256. Assert that k != 0 starting from version 0.5.0.', 'mulmod(uint x, uint y, uint k) returns (uint)', 'with arbitrary precision and does not wrap around at 2**256. Assert that k != 0 starting from version 0.5.0.', "this (current contract's type)", 'super', 'selfdestruct(address payable recipient)', '<address>.balance (uint256)', '<address>.code (bytes memory)', '<address>.codehash (bytes32)', '<address payable>.send(uint256 amount) returns (bool)', 'returns false on failure', '<address payable>.transfer(uint256 amount)', 'type(C).name (string)', 'type(C).creationCode (bytes memory)', 'type(C).runtimeCode (bytes memory)', 'type(I).interfaceId (bytes4)', 'type(T).min (T)', 'type(T).max (T)'],"sectionHeader":['contract','library','interface','abstract contract'],"allVars":['contract','library','pragma solidity','import','interface','abstract contract','constructor','function','modify','SPDX-License-Identifier']})
#newInfos-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def newVarisInfo():
    changeGlob('varisInfo',varisNew)
def newFileInfo():
    changeGlob('infoFilePath',createPath(currFileDir,'info.json'))
    changeGlob('fileInfo',js_it({"projectDir":projectDir,"originalFilePath":str(originalFilePath),"originalFileDir":str(originalFileDir),"currProjectDir":str(currProjectDir),"currFilePath":str(currFilePath),"file":str(file), "name":str(fileName),"contract_address":"","api":"","pragma":[],"license":"","args":"", "version":"","variableNames":[],'allVarsTrack':{}}))
#retrieveInfo----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def retrieveVarisInfo():
    changeGlob('varisNew',{"count":"0","files":[],"names":[], "adds":{},"currFilePaths": [],"currFileDirs":[],"originalFilePaths":[],"originalFileDirs":[],"deployHistDir":deployHistDir,"projectDir":projectDir,"currProjectDir":"","currFileDir":"","currFilePath":"","home":str(home)})
    changeGlob('varisInfo',js_it(existFileMakeSpec(varisNew,varisPath)))   
def retrieveFileinfo():
    newFileIno = js_it({"projectDir":projectDir,"originalFilePath":str(originalFilePath),"originalFileDir":str(originalFileDir),"currProjectDir":str(currProjectDir),"":str(currFilePath),"file":str(file), "name":str(fileName),"contract_address":"","api":str(keys()),"pragma":[],"license":"","args":"", "version":"","variableNames":[],"top":[],'allVarsTrack':{}})
    changeGlob('fileInfo',js_it(existFileMakeSpec(newFileInfo,infoFilePath)))
def runIt():
    initialize()
    createFolders()
    syntaxInfo()
    determineEndPoint()
def compileImports():
    ls = list_files('/home/bigrugz/Desktop/newTester/variables/compileImports')
    for i in range(0,len(ls)):
        print(ls[i],len(ls),i)
        initialize()
        createFolders()
        syntaxInfo()
        neFileInfo = js_it({"projectDir":projectDir,"originalFilePath":str(createPath('/home/bigrugz/Desktop/newTester/variables/compileImports',ls[i])),"originalFileDir":str('/home/bigrugz/Desktop/newTester/variables/compileImports'),"currProjectDir":str('/home/bigrugz/Desktop/newTester/variables/compileImports'),"currFilePath":str(createPath('/home/bigrugz/Desktop/newTester/variables/compileImports',ls[i])),"file":str(ls[i]), "name":str(ls[i].replace('.sol','')),"contract_address":"","api":"","pragma":[],"license":"","args":"", "version":"","variableNames":[],"top":[],'allVarsTrack':{}})
        changeGlob('currFileDir','/home/bigrugz/Desktop/newTester/variables/compileImports')
        changeGlob('currProjectDir','currFileDir')
        changeGlob('file',ls[i])
        changeGlob('fileName',ls[i].replace('.sol',''))
        changeGlob('fileInfo',neFileInfo)
        deriveCurrentDir()
        changeGlob('lines',readLines(createPath('/home/bigrugz/Desktop/newTester/variables/compileImports',ls[i])))
        allLinesParse()
compileImports()
