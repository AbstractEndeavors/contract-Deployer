import os
import PySimpleGUI as sg
from abstract_utilities import eatOuter, eatAll, eatInner, read_from_file, write_to_file, create_and_read_json, safe_dump_to_file, safe_read_from_json


def get_syntax_info():
    return {"names": ["Modifiers", "Visibility", "precedence", "globalVariables", "precedence"],
            "Modifiers": ["pure", "view", "payable", "constant", "immutable", "anonymous", "indexed", "virtual", "override"],
            "precedence": ["assert", "block", "coinbase", "difficulty", "number", "block;number", "timestamp", "block;timestamp", "msg", "data", "gas", "sender", "value", "gas price", "origin", "revert", "require", "keccak256", "ripemd160", "sha256", "ecrecover", "addmod", "mulmod", "cryptography", "this", "super", "selfdestruct", "balance", "codehash", "send"],
            "visibility": ["public", "private", "external", "internal"],
            "modifiers": ["pure", "view", "payable", "constant", "anonymous", "indexed"],
            "globalVariables": ['abi.decode(bytes memory encodedData, (...)) returns (...)', 'abi.encode(...) returns (bytes memory)', 'abi.encodePacked(...) returns (bytes memory)',  'abi.encodeWithSelector(bytes4 selector, ...) returns (bytes memory)', 'abi.encodeCall(function functionPointer, (...)) returns (bytes memory)', 'abi.encodeWithSelector(functionPointer.selector, (...))', 'abi.encodeWithSignature(string memory signature, ...) returns (bytes memory)', 'to abi.encodeWithSelector(bytes4(keccak256(bytes(signature)), ...)', 'bytes.concat(...) returns (bytes memory)', 'arguments to one byte array<bytes-concat>`', 'string.concat(...) returns (string memory)', 'arguments to one string array<string-concat>`', 'block.basefee (uint)', 'block.chainid (uint)', 'block.coinbase (address payable)', 'block.difficulty (uint)', 'block.gaslimit (uint)', 'block.number (uint)', 'block.timestamp (uint)', 'gasleft() returns (uint256)', 'msg.data (bytes)', 'msg.sender (address)', 'msg.sig (bytes4)', 'msg.value (uint)', 'tx.gasprice (uint)', 'tx.origin (address)', 'assert(bool condition)', 'require(bool condition)', 'for malformed input or error in external component)', 'require(bool condition, string memory message)', 'condition is false (use for malformed input or error in external component). Also provide error message.', 'revert()', 'revert(string memory message)', 'blockhash(uint blockNumber) returns (bytes32)', 'keccak256(bytes memory) returns (bytes32)', 'sha256(bytes memory) returns (bytes32)', 'ripemd160(bytes memory) returns (bytes20)', 'ecrecover(bytes32 hash, uint8 v, bytes32 r, bytes32 s) returns (address)', 'the public key from elliptic curve signature, return zero on error', 'addmod(uint x, uint y, uint k) returns (uint)', 'arbitrary precision and does not wrap around at 2**256. Assert that k != 0 starting from version 0.5.0.', 'mulmod(uint x, uint y, uint k) returns (uint)', 'with arbitrary precision and does not wrap around at 2**256. Assert that k != 0 starting from version 0.5.0.', "this (current contract's type)", 'super', 'selfdestruct(address payable recipient)', '<address>.balance (uint256)', '<address>.code (bytes memory)', '<address>.codehash (bytes32)', '<address payable>.send(uint256 amount) returns (bool)', 'returns false on failure', '<address payable>.transfer(uint256 amount)', 'type(C).name (string)', 'type(C).creationCode (bytes memory)', 'type(C).runtimeCode (bytes memory)', 'type(I).interfaceId (bytes4)', 'type(T).min (T)', 'type(T).max (T)'], "sectionHeader": ['contract', 'library', 'interface', 'abstract contract'], "allVars": ['contract', 'library', 'pragma solidity', 'import', 'interface', 'abstract contract', 'constructor', 'function', 'modify', 'SPDX-License-Identifier']}


