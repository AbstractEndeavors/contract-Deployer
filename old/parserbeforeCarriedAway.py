import json
import os
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
def readLines():
    lsN = []
    lines = fileRead.replace('\n','^*&*****').split('^*&*****')
    for i in range(0,len(lines)):
        lines[i] = eatOuterMod(lines[i],['\n','\t',' ',''])
        if lines[i] not in ['\n',' \n','',' ','\t']  and len(str(eatAllMod(lines[i],['\n','\t',' ','/',';','']))) != 0:
            lsN.append(lines[i]+'\n')
    print(lsN)
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
    return eatOuterMod(eatInnerMod(x,ls),ls)
def eatInnerMod(x,ls):
    if len(x)>2:
        while x[0] in ls and len(x) >2:
            x = x[1:]
        return x
    return x
def eatOuterMod(x,ls):
    if len(x)>2:
        while x[-1] in ls and len(x) >2:
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
def get(constructorAll):
    constructor = constructorAll.replace(';',';^^^***').split('^^^***')
    print(lineTrack['constructorVars'])
    for c in range(0,len(getAny('constructorVars',"constVariables"))):
        if '[]' in getAny('constructorVars',"attributes")[c]:
            higher = 1
            for i in range(0,len(constructor)):
                abstractLs = ListInString(constructor[i],getAny('abstract contract','names'))
                if len(abstractLs) !=0:
                    for k in range(0,len(abstractLs)):
                        spl = constructor[i].split(abstractLs[k]+'(')
                        appendAnySpec('abstract contract','addresses',spl[1].split(')')[0],findIt(abstractLs[k],getAny('abstract contract','names')))
                        if getAny('constructorVars',"constVariables")[c] in spl[1].split(')')[0]:
                            appendAny('constructorVars',"variables",getAny('abstract contract','use')[findIt(abstractLs[k],getAny('abstract contract','names'))][c]) 
                if getAny('constructorVars',"constVariables")[c]+'[' in constructor[i]:
                    constInt = constructor[i].split(getAny('constructorVars',"constVariables")[c]+'[')[1].split(']')[0]
                    if isInt(constInt) == True:
                        higher = getHigher(constInt,higher)
                    else:
                        newInt = detNumInWhile(constInt,constructor,i)
                        if newInt != None:
                            higher = getHigher(newInt,higher)
                
            lineTrack['constructorVars']["attributes"][c] = getAny('constructorVars',"attributes")[c].replace('[]','['+str(higher)+']')
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
    return js_it(str(x)[:-1]+get_c(len(x))+'"'+str(y)+'":[]'+'}')
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
def updateAny(st,st2,x,i):
    lineTrack[st][st2][i] = x
def updateLineTrack(x):
    lineTrack = x
    return lineTrack
def LineTrackJsPlace(js,st,brac):
    return jsPlace(st,brac,js)
def createAllVars():
    for i in range(0,len(lines)):
        x = eatInnerMod(lines[i],['\n','\t',' ','/'])
        for k in range(0,len(allVars)):
            if isCurrent(x,allVars[k]) == True:
                if i not in getAny(allVars[k],"lines"):
                   appendAny(allVars[k],"lines",i)
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
def createWord():
    import random
    from random import randint
    k = ''
    for i in range(0,random.randint(0,45)):
        k = k + str(get_alph()[random.randint(0, len(get_alph())-1)])
    return k
def getPragAll():
    
    changeGlob('deff',js_it('[[1,1],[0,1],[-1,1],[1,-1],[1,0],[0,0]]'))
    changeGlob('att',js_it("['=<','<','>','>=','=','^']"))
    changeGlob('pragmaVers',listAllPragma())
    lineTrack['pragma solidity']['range'] = pragmaRange(lineTrack['pragma solidity']['names'])
    lineTrack['pragma solidity']['use'] = lineTrack['pragma solidity']['range'][0]

def getPragLines():
    for i in range(0,len(lines)):
        x = eatInnerMod(lines[i],['\n','\t',' ','/'])
        if isCurrent(x,'pragma solidity') == True:
            appendAny('pragma solidity',"names",x.split('pragma solidity ')[1].split(';')[0])
    getPragAll()
def setSectionHeaders():
    for i in range(0,len(sectionHeaders)):
        if sectionHeaders[i] in lineTrack:
            sect = sectionHeaders[i]
            n = lineTrack[sect]["lines"]
            for k in range(0,len(n)):
               x = eatInnerMod(lines[n[k]],['\n','\t',' ','/'])
               name = x.split(sect+' ')[1].split(' ')[0]
               if name not in getAny(sect,'names'):
                   appendAny(sect,'names',name)
                   getAny(sect,'addresses').append([])
                   getAny(sect,'use').append([])
