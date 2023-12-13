from functions_group import *
class pragmaVariableManager:
    def __init__(self, lineTrack, fileInfo):
        self.fileInfo = fileInfo
        self.lineTrack = lineTrack
        self.slash = '//' if '//' in os.getcwd() else '/'
        self.pragmaVersionsPath = os.path.join(
            os.getcwd(), 'variables/prags.py')
        self.pragmaVersions = safe_read_from_json(self.pragmaVersionsPath)
        self.version_identifiers = ['=<', '<', '>', '>=', '=', '^']
        self.pragmaVers = self.listAllPragma()
        self.getPragAll()

    def pragHiffPieces(self, x):
        """
        Returns the first entry of the version in pragma.
        """
        return self.pragmaVers[str(pragmaVerSplit(x))][0]

    def pragSubPieces(self, x):
        """
        Finds the previous version item by identifying the index using the 'findIt' function.
        """
        return self.pragmaVers[pragmaVerSplit(x)][findIt(x, self.pragmaVers[pragmaVerSplit(x)])-1]

    def pragmaRange(self):
        """
        Returns the range of pragma versions.
        """
        prags_list = self.lineTrack['pragma solidity']['prags']
        if len(prags_list) == 1:
            if countIt(prags_list[0], '.') == 2:
                if prags_list[0][0] == '=':
                    if len(ListInString(prags_list[0].replace('=', ''), self.version_identifiers)) == 0:
                        return [prags_list[0].replace('=', ''), prags_list[0].replace('=', '')]
        prags_list = checkIsList(prags_list)
        pragCurr = [0, 0]
        for i in range(0, len(prags_list)):
            prag = self.splitAndSee(prags_list[i])
            if int(pragCurr[0]) < int(prag[0]):
                pragCurr[0] = prag[0]
            if int(pragCurr[1]) < int(prag[1]):
                pragCurr[1] = prag[1]
        pragCurr = [eatOuter(createPragFromInt(pragCurr[0]), '0'), eatOuter(
            createPragFromInt(pragCurr[1]), '0')]
        return pragCurr

    def listAllPragma(self):
        """
        Does working with all pragma versions and returns 'self.pragmaVers'.
        """
        self.pragmaVers = {"vers": []}
        for i in range(0, len(self.pragmaVersions['prags'])):
            n = self.pragmaVersions['prags'][i][1:]
            nn = ''
            while n[0] != '-' and n[0] != '+':
                nn = nn + n[0]
                n = n[1:]
            vers = safeSplit(nn, '.', 1)
            if vers not in self.pragmaVers:
                self.pragmaVers[str(vers)] = []
                self.pragmaVers["vers"].append(vers)
            if nn not in self.pragmaVers[vers]:
                self.pragmaVers[vers].append(nn)
        return self.pragmaVers

    def splitAndSee(self, prags_obj):
        """
        Processes the pragma object to extract details and perform operations based on certain conditions.
        """
        lsN = [0, 0]
        less = ['=<', '<']
        great = ['>', '>=']
        prags_list = is_list_obj_in_str(prags_obj, self.version_identifiers)
        for prags_char in prags_list:
            prags_obj = eatInner(prags_obj, [self.slash, ' ', '', '\t', '\n'])

            det = determineSection(prags_obj, [prags_char])

            if prags_obj[0] == '^':
                lsN = [convertPragToInt(prags_obj), convertPragToInt(
                    self.pragHiffPieces(prags_obj))]

            elif det != None:

                xn = splitVarOutAndEndOrSpace(det, prags_char)

                if prags_char in less:
                    if det == less[0]:
                        lsN = [convertPragToInt(
                            self.pragmaVers[self.pragmaVers["vers"][-1]][-1]), xn]
                    else:
                        lsN = [0, self.pragSubPieces(xn)]
                if prags_char in great:
                    if det == less[0]:
                        lsN = [xn, convertPragToInt(
                            self.pragmaVers[self.pragmaVers["vers"][0]][0])]
                    else:
                        lsN = [convertPragToInt(eatInner(prags_char, prags_list)), convertPragToInt(
                            self.pragmaVers[self.pragmaVers["vers"][0]][0])]
        return lsN

    def getPragAll(self):
        """
        Retrieves all details related to the pragma version.
        """
        self.lineTrack['pragma solidity']['range'] = self.pragmaRange()
        for k in range(0, 2):
            for i in range(0, len(self.version_identifiers)):
                self.lineTrack['pragma solidity']['range'][k] = str(
                    self.lineTrack['pragma solidity']['range'][k]).replace(self.version_identifiers[i], '')
        self.lineTrack['pragma solidity']['pragma'] = self.lineTrack['pragma solidity']['range'][0]
        if len(self.lineTrack['pragma solidity']['prags']) != 0:
            self.lineTrack['pragma solidity']['pragma'] = self.lineTrack['pragma solidity']['range'][0]
            self.fileInfo['pragma'] = self.lineTrack['pragma solidity']['pragma']
        for i in range(0, len(self.pragmaVersions['prags'])):
            if (str(self.fileInfo['pragma']) in str(self.pragmaVersions['prags'][i])) and self.fileInfo['version'] == '':
                self.fileInfo['version'] = self.pragmaVersions['prags'][i]
                