def ifBothOverZero(x, y):
    if len(x) > 0 and len(y) > 0:

        return True
    return False


def isAboveZero(x):
    if len(x) < 2:
        return False
    return True


def getJustHigher(k, ls):
    for i in range(0, len(ls)):
        if ls[i] > k:
            return ls[i]


def ListInString(string, ls):
    ls = checkIsList(ls)
    lsN = []
    for obj in ls:
        if obj in string:
            lsN.append(obj)
    return lsN


def create_and_read_file(file_path, contents=''):
    if os.path.isfile(file_path):
        contents = read_from_file(file_path)
    else:
        write_to_file(file_path=file_path, contents=contents)
    return contents


def checkIsList(ls):
    if not isinstance(ls, list):
        ls = [ls]
    return ls


def linesToString(ls):
    ls = checkIsList(ls)
    return ''.join(ls)


def safeSplit(x, y, i):
    good = False
    while good == False:
        if str(y) in x:
            x = x.split(str(y))
            if i <= len(x)-1:
                return x[i]
            else:
                ask = create_ask(createPrintList(
                    x), 'looks like you entered '+str(i)+' that was too big, what were you looking for?')
                return x[ask]
        else:
            print('that split was not in the variable')
            return x


def checkLsAndGetNew(ls):
    return checkIsList(ls), []


def pragmaVerSplit(x):
    return safeSplit(x, '.', 1)


def stringInLists(x, lss):
    lss, lsN = checkLsAndGetNew(lss)
    for i in range(0, len(lss)):
        lssN = checkIsList(lss[i])
        for k in range(0, len(lssN)):
            if x in lssN:
                lsN.append(findIt(x, lssN))
    return lsN


def detNumInWhile(x, string, k):
    lenget = k
    for i in range(0, len(string)):
        found = ListInString(string[lenget], ['for', 'while'])
        if len(found) > 0:
            nn = ''
            n = str(stopWhenClosed(linesToString(string[lenget:]), ['(', ')'])).replace(
                ' ', '').replace('\n', '').replace('\t', '')
            n = n.split('(')[1].split(')')[0].split(';')
            nowIntA = n[0].split('=')[1]
            found = ListInString(n[1], ['=<', '<', '>', '>=', '=', '^'])
            nowIntB = n[1].split(found[0])[1]
            if found[0] == '<':
                nowIntB = int(nowIntB) - 1
            return nowIntB
        lenget -= 1


def stringInList(x, ls):
    if ls == None:
        return False
    ls, lsN = checkLsAndGetNew(ls)
    if len(ls) == 0:
        return False
    for i in range(0, len(ls)):
        if x == ls[i]:
            return True
    return False


def ThenAppend(js, x):
    if x not in js:
        js.append(x)
    return js


def countIt(x, y):
    return (len(x)-len(x.replace(y, '')))/len(y)


def isCurrent(x, y):
    if x[:len(y)] == y:
        return True
    return False


def safeSplit2(x, y, k):
    if y in x:
        x = x.split(y)
        if len(x) >= int(k):
            return x[k]
    return x


def isInList(x, ls):
    newLs = []
    for i in range(0, len(ls)):
        n = ls[i]
        nn = ''
        for k in range(0, len(n)):
            nn = nn + n[k]
        if str(x) == str(nn):
            newLs.append(n)
    return len(newLs), newLs


def stopWhenClosed(x, ls):
    ls = checkIsList(ls)
    for i in range(0, len(x)):
        y = x[0:i]
        lenLs = [countIt(y, str(ls[0])), countIt(y, str(ls[1]))]
        if lenLs[0] == lenLs[1] and lenLs[0] != 0:
            return y
    return False


def stopWhenClosedI(x, ls):
    ls = checkIsList(ls)
    x = linesToString(x)
    for i in range(0, len(x)):
        y = x[0:i]
        lenLs = [countIt(y, str(ls[0])), countIt(y, str(ls[1]))]
        if lenLs[0] == lenLs[1] and lenLs[0] != 0:
            return
    return y+'\n}'


