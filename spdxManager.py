import os
from abstract_utilities import eatOuter, eatAll, eatInner


def checkIsList(ls):
    """
    Validates if the input is a list. If not, it converts the input into a list.
    """
    if not isinstance(ls, list):
        ls = [ls]
    return ls


def isIn(x, st):
    """
    Checks whether a string is within another string.
    """
    if str(x) in str(st):
        return True
    return False


def safeSplit(x, y, i):
    """
    Safely splits a string by a specified separator. If the input index is out of range, the function creates an ask for user intervention.
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
def makeAllString(ls):
    """
    Converts all elements of a list into strings.
    """
    ls,lsN = checkLsAndGetNew(ls)
    for i in range(0,len(ls)):
        lsN.append(str(ls[i]))
    return lsN
def getHighestFloatSpec(ls):
    """
    Range-checks all elements of a list and returns the index of element with the highest value.
    """
    hi = [0,0]
    for i in range(0,len(ls)):
        if float(ls[i])>float(hi[1]):
            hi = [i,float(ls[i])]
    return hi[0]
def getHighestLen(ls):
    """
    Range-checks all elements of a list and returns the index of the string with the maximum length.
    """
    hi = [0,0]
    for i in range(0,len(ls)):
        if len(ls[i])>int(hi[1]):
            hi = [i,len(ls[i])]
    return hi[0]
def checkLsAndGetNew(ls):
    """
    Checks if input is a list and returns the list along with a new list.
    """
    return checkIsList(ls),[]
def makeAllComparable(ls):
    """
    Converts all elements of a list into comparable units (lower-case strings).
    """
    ls,lsN = checkLsAndGetNew(ls)
    for i in range(0,len(ls)):
        lsN.append(str(ls[i].lower()))
    return lsN
def fillList(k,ls,y):
    """
    Fills a list with designated elements until it reaches a specified length.
    """
    ls = checkIsList(ls)
    for i in range(len(ls),k):
        ls.append(y)
    return ls
def returnZK(z,k,ls,y):
    """
    Returns a tuple of values adjusted according to the input parameters.
    """
    return '',int(k)+1,fillList(int(k)+2,ls,y)
def isSame(x,y):
    """
    Compares two inputs for similarity.
    """
    x,y = makeAllString([x,y])
    lsN,k,z = [''],0,''
    for i in range(0,len(str(x))):
        z = z+x[i]
        if isIn(z,y) == True:
            lsN[k] = z
        else:
            z,k,lsN = returnZK(z,k,lsN,'')
    return [x,lsN[getHighestLen(lsN)]]
def returnMostAbundant(ls,lsNone):
    """
    Finds the most frequently occurring element in a list.
    """
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
def getPercSame(x,y):
    """
    Computes the similarity percentage between two strings.
    """
    return len(x)/len(y)
def compareList(x,ls,lsOg):
    """
    Compares a value with all elements in a list and returns the highest float.
    """
    ls,lsN = checkLsAndGetNew(ls)
    for i in range(0,len(ls)):
        same = isSame(x,ls[i])
        lsN.append(getPercSame(same[1],same[0]))
    return lsOg[getHighestFloatSpec(lsN)]
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