class spdxManager:
    def __init__(self,lineTrack,fileInfo,lines):
        self.lineTrack=lineTrack
        self.fileInfo=fileInfo
        self.lines=lines
        self.getFullSPDX()
    def getAny(self,st,st2):
       return self.lineTrack[st][st2]    
    def getFullSPDX(self):
        spdx= {"0":"No License (None)","1":"The Unlicense (Unlicense)","2":"MIT License (MIT)","3":"GNU General Public License v2.0 (GNU GPLv2)","4":"GNU General Public License v3.0 (GNU GPLv3)","5":"GNU Lesser General Public License v2.1 (GNU LGPLv2.1)","6":"GNU Lesser General Public License v3.0 (GNU LGPLv3)","7":"BSD 2-clause &quot;Simplified&quot; license (BSD-2-Clause)","8":"BSD 3-clause &quot;New&quot; Or &quot;Revised&quot; license (BSD-3-Clause)","9":"Mozilla Public License 2.0 (MPL-2.0)","10":"Open Software License 3.0 (OSL-3.0)","11":"Apache 2.0 (Apache-2.0)","12":"GNU Affero General Public License (GNU AGPLv3)","13":"Business Source License (BSL 1.1)"}
        spdxIdOg = []
        for i in range(0,len(spdx)):
            n = safeSplit(safeSplit(spdx[str(i)],' (',1),')',0)
            spdxIdOg.append(n)
        spdxId = makeAllComparable(spdxIdOg)
        spdxLines = self.getAny('SPDX-License-Identifier','lines')
        for i in range(0,len(spdxLines)):
            comp = compareList(makeAllComparable(eatAll(self.lines[spdxLines[i]].split('SPDX-License-Identifier:')[1],['\n','\t',' ','/',',']))[0],spdxId,spdxIdOg)
            if comp != None:
                self.lineTrack['SPDX-License-Identifier']['Licenses'].append(comp)    
        for i in range(0,len(self.getAny('SPDX-License-Identifier','License'))):
            lic = returnMostAbundant(self.getAny('SPDX-License-Identifier','Licenses'),['',None,False,True])
            self.lineTrack['SPDX-License-Identifier']['lic'] = lic
            self.fileInfo['license'] = lic
            
