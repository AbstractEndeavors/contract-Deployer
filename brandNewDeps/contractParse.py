import json
import os
import cmdInput
import fileFinder2 as find
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
def homeIt():
    changeGlob('home',os.getcwd())
    changeGlob('slash','\\')
    if slash not in home:
        changeGlob('slash','/')
def createPath(x,y):
    if len(x) >0:
        for i in range(0,len(x)):
            if x[-1] == slash:
                x = x[:-1]
    if len(y) >0:
        for i in range(0,len(y)):
            if y[0] == slash:
                y = y[1:]
    return x+slash+y
def createPaths(ls):
    y = createPath(ls[0],ls[1])
    for i in range(2,len(ls)):
        y = createPath(y,ls[i])
    return y
def mkPens(x,y):
    if type(y) is list:
        y = createPaths(y)
    if slash in y:
        if '.' in y.split(slash)[-1]:
            mkDirs(y.replace(slash+y.split(slash)[-1],''))
            pen(x,y)
    else:
        pen(x,y)
def mkDirs(x):
    os.makedirs(x, exist_ok=True)
    return x
def lsCheck(x,ls):
    for i in range(0,len(ls)):
        if x == ls[i]:
            return True
    return False
def currIs(x,ls):
    for i in range(0,len(ls)):
        if x[:len(ls[i])] == ls[i]:
            return x[len(ls[i]):]
    return False
def currIsNeg(x,ls):
    for i in range(0,len(ls)):
        if x[len(x)-len(ls[i]):] == ls[i]:
            return x[:len(x)-len(ls[i])] 
    return False
def eatInner(x,ls):
    z = x
    for i in range(0,len(x)):
        if currIs(z,ls) == False:
            return z
        else:
            z = currIs(z,ls)
    return z
def eatOuter(x,ls):
    z = x
    for i in range(0,len(x)):
        if currIsNeg(z,ls) == False:

            return z
        else:
            z = currIsNeg(z,ls)
    return z
def eatAll(x,ls):
    y = eatInner(x,ls)
    z = eatOuter(y,ls)
    return z
def countIt(x,y):
    if y in x:
        return int((len(x)-len(x.replace(y,'')))/len(y))
    return int(0)
def getEnclosedString(sec,ls):
    z = ''
    countLs = [0,0,0,z]
    lis = sec
    for i in range(0,len(lis)):
        li = lis[i]
        for c in range(0,len(li)):
            z = z + li[c]
            countLs[0],countLs[1] = countIt(z,ls[0]),countIt(z,ls[1])
            if countLs[0] != 0 and countLs[1] != 0 and countLs[0] == countLs[1]:
                countLs[-1] = z
                countLs[-2] = len(z)
                return countLs
 
def findIt(x,ls):
    for i in range(0,len(ls)):
        if x == ls[i]:
            return i
    return False
def ifNoLs(js,x):
   if x not in js:
      js[x] = []
      js['names'].append(x)
   return js
def ifThenApp(ls,x):
   if type(ls) is list:
      ls.append(x)
      return ls
   ls = x
   return ls
def checkIsList(x):
    if type(x) is not list:
        if ',' in str(x):
            x = str(x.split(','))
        else:
            x = [x]
    return x
def chkExist(x,y):
    ls = jsAll[jsAll['current']]
    for i in range(0,len(ls)):
        n = ls[i]
        if n['type'] == x and n['name'] == y:
            return True
        else:
            return False
def lsInString(ls,x):
    for i in range(0,len(ls)):
        if ls[i][:len(x)] == x:
            return ls[i]
    return False
def isCurr(x,ls):
    for i in range(0,len(ls)):
        if x[:len(ls[i])] == ls[i]:
            return ls[i]
    return False
def isLsVar(x):
    if '[' in x:
        return True
    return False
def changeGlob(x,v):
    globals()[x] = v
def check_file(x):
    return os.path.isfile(x)
def do_the_file(x,y,z):
    if check_file(x) == False:
        pen(y,z)
        return y
    return reader(z)
def addLsJs(x,y):
    return jsIt(str(x)[:-1]+get_c(len(x))+'"'+str(y)+'":[]'+'}')
def make_dir(x):
    if check_dir(x) == False:
        os.mkdir(x)
def delete_it(x):
    os.remove(x)
def countIt(x,y):
    return (len(x)-len(x.replace(y,''))/len(y))
def sortLs(ls):
    ls.sort()
    return ls
def getLast(ls):
    return sortLs(ls)[-1]
def find_it(x,y):
    i = 0
    for i in range(0,len(x)):
        if str(x[i]) == str(y):
            return i
    return False