def readLinesSpec(x):
    lsN = []
    lines = x.split('\n')
    for i in range(0, len(lines)):
        lines[i] = eatOuter(lines[i], ['\n', '\t', ' ', '']).replace('\n', '')
        if lines[i] not in ['\n', ' \n', '', ' ', '\t'] and len(str(eatAll(lines[i], ['\n', '\t', ' ', '/', ';', '']))) != 0:
            lsN.append(lines[i]+'\n')
    return lsN


def stopWhenClosedRemove(x, ls):
    ogX = len(x)
    ls = checkIsList(ls)
    x = linesToString(x)
    for i in range(0, len(x)):
        y = x[0:i]
        lenLs = [countIt(y, str(ls[0])), countIt(y, str(ls[1]))]
        if lenLs[0] == lenLs[1] and lenLs[0] != 0:
            return readLinesSpec(x)[len(readLinesSpec(y)):]


def getFullSection(x):
    return stopWhenClosed(cont[prevK:], ['{', '}'])(linesToString(lines[fileInfo["allVarsTrack"][x][-1]:]), ['{', '}'])


def determineSection(x, ls):
    n = ''
    lsComp = []
    for i in range(0, len(str(x))):
        n = n + x[i]
        match = isInList(n, ls)
        if match[0] == 1:
            return match[1][0]
        elif match[0] == 0:
            return None


def readLines(x):
    lsN = []
    lines = read_from_file(x).split('\n')
    for i in range(0, len(lines)):
        lines[i] = eatOuter(lines[i], ['\n', '\t', ' ', '']).replace('\n', '')
        if lines[i] not in ['\n', ' \n', '', ' ', '\t'] and len(str(eatAll(lines[i], ['\n', '\t', ' ', '/', ';', '']))) != 0:
            lsN.append(lines[i]+'\n')
    return lsN


def ThenAppend(js, x):
    if x not in js:
        js.append(x)
    return js


def trackEm(ls):
    tracker_file = os.path.join(os.getcwd(), 'variables/pragmas/tracker.json')
    if os.path.exists(tracker_file) == False:
        create_and_read_json(json_data={}, file_path=tracker_file)
    track = safe_read_from_json(tracker_file)
    if ls[0] not in track:
        track[ls[0]] = {}
    if ls[1] not in track[ls[0]]:
        track[ls[0]][ls[1]] = {"names": []}
    if ls[2] not in track[ls[0]][ls[1]]:
        track[ls[0]][ls[1]]["names"] = ThenAppend(
            track[ls[0]][ls[1]]["names"], ls[2])
        track[ls[0]][ls[1]][ls[2]] = {}
    if ls[3] not in track[ls[0]][ls[1]][ls[2]]:
        track[ls[0]][ls[1]][ls[2]][ls[3]] = ls[4]
    safe_dump_to_file(data=track, file_path=tracker_file)


def checkIsList(ls):
    if type(ls) is not list:
        if ',' in str(ls):
            ls = str(ls.split(','))
        else:
            ls = [ls]
    return ls


def pragmaVerSplit(x):
    return safeSplit(x, '.', 1)


def importCheck(name, st):
    st = checkIsList(st)
    pra = pragmaVerSplit(getCurrPrag())
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


class contractVariablesManager:
    def __init__(self, currFilePath, lineTrack={}, lines=None):
        self.slash = '//' if '//' in os.getcwd() else '/'
        self.currFilePath = currFilePath
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
                                if isInt(constInt) == True:
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
            n = eatAll(constVars[0], ['\n', '\t', ' ', '/', ',', ';'])
            while 'struct' in n and isAboveZero(constVars) == True:
                constVars = stopWhenClosedRemove(constVars, ['{', '}'])
                n = eatAll(constVars[0], ['\n', '\t', ' ', '/', ',', ';'])
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

        write_to_file(contents='//SPDX-License-Identifier: '+lic+'\npragma solidity '+pragma +
                      ';\n'+stopWhenClosed(linesToString(self.lines[i:]), ['{', '}']), file_path=sectFold)
        write_to_file(contents=read_from_file(sectFold),
                      file_path=os.path.join(self.imports, title))

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