def querySectionHeaders():
    for i in range(0,len(lines)):
        x = eatInnerMod(lines[i],['\n','\t',' ','/',','])
        for k in range(0,len(sectionHeaders)):
            sect = sectionHeaders[k]
            sectNames = lineTrack[sect]["names"]
            for c in range(0,len(sectNames)):
                if isCurrent(x,sectNames[c]) == True:
                    use = eatOuterMod(x,['\n','\t',' ','/',';']).split(' ')[-1]
                    if use not in getAny(sect,'use')[c]:
                        appendAnySpec(sect,'use',use,c)
def queryLibraries():
    for i in range(0,len(lines)):
        x = eatInnerMod(lines[i],['\n','\t',' ','/'])
        if isCurrent(x,'using') == True:
            name = x.split('using ')[1].split(' ')[0]
            appendAnySpec('library',"use",x.split(' ')[-1].split(';')[0],findIt(name,getAny('library',"names")))
def queryConstructorData(lineTrack):
    const = lines[getAny('constructor','lines')[-1]].split('constructor(')[1].split(')')[0].split(',')
    constructor = stopWhenClosed(linesToString(lines[getAny('constructor','lines')[-1]:]),['{','}'])
    for i in range(0,len(const)):
        constAlls = const[i].split(' ')
        atts = ["attributes","type","constVariables"]
        for k in range(0,len(constAlls)):
            appendAny('constructorVars',atts[k],constAlls[k])
    constructor = constructor.replace(constructor.split('{')[0]+'{','')[:-1]
    constructor = eatAllMod(constructor,['\n','\t',' ','/',','])
    get(constructor)
def querySPDX():
    spdx= {"0":"No License (None)","1":"The Unlicense (Unlicense)","2":"MIT License (MIT)","3":"GNU General Public License v2.0 (GNU GPLv2)","4":"GNU General Public License v3.0 (GNU GPLv3)","5":"GNU Lesser General Public License v2.1 (GNU LGPLv2.1)","6":"GNU Lesser General Public License v3.0 (GNU LGPLv3)","7":"BSD 2-clause &quot;Simplified&quot; license (BSD-2-Clause)","8":"BSD 3-clause &quot;New&quot; Or &quot;Revised&quot; license (BSD-3-Clause)","9":"Mozilla Public License 2.0 (MPL-2.0)","10":"Open Software License 3.0 (OSL-3.0)","11":"Apache 2.0 (Apache-2.0)","12":"GNU Affero General Public License (GNU AGPLv3)","13":"Business Source License (BSL 1.1)"}
    spdxId = []
    for i in range(1,len(spdx)):
        n = safeSplit(safeSplit(spdx[str(i)],' (',1),')',0)
        spdxId.append(n)
    spdxId = makeAllComparable(spdxId)
    spdxLines = getAny('SPDX-License-Identifier','lines')
    for i in range(0,len(spdxLines)):
        appendAny('SPDX-License-Identifier','names',compareList(makeAllComparable(eatAllMod(lines[spdxLines[i]].split('SPDX-License-Identifier:')[1],['\n','\t',' ','/',',']))[0],spdxId))       
    for i in range(0,len(getAny('SPDX-License-Identifier','names'))):
        lic = returnMostAbundant(getAny('SPDX-License-Identifier','names'),['',None,False,True])
        if i == 0:
            appendAny('SPDX-License-Identifier','use',lic)
        else:
            updateAny('SPDX-License-Identifier','use',lic,0)
        input(lic)

def getVars(filePath):
    global lineTrack,sectionHeaders,allVars,lines,fileRead
    
    fileRead = reader(filePath)
    lines = readLines()
    createAllVars()
    getPragLines()
    setSectionHeaders()
    querySectionHeaders()
    queryLibraries()
    queryConstructorData(lineTrack)
    querySPDX()
    for i in range(0,len(allVars)):
        if allVars[i] in lineTrack:
            print(allVars[i],':',lineTrack[allVars[i]])
    return lineTrack,lines
global home,slash,lineTrack,sectionHeaders,allVars,lines,fileRead   
home,slash=home_it()
lines = []
lineTrack = {'contract':{"lines":[],"names":[],"use":[],"addresses":[]},'library':{"lines":[],"names":[],"use":[],"addresses":[]},'pragma solidity':{"lines":[],"names":[],"use":[]},'import':{"lines":[],"names":[],"use":[],"addresses":[]},'interface':{"lines":[],"names":[],"use":[],"addresses":[]},'abstract contract':{"lines":[],"names":[],"use":[],"addresses":[]},'constructor':{"lines":[],"names":[],"use":[],"addresses":[]},'function':{"lines":[],"names":[]},'modify':{"lines":[],"names":[],"use":[],"addresses":[]},'SPDX-License-Identifier':{"lines":[],"names":[],"use":[]},'constructorVars':{"attributes":[],"constVariables":[],"type":[],"variables":[]}}
sectionHeaders = ['contract','library','interface','abstract contract']
allVars = allVars = ['contract','library','pragma solidity','import','interface','abstract contract','constructor','function','modify','SPDX-License-Identifier']
getVars('/home/bigrugz/Desktop/newTester/contracts/boostManager.sol')