def get_c(k):
    if k == 0:
        return ''
    return ','
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

def reader_C(file):
    with open(file, 'r',encoding='utf-8-sig') as f:
        text = f.read()
        return text
def reader_B(file):
    with open(file, 'r',encoding='UTF-8') as f:
        text = f.read()

        return text
def jsRead(file):
    with open(file, 'r') as f:
        text = f.read()
        return jsIt(text)
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
def jsIt(x):
    return json.loads(str(x).replace("'",'"').replace('{,','{'))
def check_str(x,y):
    c = ''
    if str(x) != str(y):
        c = y
    return c
def create_path(x,y):
    if x == '':
        return str(y) + str(check_str(str(y),slash))
    return str(x) + str(check_str(x[-1],slash))+str(y)
def list_files(x):
    return os.listdir(x)
def eatInner(x,ls):
    if len(x) == 0:
        return x
    for i in range(0,len(x)):
        if x[i] not in ls:
            return x[i:]
    return ''
def eatOuter(x,ls):
    if len(x) == 0:
        return x
    for i in range(1,len(x)+1):
        if x[i-1] not in ls:
            return x[:-i]
    return ''
def eatAll(x,ls):
    return eatOuter(eatInner(x,ls),ls)
def eatNorm(x):
    return eatAll(x,['',' ','\n','\t'])
def isLs(ls):
    if type(ls) is list:
        return True
    return False
def mkLs(ls):
    if isLs(ls) == False:
        ls = [ls]
    return ls
def getAtts(lsN,x):
    if ' is ' in x:
        atts = mkLs(x.split('is')[1].split('{')[0].replace('  ',' ').split(',').split(' '))
        for i in range(0,len(atts)):
            lsN = ifNoAppLs(ls,atts[i])
    return lsN   
def topGet(x,y,js):
    ver = x.split(y+' ')[1].split('\n')[0].split(';')[0]
    jsAll[y]['versions'].append(ver)
    jsAll[y]['latest'] = ver
    return js
def headGet(x,y,js):
    js['currHead'] = y
    ver = x.split(y+' ')[1]
    js[y]['names'].append(ver)
    js['latest'] = y
    js[y] = ifNoAddJs(js[y],ver)
    js[y][ver]['atts'] = []
    js[y][ver]['atts'] = getAtts(js[y][ver]['atts'],x)
    
    return js
def functionGet(x,js):
    ver = x.split('function ')[1].split('(')[0]
    js['function']['names'].append(ver)
    js['currFun'] = ver
    return js
def constructorGet(x,js):
    js['currHead']['constructor'] = {'atts':[],'constVars':{"wholeVars":[]}}
    js['currHead']['constructor']['constVars']['wholeVars'] = x.split('constructor(')[1].split('(')[0].split(')')
    js['function']['latestFun'].append(ver)
    js['currHead']['constructor']['atts'] = getAtts(x)
    return js
def isHead(x):
    global jsAll
    x = eatNorm(x)
    for i in range(0,len(allVars)):
        head = allVars[i]
        if x[:len(head)] == head:
            ls = ['pragma solidity','SPDX-License-Identifier'],['contract','library','interface','abstract contract'],['constructor'],['function']
            for k in range(0,len(ls)):
               if head in ls[k]:
                   if k == 0:
                        jsAll = topGet(x,head,jsAll)
                   if k == 1:
                       jsAll = headGet(x,head,jsAll)
                   if k == 2:
                      jsAll = constructorGet(x,jsAll)
                   if k == 3:
                      jsAll = functionGet(x,jsAll)
    
def ifNoApp(ls,y):
    if y not in ls:
        ls.append(y)
    return ls
def ifNoAddLs(js,y):
    if y not in js:
        js[y] = []
    return js
def ifNoAddJs(js,y):
    if y not in js:
        js[y] = {}
    return js
def ifNoEqJs(js,y,z):
    if y not in js:
        js[y] = z
    return js
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
def writeAndRun(x,y):
    
    pen(jsAll,"takeIt.json")
    pen('import contractParse as parse\nimport json\ndef Add(x):\n\t\treturn parse.'+str(y)+'Get(x,js)\nglobal js\njs = json.loads(str(parse.reader("takeIt.json")).replace('+'"'+"'"+'"'+",'"+'"'+"'"+'))\njs = Add("'+str(x)+'")\nparse.pen(js,"takeIt.json")','funGet.py')
    import funGet as fun
    jsAll = json.loads(str(reader('takeIt.json')).replace("'",'"'))