class contractVariablesManager:
    def __init__(self, current_file_path, lineTrack={}, lines=None):
        self.slash = '//' if '//' in os.getcwd() else '/'
        self.currFilePath = current_file_path
        self.currFileDir = os.path.dirname(self.currFilePath)
        self.fileName = os.path.basename(self.currFilePath)
        self.lines = lines or readLines(self.currFilePath)
        self.lineTrack = lineTrack or {}
        self.lineTrackPath = os.path.join(self.currFileDir, 'lineTrack.json')
        self.allLines = []
        self.imports = os.path.join(self.currFileDir, 'imports')
        os.makedirs(self.imports, exist_ok=True)
        self.syntax = get_syntax_info()
        self.allLinesParse()
        self.getInitialVars()

    def checkAttributeValue(self, attr):
        try:
            value = getattr(self, attr)
            return value
        except:
            return False

    def ifInLines(self, x, ls):
        for k in range(0, len(ls)):
            if ls[k] < len(self.lines):
                if self.lines[ls[k]] == x:
                    return True
        return False

    def SPDXLines(self, line, i):
        self.addLines('SPDX-License-Identifier', i)
        self.lineTrack['SPDX-License-Identifier']["License"].append(
            line.split('SPDX-License-Identifier:')[1].replace(' ', '').replace('\n', ''))

    def getPragLines(self, line, i):
        self.addLines('pragma solidity', i)
        self.lineTrack['pragma solidity']["prags"].append(
            line.split('pragma solidity ')[1].split(';')[0].replace(' ', ''))

    def queryFunctions(self, line, i):
        self.addLines('function', i)
        funcDoc = os.path.join(self.currFileDir, 'Functions.json')
        if os.path.isfile(funcDoc) == False:
            write_to_file(contents={}, file_path=funcDoc)
        funcVars = safe_read_from_json(funcDoc)
        name = safeSplit2(line, '(', 0)
        name = safeSplit2(name, ' ', 1)
        vis = ListInString(line, self.syntax["visibility"])
        mod = ListInString(line, self.syntax["modifiers"])
        if vis == None or len(vis) == 0:
            vis = ['public']
        if mod == None or len(mod) == 0:
            mod = ['view']
        mod, vis = mod[0], vis[0]
        if vis not in funcVars:
            funcVars[vis] = {}
        if mod not in funcVars[vis]:
            funcVars[vis][mod] = []
        if 'names' not in funcVars:
            funcVars['names'] = []
        if name not in funcVars[vis][mod]:
            funcVars[vis][mod].append(name)
            funcVars['names'].append(name)
            self.lineTrack['function']["names"] = name
        safe_dump_to_file(data=funcVars, file_path=funcDoc)

    def queryLibrariesUse(self, line, i):
        name = str(line.split('using ')[1].split(' ')[0])
        use = str(line.split(' ')[-1].split(';')[0])
        self.lineTrack['library']['names'] = ThenAppend(
            self.lineTrack['library']['names'], name)
        if str(name) not in self.lineTrack['library']:
            self.lineTrack['library'][name] = {
                'attributes': {}, "address": "", "undeclared": "1"}
            self.importCheck('library', name)
        if 'library' not in self.lineTrack[self.current][self.lineTrack[self.current]['names'][-1]]['attributes']:
            self.lineTrack[self.current][self.lineTrack[self.current]
                                         ['names'][-1]]['attributes']['library'] = []
        self.lineTrack[self.current][self.lineTrack[self.current]
                                     ['names'][-1]]['attributes']['library'].append(name)

    def queryLibraries(self, line, i):
        if 'using ' in line:
            self.queryLibrariesUse(line, i)
            return
        self.addLines('library', i)
        name = str(line.split('library ')[1].split(' ')[0])
        self.lineTrack['library']['names'] = ThenAppend(
            self.lineTrack['library']['names'], name)
        if str(name) not in self.lineTrack['library']:
            self.lineTrack['library'][name] = {
                'attributes': {}, "address": "", "undeclared": "0"}
            self.importCheck('library', name)
        self.lineTrack['library'][name]["undeclared"] = "0"

    def queryContracts(self, line, i):
        self.addLines('contract', i)
        self.lineTrack['contract']['names'].append(
            eatOuter(line, ['\n', '\t', ' ', '/', ';']).split(' ')[1])
        if str(self.lineTrack['contract']['names'][-1]) not in self.lineTrack['contract']:
            self.lineTrack['contract'][str(self.getAny(
                'contract', 'names')[-1])] = {'address': "", "attributes": {}, "undeclared": "1"}
            if str(self.lineTrack['contract']['names'][-1]) != self.fileName:
                self.importCheck('contract', str(
                    self.lineTrack['contract']['names'][-1]))
        if ' is ' in line:
            self.lineTrack['contract'][str(self.getAny('contract', 'names')[-1])]['attributes'] = self.checkAtts(
                self.lineTrack['contract'][str(self.getAny('contract', 'names')[-1])]['attributes'], checkIsList(self.getAtts(line)))

    def queryAbstract(self, line, i):
        self.addLines('abstract contract', i)
        self.lineTrack['abstract contract']['names'].append(
            eatOuter(line, ['\n', '\t', ' ', '/', ';']).split(' ')[2])
        if str(self.lineTrack['abstract contract']['names'][-1]) not in self.lineTrack['abstract contract']:
            self.lineTrack['abstract contract'][str(
                self.lineTrack['abstract contract']['names'][-1])] = {'address': "", "attributes": {}, "name": ""}
            self.importCheck('abstract contract', str(
                self.lineTrack['abstract contract']['names'][-1]))
        if ' is ' in line:
            self.lineTrack['abstract contract'][str(self.lineTrack['abstract contract']['names'][-1])]['attributes'] = self.checkAtts(
                self.lineTrack['abstract contract'][str(self.lineTrack['abstract contract']['names'][-1])]['attributes'], checkIsList(self.getAtts(line)))

    def queryInterface(self, line, i):
        self.addLines('interface', i)
        self.lineTrack['interface']['names'].append(
            eatOuter(line, ['\n', '\t', ' ', '/', ';']).split(' ')[1])
        if str(self.lineTrack['interface']['names'][-1]) not in self.lineTrack['interface']:
            self.lineTrack['interface'][str(self.lineTrack['interface']['names'][-1])] = {
                'address': "", "attributes": {}, "undeclared": "1"}
            self.importCheck('interface', str(
                self.lineTrack['interface']['names'][-1]))
        if ' is ' in line:
            self.lineTrack['interface'][str(self.lineTrack['interface']['names'][-1])]['attributes'] = self.checkAtts(
                self.lineTrack['interface'][str(self.lineTrack['interface']['names'][-1])]['attributes'], checkIsList(self.getAtts(line)))

    def queryConstructorData(self, line, i):
        self.addLines('constructor', i)
        if len(self.getAny('contract', 'names')) != 0:
            contractName = self.getAny('contract', 'names')[-1]

            self.lineTrack['contract'][contractName]["constructor"] = {"attributes": [
            ], "constVariables": [], "type": [], "variables": [], "deployerVars": {}, "input": []}
            if len(self.lineTrack['constructor']['lines']) > 0:
                if 'constructor(' in self.lines[self.getAny('constructor', 'lines')[-1]]:
                    const = self.lines[self.getAny(
                        'constructor', 'lines')[-1]].split('constructor(')[1].split(')')[0].split(',')
                    for i in range(0, len(const)):
                        con = const[i].split(' ')
                        if len(con) == 2:
                            self.lineTrack['contract'][contractName]["constructor"]["attributes"].append(
                                con[0])
                            self.lineTrack['contract'][contractName]["constructor"]["constVariables"].append(
                                con[-1])
                        else:
                            self.lineTrack['contract'][contractName]["constructor"]["attributes"].append(
                                con[0])
                            co = ''
                            for k in range(1, len(con)-1):
                                co = co + con[k]
                            self.lineTrack['contract'][contractName]["constructor"]["type"].append(
                                co)
                            self.lineTrack['contract'][contractName]["constructor"]["constVariables"].append(
                                con[-1])
            if len(self.lineTrack['constructor']['lines']) > 0 and len(self.lineTrack['contract']['lines']) > 0:
                constructor = stopWhenClosed(linesToString(
                    self.lines[self.lineTrack['constructor']['lines'][-1]:]), ['{', '}'])
                constructor = constructor.replace(
                    constructor.split('{')[0]+'{', '')[:-1]
                constructor = eatAll(constructor, ['\n', '\t', ' ', '/', ','])
                constructor = constructor.replace(
                    ';', ';^^^***').split('^^^***')
                for c in range(0, len(self.lineTrack['contract'][contractName]["constructor"]["attributes"])):
                    if '[]' in self.lineTrack['contract'][contractName]["constructor"]["attributes"][c]:
                        higher = self.lineTrack['contract'][contractName]["constructor"]["attributes"][c].split('[')[
                            1].split(']')[0]
                        if len(higher) == 0:
                            higher = 1
                        for i in range(0, len(constructor)):
                            ls = ['interface', 'abstract contract']
                            if '=' in constructor[i]:
                                var = constructor[i].split('=')[0].replace(
                                    '\n', '').replace('\t', '')
                                eq = constructor[i].split('=')[1].replace(
                                    '\n', '').replace('\t', '')
                                if '0x' in eq:
                                    self.lineTrack['contract'][contractName]["constructor"][str(
                                        var.replace(' ', ''))] = {"address": str(eq.split('0x')[1][:len('')])}
                            for kk in range(0, len(ls)):
                                abstractLs = ListInString(
                                    constructor[i], self.lineTrack[ls[kk]]['names'])
                                if len(abstractLs) != None:
                                    for k in range(0, len(abstractLs)):
                                        spl = constructor[i].split(
                                            abstractLs[k]+'(')
                                        self.lineTrack[ls[kk]][abstractLs[k]]['name'] = str(eatAll(spl[0].split('=')[0].replace(
                                            ' ', '').replace('\n', '').replace('\t', ''), ['\n', '\t', ' ', '/', ',']))
                                        self.lineTrack[ls[kk]][abstractLs[k]]['address'] = spl[1].split(
                                            ')')[0].replace('\n', '').replace('\t', '')
                            if self.lineTrack['contract'][contractName]["constructor"]["constVariables"][c]+'[' in constructor[i]:
                                constInt = constructor[i].split(self.lineTrack['contract'][contractName]["constructor"]["constVariables"][c]+'[')[
                                    1].split(']')[0].replace('\n', '').replace('\t', '')
                                if isinstance(constInt,int):
                                    higher = getHigher(constInt, higher)
                                else:
                                    newInt = detNumInWhile(
                                        constInt, constructor, i)
                                    if newInt != None:
                                        higher = getHigher(newInt, higher)

                            self.lineTrack['contract'][contractName]["constructor"]["attributes"][c] = self.lineTrack[
                                'contract'][contractName]["constructor"]["attributes"][c].split('[')[0]+'['+str(higher)+']'
        if ' is ' in line:
            if str(self.lineTrack['contract']['names'][-1]) not in self.lineTrack['contract']:
                self.lineTrack['constructor'][str(
                    self.lineTrack['constructor']['lines'][-1])] = {"attributes": {}}
            self.lineTrack['constructor'][str(self.lineTrack['constructor']['lines'][-1])]['attributes'] = self.checkAtts(
                self.lineTrack['constructor'][str(self.lineTrack['constructor']['lines'][-1])]['attributes'], checkIsList(self.getAtts(line)))

    def getInitialVars(self):
        self.lineTrack['variables'] = {'rndm': [], 'address': {"list": [], "single": []}, 'uint': {"list": [], "single": [
        ]}, 'string': {"list": [], "single": []}, 'bool': {"list": [], "single": []}, 'bytes': {"list": [], "single": []}}
        contract_lines = self.lineTrack['contract']['lines']
        constVars = []
        if contract_lines:
            constVars = self.lines[contract_lines[-1]+1:getJustHigher(
                contract_lines[-1], self.lineTrack['function']['lines'])]
        constructor_lines = self.lineTrack['constructor']['lines']
        if ifBothOverZero(contract_lines, constructor_lines) == True:
            self.lines[contract_lines[-1]+1:constructor_lines[-1]]
        lsN = []
        for i in range(0, len(constVars)):
            n = constVars[i]
            if self.ifInLines(n, self.allLines) == False:
                lsN.append(n)
        constVars = lsN
        typesVars = ['address', 'uint', 'string', 'bool']
        while isAboveZero(constVars) == True:
            n=constVars
            if isinstance(n,list) and n:
                n=n[0]
            n = eatAll(n, ['\n', '\t', ' ', '/', ',', ';'])
            while 'struct' in n and isAboveZero(constVars) == True:
                constVars = stopWhenClosedRemove(constVars, ['{', '}'])
                n=constVars
                if isinstance(n,list) and n:
                    n=n[0]
                n = eatAll(n, ['\n', '\t', ' ', '/', ',', ';'])
            if '=' in n:
                n = n.split('=')
                nA = eatAll(n[0], ['\n', '\t', ' ', '/', ',', ';'])
                lsN = ListInString(eatAll(
                    nA[0], ['\n', '\t', ' ', '/', ',', ';']), ['address', 'uint', 'string', 'bool'])
                nB = eatAll(n[-1], ['\n', '\t', ' ', '/', ',', ';'])
                if len(lsN) != 0:
                    if '[' in nA:
                        self.lineTrack['variables'][lsN[0]
                                                    ]['list'].append(nA[-1])
                    else:
                        self.lineTrack['variables'][lsN[0]
                                                    ]['single'].append(nA[-1])
                else:
                    self.lineTrack['variables']['rndm'].append(n)
                    self.importCheck(
                        ['interface', 'abstract contract', 'library', 'contract'], n)
            else:
                n = n.split(' ')
                lsN = []
                for i in range(0, len(n)):
                    if n[i] != '':
                        lsN.append(n[i])
                inpu = False
                for k in range(0, len(lsN)):
                    nn = eatAll(lsN[k], ['\n', '\t', ' ', '/', ',', ';'])
                    inLs = ListInString(
                        nn, ['address', 'uint', 'string', 'bool'])
                    if len(inLs) != 0:
                        if '[' in nn:
                            self.lineTrack['variables'][inLs[0]
                                                        ]['list'].append(n[-1])
                        else:
                            self.lineTrack['variables'][inLs[0]
                                                        ]['single'].append(n[-1])
                        inpu = True
                if inpu == False:
                    if n[0] in self.lineTrack['abstract contract']['names']:
                        self.lineTrack['abstract contract'][str(
                            n[0])]['name'] = str(n[-1])
                    elif n[0] in self.lineTrack['interface']['names']:
                        self.lineTrack['interface'][str(
                            n[0])]['name'] = str(n[-1])
                    else:
                        self.lineTrack['variables']['rndm'].append(n)
                        self.importCheck(
                            ['interface', 'abstract contract', 'library', 'contract'], n)
            constVars = constVars[1:]
            safe_dump_to_file(data=self.lineTrack,
                              file_path=self.lineTrackPath)
        return self.lineTrack

    def getAtts(self, x):
        atts = x.split(' is ')[1].split('{')[0].replace(' ', '')
        if ',' in atts:
            atts = atts.split(',')
        return atts

    def findAtts(self, js, ls):
        names = ['contract', 'abstract contract', 'interface']
        ls, lsN = checkLsAndGetNew(ls)
        for i in range(0, len(ls)):
            lsN.append(False)
        for i in range(0, len(names)):
            name = names[i]
            for k in range(0, len(ls)):
                if stringInList(ls[k], self.getNames(name)) == True:
                    if name not in js:
                        js[name] = []
                    js[name] = ThenAppend(js[name], ls[k])
                    lsN[k] = True
        return lsN

    def checkAtts(self, js, ls):
        if ls == None:
            return
        lsN = self.findAtts(js, ls)
        for i in range(0, len(lsN)):
            if lsN[i] == False:
                importCheck(ls[i], self.getAtts(lines[self.currLine]))

        return js

    def addLines(self, st, i):
        self.lineTrack[st]['lines'].append(i)
        self.allLines.append(i)

    def getAny(self, st, st2):
        return self.lineTrack[st][st2]

    def getAnys(self, st, st2):
        return self.lineTrack[st][st2]

    def getNames(self, st):
        return self.lineTrack[st]['names']

    def getCurrPrag(self):
        if len(self.getAny('pragma solidity', 'prags')) > 0:
            return self.getAny('pragma solidity', 'prags')[-1]
        else:
            return '^0.8.0'

    def importCheck(self, name, st):
        st = checkIsList(st)
        pra = pragmaVerSplit(self.getCurrPrag())
        verPath = os.path.join(os.getcwd(), 'variables/pragmas/', str(pra))
        for each in verPath:
            verPath
        os.makedirs(verPath, exist_ok=True)
        pragFold = os.listdir(verPath)
        for i in range(0, len(pragFold)):
            namePath = os.path.join(verPath, pragFold[i])
            for item in os.listdir(namePath):
                item_path = os.path.join(namePath, item)
                if os.path.isdir(item_path):
                    contextfold = os.listdir(item_path)
                    for name in st:
                        sol_file = name+'.sol'
                        if sol_file in contextfold and sol_file not in os.listdir(self.imports):
                            finalPath = os.path.join(item_path, sol_file)
                            file_path = os.path.join(self.imports, sol_file)
                            write_to_file(contents=read_from_file(
                                finalPath), file_path=file_path)

    def allLinesParse(self):
        """
        Iterates through each line in the contract, cleans it of unwanted characters, and sends it for further processing.
        """
        self.lineTrack['SPDX-License-Identifier'] = {
            "lines": [], "Licenses": [], "License": [], "lic": ""}
        self.lineTrack['pragma solidity'] = {
            "lines": [], "range": [], "prags": [], "pragma": ""}
        self.lineTrack['function'] = {"lines": [], 'names': []}
        self.lineTrack['library'] = {"lines": [], 'names': []}
        self.lineTrack['contract'] = {"lines": [], 'names': []}
        self.lineTrack['abstract contract'] = {"lines": [], 'names': []}
        self.lineTrack['interface'] = {"lines": [], 'names': []}
        self.lineTrack['constructor'] = {"lines": [], 'names': []}
        safe_dump_to_file(data={}, file_path=os.path.join(
            self.currFileDir, 'Functions.json'))

        for i, line in enumerate(self.lines):
            line = eatAll(line, ['\n', '\t', ' ', '/'])
            self.sendIfs(line, i)

    def saveSect(self, st, i):
        """
        Generates a file with the appropriate sections of a contract, makes necessary directories, and saves the contract info into corresponding files.
        """
        lic = 'None'
        if len(self.getAnys('SPDX-License-Identifier', "License")) != 0:
            lic = self.getAnys('SPDX-License-Identifier', "License")[-1]
        pragma = self.getCurrPrag()
        title = self.getNames(st)[-1]+'.sol'

        pragFold = pragmaVerSplit(pragma)
        pragmaFold = os.path.join(os.getcwd(), 'variables/pragmas', pragFold)
        os.makedirs(pragmaFold, exist_ok=True)
        pragmaSpec = os.path.join(pragmaFold, pragma).replace(
            self.slash+' ', self.slash+'')
        os.makedirs(pragmaSpec, exist_ok=True)

        headFold = os.path.join(pragmaSpec, st)
        os.makedirs(headFold, exist_ok=True)
        sectFold = os.path.join(headFold, title)
        create_and_read_file(file_path=sectFold)
        trackEm([pragFold, pragma, st, self.getNames(st)[-1], sectFold])
        contents = '//SPDX-License-Identifier: '+lic+'\npragma solidity '+pragma +';\n'
        when_closed = stopWhenClosed(linesToString(self.lines[i:]), ['{', '}'])
        if when_closed:
            contents+=when_closed
        write_to_file(contents=contents, file_path=sectFold)
        write_to_file(contents=read_from_file(sectFold),file_path=os.path.join(self.imports, title))

    def sendIfs(self, line, i):
        """
        Depending on the 'head' of the contract it directs processing to corresponding methods.
        """
        self.currLine = i
        heads = ['SPDX-License-Identifier', 'pragma solidity', 'library', 'using',
                 'contract', 'abstract contract', 'interface', 'constructor', 'function']
        saveLst = ['library', 'interface', 'contract',
                   'library', 'abstract contract']
        for head in heads:
            if isCurrent(line, head) == True:
                if head != 'using':
                    self.current = head
                if self.current == 'SPDX-License-Identifier':
                    self.SPDXLines(line, i)
                elif self.current == 'pragma solidity':
                    self.getPragLines(line, i)
                elif self.current == 'library':
                    self.queryLibraries(line, i)
                elif self.current == 'using':
                    self.queryLibrariesUse(line, i)
                elif self.current == 'contract':
                    self.queryContracts(line, i)
                elif self.current == 'abstract contract':
                    self.queryAbstract(line, i)
                elif self.current == 'interface':
                    self.queryInterface(line, i)
                elif self.current == 'constructor':
                    self.queryConstructorData(line, i)
                elif self.current == 'function':
                    self.queryFunctions(line, i)
                if self.current in saveLst:
                    self.saveSect(self.current, i)
