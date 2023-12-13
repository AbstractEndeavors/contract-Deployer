import os
import json
import stat
import time
import PySimpleGUI as sg
from flatten_script import flatten_it
from abstract_gui import AbstractWindowManager,AbstractBrowser,ensure_nested_list,make_component,expandable
from abstract_utilities import create_new_name,eatOuter, eatAll, make_list,eatInner, read_from_file, write_to_file, create_and_read_json, safe_dump_to_file, safe_read_from_json
abstract_browser = AbstractBrowser()
from web3 import Web3
from eth_abi import encode

def const_it(x):
    print([[x[0]],[x[1]]])
    return read_hex(encode([x[0]],[x[1]]))
def read_hex(hb):
    h = "".join(["{:02X}".format(b) for b in hb])
    return h


def read_hex(hb):
    return hb.hex().upper()
def get_syntax_info():
    return {"names": ["Modifiers", "Visibility", "precedence", "globalVariables", "precedence"],
            "Modifiers": ["pure", "view", "payable", "constant", "immutable", "anonymous", "indexed", "virtual", "override"],
            "precedence": ["assert", "block", "coinbase", "difficulty", "number", "block;number", "timestamp", "block;timestamp", "msg", "data", "gas", "sender", "value", "gas price", "origin", "revert", "require", "keccak256", "ripemd160", "sha256", "ecrecover", "addmod", "mulmod", "cryptography", "this", "super", "selfdestruct", "balance", "codehash", "send"],
            "visibility": ["public", "private", "external", "internal"],
            "modifiers": ["pure", "view", "payable", "constant", "anonymous", "indexed"],
            "globalVariables": ['abi.decode(bytes memory encodedData, (...)) returns (...)', 'abi.encode(...) returns (bytes memory)', 'abi.encodePacked(...) returns (bytes memory)',  'abi.encodeWithSelector(bytes4 selector, ...) returns (bytes memory)', 'abi.encodeCall(function functionPointer, (...)) returns (bytes memory)', 'abi.encodeWithSelector(functionPointer.selector, (...))', 'abi.encodeWithSignature(string memory signature, ...) returns (bytes memory)', 'to abi.encodeWithSelector(bytes4(keccak256(bytes(signature)), ...)', 'bytes.concat(...) returns (bytes memory)', 'arguments to one byte array<bytes-concat>`', 'string.concat(...) returns (string memory)', 'arguments to one string array<string-concat>`', 'block.basefee (uint)', 'block.chainid (uint)', 'block.coinbase (address payable)', 'block.difficulty (uint)', 'block.gaslimit (uint)', 'block.number (uint)', 'block.timestamp (uint)', 'gasleft() returns (uint256)', 'msg.data (bytes)', 'msg.sender (address)', 'msg.sig (bytes4)', 'msg.value (uint)', 'tx.gasprice (uint)', 'tx.origin (address)', 'assert(bool condition)', 'require(bool condition)', 'for malformed input or error in external component)', 'require(bool condition, string memory message)', 'condition is false (use for malformed input or error in external component). Also provide error message.', 'revert()', 'revert(string memory message)', 'blockhash(uint blockNumber) returns (bytes32)', 'keccak256(bytes memory) returns (bytes32)', 'sha256(bytes memory) returns (bytes32)', 'ripemd160(bytes memory) returns (bytes20)', 'ecrecover(bytes32 hash, uint8 v, bytes32 r, bytes32 s) returns (address)', 'the public key from elliptic curve signature, return zero on error', 'addmod(uint x, uint y, uint k) returns (uint)', 'arbitrary precision and does not wrap around at 2**256. Assert that k != 0 starting from version 0.5.0.', 'mulmod(uint x, uint y, uint k) returns (uint)', 'with arbitrary precision and does not wrap around at 2**256. Assert that k != 0 starting from version 0.5.0.', "this (current contract's type)", 'super', 'selfdestruct(address payable recipient)', '<address>.balance (uint256)', '<address>.code (bytes memory)', '<address>.codehash (bytes32)', '<address payable>.send(uint256 amount) returns (bool)', 'returns false on failure', '<address payable>.transfer(uint256 amount)', 'type(C).name (string)', 'type(C).creationCode (bytes memory)', 'type(C).runtimeCode (bytes memory)', 'type(I).interfaceId (bytes4)', 'type(T).min (T)', 'type(T).max (T)'], "sectionHeader": ['contract', 'library', 'interface', 'abstract contract'], "allVars": ['contract', 'library', 'pragma solidity', 'import', 'interface', 'abstract contract', 'constructor', 'function', 'modify', 'SPDX-License-Identifier']}