def initiateJs():
    global jsAll
    setUp = {'pragma solidity':{'versions':[],'latest':"","range":[],"total":""},'SPDX-License-Identifier':{"versions":[],"latest":"","total":""},'contract':{"names":[],"atts":[]},'library':{"names":[],"atts":[]},'interface':{"names":[],"atts":[]},'abstract contract':{"names":[],"atts":[]},'constructor':{"atts":[]},'function':{"names":[]},'modify':{"names":[]}}
    for i in range(0,len(allVars)):
        ifNoAddJs(jsAll,allVars[i])
        jsAll[allVars[i]] = setUp[allVars[i]]
def syntaxInfo():
        changeGlob("syntax",{ "names":["Modifiers","Visibility","precedence","globalVariables","precedence"],
                             "Modifiers":["pure","view","payable","constant","immutable","anonymous","indexed","virtual","override"],
                             "precedence":["assert","block","coinbase","difficulty","number","block;number","timestamp","block;timestamp","msg","data","gas","sender","value","gas price","origin","revert","require","keccak256","ripemd160","sha256","ecrecover","addmod","mulmod","cryptography","this","super","selfdestruct","balance","codehash","send"],
                             "visibility":["public","private","external","internal"],
                             "modifiers":["pure","view","payable","constant","anonymous","indexed"],
                             "globalVariables":['abi.decode(bytes memory encodedData, (...)) returns (...)', 'abi.encode(...) returns (bytes memory)', 'abi.encodePacked(...) returns (bytes memory)',  'abi.encodeWithSelector(bytes4 selector, ...) returns (bytes memory)', 'abi.encodeCall(function functionPointer, (...)) returns (bytes memory)','abi.encodeWithSelector(functionPointer.selector, (...))', 'abi.encodeWithSignature(string memory signature, ...) returns (bytes memory)', 'to abi.encodeWithSelector(bytes4(keccak256(bytes(signature)), ...)', 'bytes.concat(...) returns (bytes memory)', 'arguments to one byte array<bytes-concat>`', 'string.concat(...) returns (string memory)', 'arguments to one string array<string-concat>`', 'block.basefee (uint)', 'block.chainid (uint)', 'block.coinbase (address payable)', 'block.difficulty (uint)', 'block.gaslimit (uint)', 'block.number (uint)', 'block.timestamp (uint)', 'gasleft() returns (uint256)', 'msg.data (bytes)', 'msg.sender (address)', 'msg.sig (bytes4)', 'msg.value (uint)', 'tx.gasprice (uint)', 'tx.origin (address)', 'assert(bool condition)', 'require(bool condition)', 'for malformed input or error in external component)', 'require(bool condition, string memory message)', 'condition is false (use for malformed input or error in external component). Also provide error message.', 'revert()', 'revert(string memory message)', 'blockhash(uint blockNumber) returns (bytes32)', 'keccak256(bytes memory) returns (bytes32)', 'sha256(bytes memory) returns (bytes32)', 'ripemd160(bytes memory) returns (bytes20)', 'ecrecover(bytes32 hash, uint8 v, bytes32 r, bytes32 s) returns (address)', 'the public key from elliptic curve signature, return zero on error', 'addmod(uint x, uint y, uint k) returns (uint)', 'arbitrary precision and does not wrap around at 2**256. Assert that k != 0 starting from version 0.5.0.', 'mulmod(uint x, uint y, uint k) returns (uint)', 'with arbitrary precision and does not wrap around at 2**256. Assert that k != 0 starting from version 0.5.0.', "this (current contract's type)", 'super', 'selfdestruct(address payable recipient)', '<address>.balance (uint256)', '<address>.code (bytes memory)', '<address>.codehash (bytes32)', '<address payable>.send(uint256 amount) returns (bool)', 'returns false on failure', '<address payable>.transfer(uint256 amount)', 'type(C).name (string)', 'type(C).creationCode (bytes memory)', 'type(C).runtimeCode (bytes memory)', 'type(I).interfaceId (bytes4)', 'type(T).min (T)', 'type(T).max (T)'],"sectionHeader":['contract','library','interface','abstract contract'],"allVars":['contract','library','pragma solidity','import','interface','abstract contract','constructor','function','modify','SPDX-License-Identifier']})
changeGlob('allVars',['pragma solidity','SPDX-License-Identifier','contract','library','interface','abstract contract','constructor','function'])
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
        x = eatInner(x,[' ','\t','\n'])
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
            ls_pr = jsIt(str(str(ls_pr)[:-1] + ','+str(make_js(pr[i],n)+'}')).replace('{,','{'))
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
    pragCurr = ['0'+eatInner(createPragFromInt(pragCurr[0]),['0']),'0'+eatInner(createPragFromInt(pragCurr[1]),['0'])]
    return pragCurr