def getInitialVars(lines, lineTrack, allLines):
    """
    Handles the initial extraction and managing of various types of variables and essential information from a smart contract, such as page directives, 'pragma solidity', and import statements. This function works with specific data types, such as 'address', 'uint', 'string', 'bool', etc., but also leaves room for flexibility with a 'random' category. It also performs implicit checks for necessary resources and carefully scans dependencies, reducing the risk of errors in the smart contract deployment process.
    """
    def getAny(lineTrack, st, st2):
        return lineTrack[st][st2]

    def pragmaVerSplit(x):
        return safeSplit(x, '.', 1)

    def getCurrPrag(lineTrack):
        if len(getAny(lineTrack, 'pragma solidity', 'prags')) > 0:
            return getAny(lineTrack, 'pragma solidity', 'prags')[-1]
        else:
            return '^0.8.0'

    def importCheck(lineTrack, name, st):
        st = checkIsList(st)
        pra = pragmaVerSplit(getCurrPrag(lineTrack))
        verPath = os.path.join(os.getcwd(), 'variables/pragmas/', str(pra))
        for each in verPath:
            verPath

        pragFold = os.listdir(verPath)
        for i in range(0, len(pragFold)):
            namePath = os.path.join(verPath, pragFold[i])
            for item in os.listdir(namePath):
                item_path = os.path.join(namePath, item)
                if os.path.isdir(item_path):
                    contextfold = os.listdir(item_path)
                    for name in st:
                        sol_file = name+'.sol'
                        if sol_file in contextfold and sol_file not in os.listdir(imports):
                            print(name, st)
                            finalPath = os.path.join(item_path, sol_file)
                            write_to_file(contents=read_from_file(
                                finalPath), file_path=os.path.join(imports, sol_file))

    lineTrack['variables'] = {'rndm': [], 'address': {"list": [], "single": []}, 'uint': {"list": [], "single": []}, 'string': {"list": [], "single": []}, 'bool': {"list": [], "single": []}, 'bytes': {"list": [], "single": []}}
    contract_lines = lineTrack['contract']['lines']
    constVars = []
    if contract_lines:
        constVars = lines[contract_lines[-1] + 1:getJustHigher(contract_lines[-1], lineTrack['function']['lines'])]
    constructor_lines = lineTrack['constructor']['lines']
    if ifBothOverZero(contract_lines, constructor_lines) == True:
        lines[contract_lines[-1]+1:constructor_lines[-1]]
    lsN = []
    for i in range(0, len(constVars)):
        n = constVars[i]
        if ifInLines(lines, n, allLines) == False:
            lsN.append(n)
    constVars = lsN
    typesVars = ['address', 'uint', 'string', 'bool']
    while isAboveZero(constVars) == True:
        n=constVars
        if isinstance(n,list) and n:
            n=n[0]
        n = eatAll(n, ['\n', '\t', ' ', '/', ',', ';'])
        while 'struct' in n and isAboveZero(constVars) == True:
            constVars = stopWhenClosedRemove(constVars, ['{', '}'])
            n=constVars
            if isinstance(n,list) and n:
                n=n[0]
            n = eatAll(n, ['\n', '\t', ' ', '/', ',', ';'])
        if '=' in n:
            n = n.split('=')
            nA = eatAll(n[0], ['\n', '\t', ' ', '/', ',', ';'])
            lsN = ListInString(eatAll(
                nA[0], ['\n', '\t', ' ', '/', ',', ';']), ['address', 'uint', 'string', 'bool'])
            nB = eatAll(n[-1], ['\n', '\t', ' ', '/', ',', ';'])
            if len(lsN) != 0:
                if '[' in nA:
                    lineTrack['variables'][lsN[0]]['list'].append(nA[-1])
                else:
                    lineTrack['variables'][lsN[0]]['single'].append(nA[-1])
            else:
                lineTrack['variables']['rndm'].append(n)
                importCheck(
                    lineTrack, ['interface', 'abstract contract', 'library', 'contract'], n)
        else:
            n = n.split(' ')
            lsN = []
            for i in range(0, len(n)):
                if n[i] != '':
                    lsN.append(n[i])
            inpu = False
            for k in range(0, len(lsN)):
                nn = eatAll(lsN[k], ['\n', '\t', ' ', '/', ',', ';'])
                inLs = ListInString(nn, ['address', 'uint', 'string', 'bool'])
                if len(inLs) != 0:
                    if '[' in nn:
                        lineTrack['variables'][inLs[0]]['list'].append(n[-1])
                    else:
                        lineTrack['variables'][inLs[0]]['single'].append(n[-1])
                    inpu = True
            if inpu == False:
                if n[0] in lineTrack['abstract contract']['names']:
                    lineTrack['abstract contract'][str(
                        n[0])]['name'] = str(n[-1])
                elif n[0] in lineTrack['interface']['names']:
                    lineTrack['interface'][str(n[0])]['name'] = str(n[-1])
                else:
                    lineTrack['variables']['rndm'].append(n)
                    importCheck(
                        lineTrack, ['interface', 'abstract contract', 'library', 'contract'], n)
        constVars = constVars[1:]
        safe_dump_to_file(data=lineTrack, file_path='lineTrack.txt')
        return lineTrack
