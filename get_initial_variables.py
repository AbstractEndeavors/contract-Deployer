from abstract_utilities import eatAll, eatOuter, write_to_file, safe_dump_to_file
import os


def getJustHigher(k, ls):
    """
    Returns the first item from a list that is higher than a specified value, k.
    """
    for i in range(0, len(ls)):
        if ls[i] > k:
            return ls[i]


def isAboveZero(x):
    """
    Checks if the length of an element x is greater than one.
    """
    if len(x) < 2:
        return False
    return True


def linesToString(x):
    """
    Converts a list of strings into a single string.
    """
    x = checkIsList(x)
    nn = ''
    for i in range(0, len(x)):
        n = x[i]
        for c in range(0, len(n)):
            nn = nn + n[c]
    return nn


def countIt(x, y):
    """
    Counts the number of occurrences of a specific letter in a string.
    """
    return (len(x)-len(x.replace(y, '')))/len(y)


def ifBothOverZero(x, y):
    """
    Checks if the length of both elements x and y is greater than zero.
    """
    if len(x) > 0 and len(y) > 0:

        return True
    return False


def checkIsList(ls):
    """
    Checks if a given element is a list. If it is not, the element is converted into a list.
    """
    if type(ls) is not list:
        if ',' in str(ls):
            ls = str(ls.split(','))
        else:
            ls = [ls]
    return ls


def stopWhenClosedRemove(x, ls):
    """
    Stops parsing the list when a closed bracket is found and removes the parsed part from the list.
    """
    ogX = len(x)
    ls = checkIsList(ls)
    x = linesToString(x)
    for i in range(0, len(x)):
        y = x[0:i]
        lenLs = [countIt(y, str(ls[0])), countIt(y, str(ls[1]))]
        if lenLs[0] == lenLs[1] and lenLs[0] != 0:
            return readLinesSpec(x)[len(readLinesSpec(y)):]


def readLinesSpec(x):
    """
    Cleans and returns a list of lines without unnecessary white spaces and new-line characters.
    """
    lsN = []
    lines = x.split('\n')
    for i in range(0, len(lines)):
        lines[i] = eatOuter(lines[i], ['\n', '\t', ' ', '']).replace('\n', '')
        if lines[i] not in ['\n', ' \n', '', ' ', '\t'] and len(str(eatAll(lines[i], ['\n', '\t', ' ', '/', ';', '']))) != 0:
            lsN.append(lines[i]+'\n')
    return lsN


def ifInLines(lines, x, ls):
    """
    Checks if a specific string x is in a list of strings at the specified lines.
    """
    for k in range(0, len(ls)):
        if ls[k] < len(lines):
            if lines[ls[k]] == x:
                return True
    return False


def ListInString(x, ls):
    """
    Returns a list of strings that are found in a given string x.
    """
    ls = checkIsList(ls)
    lsN = []
    for i in range(0, len(ls)):
        if ls[i] in x:

            lsN.append(ls[i])
    return lsN


def safeSplit(x, y, i):
    """
    Safely splits a given string x using a specified delimiter y and at a specified index i.
    """
    if str(y) in str(x):
        spl = str(x).split(str(y))
        if len(spl) > i:
            return spl[i]
        return spl
    return False


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

    lineTrack['variables'] = {'rndm': [], 'address': {"list": [], "single": []}, 'uint': {"list": [], "single": [
    ]}, 'string': {"list": [], "single": []}, 'bool': {"list": [], "single": []}, 'bytes': {"list": [], "single": []}}
    contract_lines = lineTrack['contract']['lines']
    constVars = []
    if contract_lines:
        constVars = lines[contract_lines[-1] +
                          1:getJustHigher(contract_lines[-1], lineTrack['function']['lines'])]
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