def listAllPragma():
    pragsVers = jsRead(createPath(home,'pragmas/prags.py'))
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
    return '0.'+x[0]+'.'+eatOuter(x[1:],['0'])
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
def getThePrags(lines):
    for i in range(0,len(fileInfo["allVarsTrack"][allVars][getSectHeaders()[-1]]["lines"])):
        fileInfo["allVarsTrack"][getSectHeaders()[-2]]["names"].append(safeSplit(safeSplit(lines[int(fileInfo["allVarsTrack"][getSectHeaders()[-2]]["lines"][i])],'pragma solidity'+' ',1),';',0))
    pragmaRange(fileInfo["allVarsTrack"][getSectHeaders()[-1]]["names"])

def getInitPrags():
    changeGlob('deff',jsIt('[[1,1],[0,1],[-1,1],[1,-1],[1,0],[0,0]]'))
    changeGlob('att',jsIt("['=<','<','>','>=','=','^']"))
    changeGlob('pragmaVers',listAllPragma())
    fileInfo['currPrag'] = pragmaRange(fileInfo['pragmas'])[0]
def doIt():
    global jsAll,allVars
    jsAll = {}
    allVars = ''
    changeGlob('allVars',['pragma solidity','SPDX-License-Identifier','contract','library','interface','abstract contract','constructor','function'])
    changeGlob('jsAll',{'currHead':"",'names':{}})
    initiateJs()
    cont = reader('NeFiBoostManager.sol')
    for i in range(0,len(lines)):
        isHead(lines[i])
def getTops():
    
    for i in range(0,len(lines)):
        li = lines[i]
        if li[:len('pragma solidity')] == 'pragma solidity':
            prag = li.split('pragma solidity ')[1].split(';')[0]
            fileInfo['pragmas'].append(prag)
            fileInfo['currPrag'] = prag
        if li[:len('//SPDX-License-Identifier:')] == '//SPDX-License-Identifier:':
            lic = li.split('//SPDX-License-Identifier:')[1].split(';')[0].replace(' ','')
            fileInfo['licenses'].append(lic)
            fileInfo['currLic'] = lic
    getInitPrags()
    rang = pragmaRange(fileInfo['pragmas'])
    fileInfo['pragmaRange'] = rang
    fileInfo['currPrag'] = rang[0]
    mkPens(fileInfo,[varis['fileFolds'][-1],'fileInfo.json'])
    pen(reader('samples/hardhat.config.js').replace('^^^*killMe*^^^',fileInfo['currPrag'][-1]),createPath(varis['fileFolds'][-1],'hardhat.config.js'))
    cmdInput.createPassScript('solc-select install '+fileInfo['currPrag'][-1].replace('^','')+';'+' solc-select use '+fileInfo['currPrag'][-1].replace('^','')+'; npx hardhat run scripts/deploy.js',varis['fileFolds'][-1])
homeIt()
varis,varis['filePaths'],varis['oGfiles'],varis['fileFolds'],varis['files'],varis['ogFilePath'],varis['Dir'] = {},[],[],[],[],[],str(createPaths(['deploys',input('what would you like to name the deploy?')]))
print('which contract would you like to deploy?')
varis['ogFilePath'].append(find.displayFiles(home,'sol',True,'files'))
varis['files'].append(varis['ogFilePath'][-1].split(slash)[-1])
varis['fileFolds'].append(mkDirs(createPaths([varis['Dir'],varis['files'][-1].split('.sol')[0]])))
varis['varisPath'] = createPaths([varis['fileFolds'][-1],'varis.json'])
varis['filePaths'].append(createPaths([varis['fileFolds'][-1],varis['files'][-1]]))
varis['oGfiles'].append(createPaths([varis['fileFolds'][-1].split('.sol')[0],'ogFile',varis['files'][-1]]))
pen(varis,varis['varisPath'])
changeGlob('fileInfo',{'fold':"",'itterableMapping':'','constructorData':'','contName':"",'current':'','currHead':'','currPrag':'','pragmas':[],'currLic':'','licenses':[],'names':[]})
mkPens(reader(varis['ogFilePath'][-1]),varis['oGfiles'][-1])
mkPens(reader(varis['ogFilePath'][-1]),varis['filePaths'][-1])
mkPens(fileInfo,[varis['fileFolds'][-1],'fileInfo.json'])
changeGlob('lines',reader(varis['filePaths'][-1]).split('\n'))
getTops()
    