def make_dir(*args):
    path=''
    for arg in args:
        path=os.path.join(path,arg)
        os.makedirs(path,exist_ok=True)
    return path
#___________isInList_____________#

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


#___________checkIsList_____________#

def checkIsList(ls):
    """
    Checks if the given input 'ls' is a list. If not, it makes it a list by putting it as an element in a new list.
    """
    if not isinstance(ls, list):
        ls = [ls]
    return ls


#___________countIt_____________#

def countIt(x, y):
    """
    Counts how many times a specific string 'y' appears in another string 'x'.
    """
    return (len(x)-len(x.replace(y, '')))/len(y)

#___________determineSection_____________#

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



#___________safeSplit_____________#

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

#___________getHigher_____________#

def getHigher(x, y):
    """
    Compares two integers and returns the higher one.
    """
    if int(y) > int(x):
        return y
    return x



#___________splitVarOutAndEndOrSpace_____________#

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



#___________is_list_obj_in_str_____________#

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



#___________createPragFromInt_____________#

def createPragFromInt(x):
    """
    Converts an integer into pragma version format for JavaScript.
    """
    x = str(x)
    return '0.'+x[0]+'.'+eatOuter(x[1:], '0') + '0'



#___________convertPragToInt_____________#

def convertPragToInt(x):
    """
    Converts a pragma version into an integer.
    """
    a, b = str(safeSplit(x, '.', 1)), str(safeSplit(x, '.', 2)) + '0'
    return a+b



#___________pragmaVerSplit_____________#

def pragmaVerSplit(x):
    """
    Returns the first part of the pragma version after splitting it at the dot.
    """
    return safeSplit(x, '.', 1)

#___________ListInString_____________#

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


#___________isIn_____________#

def isIn(x, st):
    """
    Checks whether a string is within another string.
    """
    if str(x) in str(st):
        return True
    return False



#___________makeAllString_____________#

def makeAllString(ls):
    """
    Converts all elements of a list into strings.
    """
    ls,lsN = checkLsAndGetNew(ls)
    for i in range(0,len(ls)):
        lsN.append(str(ls[i]))
    return lsN

#___________getHighestFloatSpec_____________#

def getHighestFloatSpec(ls):
    """
    Range-checks all elements of a list and returns the index of element with the highest value.
    """
    hi = [0,0]
    for i in range(0,len(ls)):
        if float(ls[i])>float(hi[1]):
            hi = [i,float(ls[i])]
    return hi[0]

#___________getHighestLen_____________#

def getHighestLen(ls):
    """
    Range-checks all elements of a list and returns the index of the string with the maximum length.
    """
    hi = [0,0]
    for i in range(0,len(ls)):
        if len(ls[i])>int(hi[1]):
            hi = [i,len(ls[i])]
    return hi[0]

#___________checkLsAndGetNew_____________#

def checkLsAndGetNew(ls):
    """
    Checks if input is a list and returns the list along with a new list.
    """
    return checkIsList(ls),[]

#___________makeAllComparable_____________#

def makeAllComparable(ls):
    """
    Converts all elements of a list into comparable units (lower-case strings).
    """
    ls,lsN = checkLsAndGetNew(ls)
    for i in range(0,len(ls)):
        lsN.append(str(ls[i].lower()))
    return lsN

#___________fillList_____________#

def fillList(k,ls,y):
    """
    Fills a list with designated elements until it reaches a specified length.
    """
    ls = checkIsList(ls)
    for i in range(len(ls),k):
        ls.append(y)
    return ls

#___________returnZK_____________#

def returnZK(z,k,ls,y):
    """
    Returns a tuple of values adjusted according to the input parameters.
    """
    return '',int(k)+1,fillList(int(k)+2,ls,y)

#___________isSame_____________#

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

#___________returnMostAbundant_____________#

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

#___________getPercSame_____________#

def getPercSame(x,y):
    """
    Computes the similarity percentage between two strings.
    """
    return len(x)/len(y)