class ContractDeployer:
    def __init__(self, home_folder=None):
        self.section_key='DEPLOYER'
        self.varisPath=None
        self.home = home_folder or os.getcwd()
        self.slash = '//' if '//' in self.home else '/'
        self.last = home_folder or self.home
        self.lineTrack, self.allLines, self.lines, self.last = {}, [], [], self.home
        self.createFolders()
        self.syntax = get_syntax_info()
        self.determineEndPoint()
        
    def checkAttributeValue(self, attr):
        try:
            value = getattr(self, attr)
            return value
        except:
            return False

    def createFolders(self, home_folder=None):
        folders = ['variables', 'deployHist', 'current']
        for folder in folders:
            setattr(self, folder+'Dir', existFoldCheck(self.home, folder))
        self.projectsDir= make_dir(self.home, 'deployHist', 'projects')

    def determineEndPoint(self):
        self.createFolders()
        abstract_browser.initiate_browser_window(extra_buttons=self.createNewProject(),event_handlers=[self.startWhere],exit_events=[],section=self.section_key)
        
        keepItUp = True
        while keepItUp == True:
            allFiles, choice = self.returnLen()
            if choice == 'addAnother':
                self.getItGoing()
                compileNeeds()
            else:
                keepItUp = False
        if self.varisPath:
            safe_dump_to_file(safe_read_from_json(self.varisPath),os.path.join(self.home, 'current', 'varis.py'))
        if allFiles:
            return allFiles
    def chooseExisting(self):
        self.existing_projects = os.listdir(self.projectsDir)
        return sg.Frame('choose existing:',layout=ensure_nested_list([make_component("Combo",self.existing_projects,value=self.existing_projects[0],key='existing_projects',size=(25,15),enable_events=True),
                                                                      sg.Button('Choose')]))
                                                                    
    def createNewProject(self):
        return [[sg.Frame('what would you like to call the new project?',layout=ensure_nested_list([make_component("Input",key='projectName',enable_events=True,**expandable())])),
                 self.chooseExisting()],
                [sg.Button('Input'),sg.Button('Exit'),sg.Button('Done'),sg.Submit(button_text="addNew")]
                ]
    def startWhere(self,event,values,window):
        if event == 'Done':
            
            self.projectName=create_new_name(name=values['projectName'],names_list=self.existing_projects)
            self.projectDirectory = make_dir(os.path.join(self.projectsDir,self.projectName))
            file_paths = abstract_browser.files_list_mgr.get_file_path_list(key=self.section_key)
            self.project_variables = {"project_name":self.projectName,'project_directory':self.projectDirectory,'contracts':{}}
            
            for original_file_path in file_paths:
                file_name = os.path.basename(original_file_path)
                name = os.path.splitext(file_name)[0]
                self.fileName=file_name
                current_file_directory = make_dir(self.projectDirectory,name)
                imports_directory = make_dir(current_file_directory,'imports')
                alls_file_path = os.path.join(imports_directory, 'alls.txt')
                create_and_read_file(file_path=alls_file_path, contents='')
                info_file_path = os.path.join(current_file_directory, 'info.json')
                current_file_path=os.path.join(current_file_directory,file_name)
                CopyOriginalFile(current_file_path, original_file_path)
                self.currFileDir=current_file_directory
                self.fileInfo={"file_name":file_name,
                              'current_file_directory':current_file_directory,
                              'current_file_path':current_file_path,
                              'current_imports_directory':imports_directory,
                              'current_alls_path':alls_file_path,
                              'info_file_path':info_file_path,
                              "original_file_path":original_file_path,
                              'original_file_directory':os.path.dirname(original_file_path),
                              'lines':readLines(current_file_path),
                              "contract_address": "",
                              "api": "",
                              "pragma": [],
                              "license": "",
                              "args": "",
                              "version": "",
                              "variableNames": "",
                              'allVarsTrack': {}}
                self.fileInfo=self.getTheVars(self.fileInfo)
                self.lineTrack = getInitialVars(self.fileInfo['lines'], self.lineTrack, self.allLines)
                self.pragmaSpec = str(self.fileInfo['allVarsTrack']['pragma solidity']['pragma'])
                self.makeConstructors()
                self.createFiles()
                resetArtifactsAndCache()
                safe_dump_to_file(file_path=info_file_path, data=self.fileInfo)
                self.project_variables['contracts'][name]=self.fileInfo
        elif event == 'Choose':
            self.varisPath=os.path.join(self.projectsDir,values['existing_projects'][0],'varis.py')
            self.retrieveVarisInfo()
        elif event == 'current':
            self.currentDeployed() 
        return 

    def NewProjectDir(self, extra_string=''):
        def get_string(extra_string=''):
            string = "what would you like to name the new batch?"
            if extra_string:
                string = extra_string+'\n'+string
            return string

        project_name = gui_input(get_string(extra_string=extra_string))
        while project_name in os.listdir(self.projectsDir):
            extra_string = f'the name {project_name} already exists in the projects directory'
            project_name = gui_input(get_string(extra_string=extra_string))
        return project_name

    def retrieveVarisInfo(self):
        self.varisNew = get_new_varis()
        self.varisInfo = create_and_read_json(
            file_path=self.varisPath, json_data=self.varisNew)
        
    def currentDeployed(self):
        self.createFolders()
        self.varisPath = os.path.join(self.currentDir, 'varis.py')
        self.varisInfo = safe_read_from_json(self.varisPath)
        self.currProjectDir = self.varisInfo["currProjectDir"]
        self.varisPath = os.path.join(self.currProjectDir, 'varis.py')

    def returnLen(self):
        self.retrieveVarisInfo()
        if len(self.varisInfo['files']) == 0:
            self.last = self.home
            return self.varisInfo['fileNames'], 'addAnother'
        return display_modular_listbox('this is your current deploy schedule:', self.varisInfo['fileNames'])

    def bulkUpdateVarisInfo(self):
        for key in list(self.varisInfo.keys()):
            if key[-1] == 's':
                value = self.checkAttributeValue(key[:-1])
                if value:
                    if value not in self.varisInfo[key]:
                        self.varisInfo[key].append(value)
            else:
                value = self.checkAttributeValue(key)
                if value:
                    self.varisInfo[key] = value

        safe_dump_to_file(file_path=self.varisPath, data=self.varisInfo)
        safe_dump_to_file(file_path=self.infoFilePath, data=self.fileInfo)

    def updateVarisInfo(string, x):
        if string in varisInfo:
            js = varisInfo[string]
            if type(js) is list:
                varisInfo[string] = ThenAppend(varisInfo[string], x)
            else:
                varisInfo[string] = x

        else:
            print(str(string), ' not in varisInfo')

    def getAny(self, st, st2):
        if self.lineTrack:
            return self.lineTrack[st][st2]

    def existWriteFileRead(self, x, y):
        if os.path.exists(y) == False:
            write_to_file(contents=x, file_path=y)
        return read_from_file(y).replace("'", '"')

    def makeConstructors(self):
        contName = self.getAny('contract', 'names')
        if contName:
            contName = contName[-1]
        self.isUnisEven(contName)

    def isUnisEven(self, na):
        if na:
            if "constructor" in self.lineTrack['contract'][na]:
                if "attributes" in self.lineTrack['contract'][na]["constructor"]:
                    n = self.lineTrack['contract'][na]["constructor"]["attributes"]
                    units = self.lineTrack['contract'][na]["constructor"]["input"]
                    lsConsts = create_and_read_json(
                        json_data=units, file_path=os.path.join(self.currFileDir, 'constVals.sol'))
                    lsVerify = []
                    if len(n) > len(units):
                        for i in range(len(units), len(n)):
                            if '[' in n[i]:
                                lsN = []
                                for c in range(0, int(n[i].split('[')[1].split(']')[0])):
                                    lsN.append(n[i].split('[')[0]+'['+str(c+1)+']')
                                    self.lineTrack['contract'][na]["constructor"]["input"].append(constAsk(n[i].split('[')[0]+'['+str(c+1)+']', n[i].split('[')[0], ifAble(lsConsts, c)))
                                    lsVerify.append(const_it([n[i].split('[')[0], self.lineTrack['contract'][na]["constructor"]["input"][-1]]))
                                self.lineTrack['contract'][na]["constructor"]["deployerVars"][n[i]] = lsN
                    self.fileInfo["args"] = lsVerify
                    # self.fileInfo["api"] = keys()

    def createFiles(self):
        self.pragmaSpec = str(
            self.fileInfo['allVarsTrack']['pragma solidity']['pragma'])
        write_to_file(contents=read_from_file(os.path.join(os.getcwd(), 'variables/samples/config_sample.txt').replace('^^killme^^', '{\n\tversion: "'+self.pragmaSpec+'",\n\tsettings: {\n\t\toptimizer: {\n\tenabled: true,\n\truns: 200\n\t}\n\t}\n\t},')),
                      file_path=os.path.join(self.currFileDir, 'hardhat.config.js'))
        write_to_file(contents='solc-select install '+self.pragmaSpec+'; solc-select use '+self.pragmaSpec+';  cd '+str(self.home)+'; npx hardhat run '+os.path.join(self.currFileDir, self.fileName+'_deploy.js')+' --network FUJI_avax;',
                      file_path=os.path.join(self.currFileDir, 'script.sh'))
        contents = self.lineTrack
        contName = None
        if self.lineTrack:
            contName = self.getAny('contract', 'names')
            if 'contract' in self.lineTrack:
                contents = self.lineTrack['contract']

        if contName:
            contName = contName[-1]
            if contName:
                contents = contents[contName]
        if contents:
            if 'constructor' in contents:
                contents = contents["constructor"]
            if 'input' in contents:
                contents = contents['input']
        contents_path = os.path.join(self.currFileDir, 'constVals.sol')
        if isinstance(contents, dict) or isinstance(contents, list):
            safe_dump_to_file(data=contents, file_path=contents_path)
        else:
            write_to_file(data=str(contents), file_path=contents_path)
        # contents=read_from_file(os.path.join(os.getcwd(),'variables/samples/deploy_sample.txt'))
        
        #contents = contents.replace(
        #    '^^0^^', 'require("@nomiclabs/hardhat-etherscan");')
        #contents = contents.replace(
        #    '^^1^^', self.fileName).replace('^^2^^', '')
        track = ''
        if self.lineTrack:
            track = self.lineTrack
            if 'contract' in track:
                track = track['contract']
                if 'names' in track:
                    track = track['names']
                    if len(track) > 0:
                        track = track[-1]
                        if 'contract' in track:
                            track = track['contract']
                            if 'input' in track:
                                track = track['input']
        contents = '''require("@nomiclabs/hardhat-etherscan");
const hre = require("hardhat");
async function main() {
  const Greeter = await hre.ethers.getContractFactory("'''+f"{self.fileName}"+'''");
  const greeter = await Greeter.deploy("'''+f"{track}"+'''");
  await greeter.deployed();
  console.log("Greeter deployed to:", greeter.address);
}
function link(bytecode, libName, libAddress) {
  let symbol = "__" + libName + "_".repeat(40 - libName.length - 2);
  return bytecode.split(symbol).join(libAddress.toLowerCase().substr(2))
}
main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });'''
        deploy_path = os.path.join(os.path.dirname(self.currFileDir), 'deploy')
        os.makedirs(deploy_path, exist_ok=True)
        file_path = os.path.join(deploy_path, self.fileName+'_deploy.js')
        write_to_file(file_path=file_path, contents=contents)
        chmodIt(file_path)

  
    def getTheVars(self,file_info):
        flatten_it(file_info['current_file_path'])
        self.lineTrack = contractVariablesManager(current_file_path=file_info['current_file_path'], lines=file_info['lines']).lineTrack
        pragmaVar_mgr = pragmaVariableManager(lineTrack=self.lineTrack, fileInfo=file_info)
        self.lineTrack = pragmaVar_mgr.lineTrack
        fileInfo = pragmaVar_mgr.fileInfo
        self.spdx_mgr = spdxManager(lineTrack=self.lineTrack, fileInfo=fileInfo, lines=file_info['lines'])
        self.lineTrack = self.spdx_mgr.lineTrack
        file_info = self.spdx_mgr.fileInfo
        fileInfo['allVarsTrack'] = self.lineTrack
        return fileInfo

    
ContractDeployer()
