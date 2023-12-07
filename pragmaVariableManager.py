import os
import PySimpleGUI as sg
from abstract_utilities import eatOuter, eatAll, eatInner, read_from_file, write_to_file, create_and_read_json, safe_dump_to_file, safe_read_from_json


def isInList(x, ls):
    """
    Checks if the specified element 'x' exists in the list 'ls'. If the element exists, it appends it to 'newLs' and returns the length of 'newLs' and 'newLs' itself. 
    """
    newLs = []
    for i in range(0, len(ls)):
        n = ls[i]
        nn = ''
        for k in range(0, len(n)):
            nn = nn + n[k]
        if str(x) == str(nn):
            newLs.append(n)
    return len(newLs), newLs


def checkIsList(ls):
    """
    Checks if the given input 'ls' is a list. If not, it makes it a list by putting it as an element in a new list.
    """
    if not isinstance(ls, list):
        ls = [ls]
    return ls


def countIt(x, y):
    """
    Counts how many times a specific string 'y' appears in another string 'x'.
    """
    return (len(x)-len(x.replace(y, '')))/len(y)


def determineSection(x, ls):
    """
    Determines a section of the string 'x' that matches an element in the list 'ls', effectively creating the match list.
    """
    n = ''
    lsComp = []
    for i in range(0, len(str(x))):
        n = n + x[i]
        match = isInList(n, ls)
        if match[0] == 1:
            return match[1][0]
        elif match[0] == 0:
            return None


def safeSplit(x, y, i):
    """
    Safely splits the string 'x' by 'y'. If the index 'i' is out of boundary, it asks for a new index from user.
    """
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


def getHigher(x, y):
    """
    Compares two integers and returns the higher one.
    """
    if int(y) > int(x):
        return y
    return x


def splitVarOutAndEndOrSpace(x, y):
    """
    Given a portion of the string 'x', it removes it from 'y' and returns the processed string.
    """
    if x+' ' in y:
        x = x+' '
    n = y.split(str(x))[1]
    if ' ' in n:
        n = n.split(' ')[0]
    return n


def is_list_obj_in_str(string, list_obj):
    """
    Checks if the objects in the list 'list_obj' are in the string. If an object is found and is not in the 'found_list', it is added to 'found_list'.
    """
    found_list = []
    for obj in list_obj:
        if obj in string and obj not in found_list:
            # Check if this obj is a substring of any already found items
            if any(obj in found_obj for found_obj in found_list):
                continue
            # Check if any already found items are substrings of this obj
            found_list = [
                found_obj for found_obj in found_list if found_obj not in obj]
            found_list.append(obj)
    return found_list


def createPragFromInt(x):
    """
    Converts an integer into pragma version format for JavaScript.
    """
    x = str(x)
    return '0.'+x[0]+'.'+eatOuter(x[1:], '0') + '0'


def convertPragToInt(x):
    """
    Converts a pragma version into an integer.
    """
    a, b = str(safeSplit(x, '.', 1)), str(safeSplit(x, '.', 2)) + '0'
    return a+b


def pragmaVerSplit(x):
    """
    Returns the first part of the pragma version after splitting it at the dot.
    """
    return safeSplit(x, '.', 1)


def ListInString(x, ls):
    """
    Checks for elements of list 'ls' in a string 'x', returns a list containing those elements.
    """
    ls = checkIsList(ls)
    lsN = []
    for i in range(0, len(ls)):
        if ls[i] in x:

            lsN.append(ls[i])
    return lsN


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