#___________compareList_____________#

def compareList(x,ls,lsOg):
    """
    Compares a value with all elements in a list and returns the highest float.
    """
    ls,lsN = checkLsAndGetNew(ls)
    for i in range(0,len(ls)):
        same = isSame(x,ls[i])
        lsN.append(getPercSame(same[1],same[0]))
    return lsOg[getHighestFloatSpec(lsN)]

#___________getJustHigher_____________#

def getJustHigher(k, ls):
    """
    Returns the first item from a list that is higher than a specified value, k.
    """
    for i in range(0, len(ls)):
        if ls[i] > k:
            return ls[i]


#___________isAboveZero_____________#

def isAboveZero(x):
    """
    Checks if the length of an element x is greater than one.
    """
    if len(x) < 2:
        return False
    return True


#___________linesToString_____________#


def linesToString(ls):
    ls = checkIsList(ls)
    return ''.join(ls)



#___________ifBothOverZero_____________#

def ifBothOverZero(x, y):
    """
    Checks if the length of both elements x and y is greater than zero.
    """
    if len(x) > 0 and len(y) > 0:

        return True
    return False

#___________stopWhenClosedRemove_____________#

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
def boolAsk(x):
    yes = ['y','yes','true','t','']
    no = ['n','no','false','f']
    ask = str(input(x)).lower()
    if ask in yes:
        return True
    
    return False
#___________readLinesSpec_____________#

def readLinesSpec(x):
    """
    Cleans and returns a list of lines without unnecessary white spaces and new-line characters.
    """
    lsN = []
    lines = x.split('\n')
    for i in range(0, len(lines)):
        lines[i] = eatOuter(lines[i], ['', '	', ' ', '']).replace('', '')
        if lines[i] not in ['', ' ', '', ' ', '	'] and len(str(eatAll(lines[i], ['', '	', ' ', '/', ';', '']))) != 0:
            lsN.append(lines[i]+'')
    return lsN


#___________ifInLines_____________#

def ifInLines(lines, x, ls):
    """
    Checks if a specific string x is in a list of strings at the specified lines.
    """
    for k in range(0, len(ls)):
        if ls[k] < len(lines):
            if lines[ls[k]] == x:
                return True
    return False



#___________create_and_read_file_____________#

def create_and_read_file(file_path, contents=''):
    if os.path.isfile(file_path):
        contents = read_from_file(file_path)
    else:
        write_to_file(file_path=file_path, contents=contents)
    return contents





#___________stringInLists_____________#

def stringInLists(x, lss):
    lss, lsN = checkLsAndGetNew(lss)
    for i in range(0, len(lss)):
        lssN = checkIsList(lss[i])
        for k in range(0, len(lssN)):
            if x in lssN:
                lsN.append(findIt(x, lssN))
    return lsN



#___________detNumInWhile_____________#

def detNumInWhile(x, string, k):
    lenget = k
    for i in range(0, len(string)):
        found = ListInString(string[lenget], ['for', 'while'])
        if len(found) > 0:
            nn = ''
            n = str(stopWhenClosed(linesToString(string[lenget:]), ['(', ')'])).replace(
                ' ', '').replace('', '').replace('	', '')
            n = n.split('(')[1].split(')')[0].split(';')
            nowIntA = n[0].split('=')[1]
            found = ListInString(n[1], ['=<', '<', '>', '>=', '=', '^'])
            nowIntB = n[1].split(found[0])[1]
            if found[0] == '<':
                nowIntB = int(nowIntB) - 1
            return nowIntB
        lenget -= 1



#___________stringInList_____________#

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



#___________ThenAppend_____________#

def ThenAppend(js, x):
    if x not in js:
        js.append(x)
    return js

#___________isCurrent_____________#

def isCurrent(x, y):
    if x[:len(y)] == y:
        return True
    return False



#___________safeSplit2_____________#

def safeSplit2(x, y, k):
    if y in x:
        x = x.split(y)
        if len(x) >= int(k):
            return x[k]
    return x






#___________stopWhenClosed_____________#

def stopWhenClosed(x, ls):
    ls = checkIsList(ls)
    for i in range(0, len(x)):
        y = x[0:i]
        lenLs = [countIt(y, str(ls[0])), countIt(y, str(ls[1]))]
        if lenLs[0] == lenLs[1] and lenLs[0] != 0:
            return y
    return False



#___________stopWhenClosedI_____________#

def stopWhenClosedI(x, ls):
    ls = checkIsList(ls)
    x = linesToString(x)
    for i in range(0, len(x)):
        y = x[0:i]
        lenLs = [countIt(y, str(ls[0])), countIt(y, str(ls[1]))]
        if lenLs[0] == lenLs[1] and lenLs[0] != 0:
            return
    return y+'}'



#___________getFullSection_____________#

def getFullSection(x):
    return stopWhenClosed(cont[prevK:], ['{', '}'])(linesToString(lines[fileInfo["allVarsTrack"][x][-1]:]), ['{', '}'])






#___________readLines_____________#

def readLines(x):
    lsN = []
    lines = read_from_file(x).split('')
    for i in range(0, len(lines)):
        lines[i] = eatOuter(lines[i], ['', '	', ' ', '']).replace('', '')
        if lines[i] not in ['', ' ', '', ' ', '	'] and len(str(eatAll(lines[i], ['', '	', ' ', '/', ';', '']))) != 0:
            lsN.append(lines[i]+'')
    return lsN



#___________trackEm_____________#

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






#___________importCheck_____________#

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

def create_and_read_jsons(file_path=os.getcwd(), data={}):
    if os.path.isfile(file_path):
        data = safe_read_from_json(file_path)
    else:
        safe_dump_to_file(file_path=file_path, data=contents)
    return data


def create_and_read_file(file_path, contents=''):
    """
    Creates a new file or reads an existing one based on the given file path and contents. Returns the contents of the file."}]
    """
    if os.path.isfile(file_path):
        contents = read_from_file(file_path)
    else:
        write_to_file(file_path=file_path, contents=contents)
    return contents


def while_it(title, layout, event_handlers=[], close_events=['-EXIT-']):
    window_mgr = AbstractWindowManager()
    window_name = window_mgr.add_window(
        title=title, layout=layout, close_events=close_events, event_handlers=event_handlers)
    return window_mgr.while_window()


def display_modular_listbox(string, list_obj):
    layout = [[sg.Text(string)], [sg.Listbox(list_obj, key='-LISTBOX_VALUES-', size=(20, 10))], [[sg.Button('move up')], [sg.Button('move down')],
                                                                                                 [sg.Button('remove')], [sg.Button('add another')]], [sg.Input(str(list_obj), key='current values', visible=False)], [sg.Button('SUBMIT')]]
    key_values = while_it(string, layout, list_it, close_events=[
                          'add another', 'SUBMIT'])
    return key_values['values']['current values'], key_values['event']


def choose_files(path=os.getcwd(), string='choose a file'):
    layout = [[sg.Text(string)], [sg.Input('', key='-FILE_PATH-'),
                                  sg.FilesBrowse(initial_folder=path)], [sg.Button('SUBMIT')]]
    key_values = while_it(string, layout, close_events=['SUBMIT'])
    return key_values['values']['-FILE_PATH-']


def list_it(event, values, window):
    def get_list_num(list_obj, var):
        if list_obj:
            if var == list_obj[-1]:
                return len(list_obj)-1
            if list_obj[0] == var:
                return 0
        for i, obj in enumerate(list_obj):
            if obj == var:
                return i

    def add_position(list_obj, var, num, direction):
        new_list = []
        for i, obj in enumerate(list_obj):
            if i == num:
                if direction == 'down':
                    new_list.append(obj)
                    new_list.append(var)
                else:
                    new_list.append(var)
                    new_list.append(obj)
            else:
                new_list.append(obj)
        return new_list
    list_values = window['-LISTBOX_VALUES-'].Values
    list_value = values['-LISTBOX_VALUES-']
    if list_value:
        list_value = list_value[0]
        position = get_list_num(list_values, list_value)
        if event.split(' ')[0] == 'move':
            direction = event.split(' ')[-1]
            if direction == 'up' and position > 0:
                list_values.remove(list_value)
                position -= 1
                list_values = add_position(
                    list_values, list_value, position, direction)
            if direction == 'down' and position < len(list_values)-1:
                list_values.remove(list_value)
                list_values = add_position(
                    list_values, list_value, position, direction)
            window['-LISTBOX_VALUES-'].update(values=list_values)
            window['-LISTBOX_VALUES-'].update(
                set_to_index=[get_list_num(list_values, list_value)])
        elif event == 'remove':
            list_values.remove(list_value)
            window['-LISTBOX_VALUES-'].update(values=list_values)
    window['current values'].update(value=str(list_values))


def createAsk(how, string):
    def get_checkbox(how):
        layout = []
        for each in how:
            layout.append(sg.Checkbox(
                each, default=False, key=f'-CHECK_{each.upper().replace(" ","_")}-', enable_events=True))
        return layout
    layout = [[sg.Text(string)], [get_checkbox(how)]]
    key_values = while_it(string, layout, check_it, ['-EXIT-'])['values']
    for key, value in key_values.items():
        if value:
            return ' '.join(key.lower()[1:-1].split('_')[1:])


def gui_input(string):
    layout = [[sg.Text(string)], [sg.Input(
        '', key='-INPUT-')], [sg.Button('SUBMIT')]]
    key_values = while_it(string, layout, close_events=['SUBMIT'])
    return key_values['values']['-INPUT-']


def choose_from_list_gui(string, list_obj):
    layout = [[sg.Text(string)], [sg.Listbox(
        list_obj, key='-LISTBOX_VALUES-', size=(20, 10))], [sg.Button('SUBMIT')]]
    key_values = while_it(string, layout, close_events=['SUBMIT'])
    return key_values['values']['-LISTBOX_VALUES-'][0]


def check_it(event, values, window):
    if event[1:-1].split('_')[0] == 'CHECK':
        key = " ".join(event.lower()[1:-1].split('_')[1:])
        if values[event] == True:
            window.write_event_value('-EXIT-', '')


def read_make(file_path, contents=''):
    if os.path.isfile(file_path):
        return


def existFoldCheck(*args):
    for i, arg in enumerate(args):
        if i == 0:
            path = args[0]
        else:
            path = os.path.join(path, arg)
        if i == len(args)-1:
            if '.' in arg:
                return path
        os.makedirs(path, exist_ok=True)
    return path


def get_syntax_info():
    return {"names": ["Modifiers", "Visibility", "precedence", "globalVariables", "precedence"],
            "Modifiers": ["pure", "view", "payable", "constant", "immutable", "anonymous", "indexed", "virtual", "override"],
            "precedence": ["assert", "block", "coinbase", "difficulty", "number", "block;number", "timestamp", "block;timestamp", "msg", "data", "gas", "sender", "value", "gas price", "origin", "revert", "require", "keccak256", "ripemd160", "sha256", "ecrecover", "addmod", "mulmod", "cryptography", "this", "super", "selfdestruct", "balance", "codehash", "send"],
            "visibility": ["public", "private", "external", "internal"],
            "modifiers": ["pure", "view", "payable", "constant", "anonymous", "indexed"],
            "globalVariables": ['abi.decode(bytes memory encodedData, (...)) returns (...)', 'abi.encode(...) returns (bytes memory)', 'abi.encodePacked(...) returns (bytes memory)',  'abi.encodeWithSelector(bytes4 selector, ...) returns (bytes memory)', 'abi.encodeCall(function functionPointer, (...)) returns (bytes memory)', 'abi.encodeWithSelector(functionPointer.selector, (...))', 'abi.encodeWithSignature(string memory signature, ...) returns (bytes memory)', 'to abi.encodeWithSelector(bytes4(keccak256(bytes(signature)), ...)', 'bytes.concat(...) returns (bytes memory)', 'arguments to one byte array<bytes-concat>`', 'string.concat(...) returns (string memory)', 'arguments to one string array<string-concat>`', 'block.basefee (uint)', 'block.chainid (uint)', 'block.coinbase (address payable)', 'block.difficulty (uint)', 'block.gaslimit (uint)', 'block.number (uint)', 'block.timestamp (uint)', 'gasleft() returns (uint256)', 'msg.data (bytes)', 'msg.sender (address)', 'msg.sig (bytes4)', 'msg.value (uint)', 'tx.gasprice (uint)', 'tx.origin (address)', 'assert(bool condition)', 'require(bool condition)', 'for malformed input or error in external component)', 'require(bool condition, string memory message)', 'condition is false (use for malformed input or error in external component). Also provide error message.', 'revert()', 'revert(string memory message)', 'blockhash(uint blockNumber) returns (bytes32)', 'keccak256(bytes memory) returns (bytes32)', 'sha256(bytes memory) returns (bytes32)', 'ripemd160(bytes memory) returns (bytes20)', 'ecrecover(bytes32 hash, uint8 v, bytes32 r, bytes32 s) returns (address)', 'the public key from elliptic curve signature, return zero on error', 'addmod(uint x, uint y, uint k) returns (uint)', 'arbitrary precision and does not wrap around at 2**256. Assert that k != 0 starting from version 0.5.0.', 'mulmod(uint x, uint y, uint k) returns (uint)', 'with arbitrary precision and does not wrap around at 2**256. Assert that k != 0 starting from version 0.5.0.', "this (current contract's type)", 'super', 'selfdestruct(address payable recipient)', '<address>.balance (uint256)', '<address>.code (bytes memory)', '<address>.codehash (bytes32)', '<address payable>.send(uint256 amount) returns (bool)', 'returns false on failure', '<address payable>.transfer(uint256 amount)', 'type(C).name (string)', 'type(C).creationCode (bytes memory)', 'type(C).runtimeCode (bytes memory)', 'type(I).interfaceId (bytes4)', 'type(T).min (T)', 'type(T).max (T)'], "sectionHeader": ['contract', 'library', 'interface', 'abstract contract'], "allVars": ['contract', 'library', 'pragma solidity', 'import', 'interface', 'abstract contract', 'constructor', 'function', 'modify', 'SPDX-License-Identifier']}


def get_new_varis():
    return {"count": "0", "files": [], "fileNames": [], "adds": {}, "currFilePaths": [], "currFileDirs": [], "originalFilePaths": [], "originalFileDirs": [], "deployHistDir": '', "projectsDir": '', "currProjectDir": "", "currFileDir": "", "currFilePath": "", "home": ''}


def get_new_file_info():
    return {"projectDir": '', 
            "originalFilePath": '',
            "originalFileDir": '',
            "currProjectDir": '',
            "currFilePath": '',
            "file": '',
            "fileName": '',
            "contract_address": "",
            "api": "",
            "pragma": [],
            "license": "",
            "args": "",
            "version": "",
            "variableNames": [],
            'allVarsTrack': {}}


def resetArtifactsAndCache():
    if os.path.isdir('cache') == True:
        shutil.rmtree('cache')
    if os.path.isdir('artifacts') == True:
        shutil.rmtree('artifacts')


def CopyOriginalFile(currFilePath, originalFilePath):
    write_to_file(file_path=currFilePath,
                  contents=read_from_file(originalFilePath),)


def eatOuterMod(string, ls):
    if strInListRev(string, ls) != False:
        string = strInListRev(string, ls)
    return x


def readLines(file_path):
    lsN = []
    lines = read_from_file(file_path).split('\n')
    for i in range(0, len(lines)):
        lines[i] = eatOuter(lines[i], ['\n', '\t', ' ', '']).replace('\n', '')
        if lines[i] not in ['\n', ' \n', '', ' ', '\t'] and len(str(eatAll(lines[i], ['\n', '\t', ' ', '/', ';', '']))) != 0:
            lsN.append(lines[i]+'\n')
    return lsN


def chmodIt(x):
    st = os.stat(x)
    os.chmod(x, st.st_mode | stat.S_IEXEC)
    os.chmod(x, 0o775)
    return 'sh '+str(x)


def delFile(x):
    os.remove(x)


def checkName():
    names = lineTrack['contract']['names']
    lsN = ['input New Name', fileName]
    if fileName not in names:
        for i in range(0, len(names)):
            lsN.append(names[i])
        newName = createAsk(lsN, lsN, 'looks like there is a discrepency in the naming convention, we recorded ' +
                            str(fileName)+'; please choose the name that does not belong.')
        input(newName)
        lines = readLines(originalFilePath)
        for i in range(0, len(lines)):
            if isCurrent(lines[i], 'contract') == True:
                input(lines[i])
                if newName in lines[i]:
                    lines[i] = lines[i].replace(newName, fileName)
        write_to_file(linesToString(lines), originalFilePath)
        getItGoing()


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
    return remExtLs(os.listdir(imports),'.sol')
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
        print(nImps)
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
        print(nImps)
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
