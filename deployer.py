import os
import PySimpleGUI as sg
import json
from abstract_utilities import eatOuter, eatAll, eatInner, read_from_file, write_to_file, create_and_read_json, safe_dump_to_file, safe_read_from_json
from abstract_window_manager import AbstractWindowManager
from contractVariableManager import contractVariablesManager
from pragmaVariableManager import pragmaVariableManager
from flatten_script import flatten_it
from spdxManager import spdxManager
from get_initial_variables import getInitialVars

import stat
import time


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
    return {"projectDir": '', "originalFilePath": '', "originalFileDir": '', "currProjectDir": '', "currFilePath": '', "file": '', "fileName": '', "contract_address": "", "api": "", "pragma": [], "license": "", "args": "", "version": "", "variableNames": [], 'allVarsTrack': {}}


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

class ContractDeployer:
    def __init__(self, home_folder=None):
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
        self.projectsDir = existFoldCheck(self.home, 'deployHist', 'projects')

    def determineEndPoint(self):
        self.startWhere()
        keepItUp = True
        while keepItUp == True:
            allFiles, choice = self.returnLen()
            if choice == 'addAnother':
                self.getItGoing()
                compileNeeds()
            else:
                keepItUp = False
        safe_dump_to_file(safe_read_from_json(self.varisPath),
                          os.path.join(self.home, 'current', 'varis.py'))
        return allFiles

    def startWhere(self):
        options = ['new']
        projects_dir_list = os.listdir(self.projectsDir)
        if len(projects_dir_list) > 0:
            options.append('old')
        current_list = os.listdir(self.currentDir)
        if len(current_list) > 0:
            options.append('current')
        if len(options) == 1:
            ask = 'new'
        else:
            ask = createAsk(options, 'How would you like to start?')
        if ask == 'new':
            self.newDep()
        elif ask == 'old':
            self.chooseProjectDir()
        elif ask == 'current':
            self.currentDeployed()

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

    def create_project_dir(self, project_name):
        self.currProjectDir = existFoldCheck(self.projectsDir, project_name)
        self.varisPath = existFoldCheck(self.currProjectDir, 'varis.py')
        self.retrieveVarisInfo()

    def retrieveVarisInfo(self):
        self.varisNew = get_new_varis()
        self.varisInfo = create_and_read_json(
            file_path=self.varisPath, json_data=self.varisNew)

    def newDep(self, extra_string=''):
        project_name = self.NewProjectDir(extra_string=extra_string)
        self.currProjectDir = existFoldCheck(self.projectsDir, project_name)
        self.create_project_dir(project_name=project_name)

    def currentDeployed(self):
        self.createFolders()
        self.varisPath = os.path.join(self.currentDir, 'varis.py')
        self.varisInfo = safe_read_from_json(self.varisPath)
        self.currProjectDir = self.varisInfo["currProjectDir"]
        self.varisPath = os.path.join(self.currProjectDir, 'varis.py')

    def chooseProjectDir(self):
        self.createFolders()
        projects_dir_list = os.listdir(self.projectsDir)
        if len(projects_dir_list) == 0:
            self.newDep(
                'looks like no older projects are on record here, you will have to start a new deploy')
        else:
            project_name = choose_from_list_gui(
                'choose from previous projects', projects_dir_list)
            self.create_project_dir(project_name=project_name)
        self.retrieveVarisInfo()

    def returnLen(self):
        self.retrieveVarisInfo()
        if len(self.varisInfo['files']) == 0:
            self.last = self.home
            return self.varisInfo['fileNames'], 'addAnother'
        return display_modular_listbox('this is your current deploy schedule:', self.varisInfo['fileNames'])

    def newFileInfo(self):
        new_file_info = get_new_file_info()
        self.infoFilePath = os.path.join(self.currFileDir, 'info.json')
        file_info = ''
        if os.path.isfile(self.infoFilePath):
            self.fileInfo = safe_read_from_json(self.infoFilePath)
            for key in list(file_info.keys()):
                if self.checkAttributeValue(key):
                    setattr(self, key, file_info[key])
        if file_info == '':
            for key in list(new_file_info.keys()):
                value = self.checkAttributeValue(key)
                if value:
                    new_file_info[key] = value
            self.fileInfo = new_file_info
            safe_dump_to_file(file_path=self.infoFilePath, data=self.fileInfo)

    def choose_original_file_path(self):
        value = self.checkAttributeValue("originalFilePath")
        if value in [None, False]:
            self.originalFilePath = choose_files(self.last)
        self.originalFileDir = os.path.dirname(self.originalFilePath)

    def deriveNameAndFile(self):
        self.file = os.path.basename(self.originalFilePath)
        self.fileName = os.path.splitext(self.file)[0]

    def deriveCurrentDir(self):
        self.currFileDir = existFoldCheck(self.currProjectDir, self.fileName)
        self.currFilePath = os.path.join(self.currFileDir, self.file)
        self.importsDir = existFoldCheck(self.currFileDir, 'imports')
        self.allsPath = os.path.join(self.importsDir, 'alls.txt')
        create_and_read_file(file_path=self.allsPath, contents='')

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
                                    lsN.append(n[i].split('[')[
                                               0]+'['+str(c+1)+']')
                                    self.lineTrack['contract'][na]["constructor"]["input"].append(constAsk(
                                        n[i].split('[')[0]+'['+str(c+1)+']', n[i].split('[')[0], ifAble(lsConsts, c)))
                                    lsVerify.append(const_it([n[i].split(
                                        '[')[0], self.lineTrack['contract'][na]["constructor"]["input"][-1]]))
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
        contents = """^^0^^
const hre = require("hardhat");
async function main() {
  const Greeter = await hre.ethers.getContractFactory(^^1^^);
  const greeter = await Greeter.deploy(^^2^^,^^3^^);
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
  });"""
        contents = contents.replace(
            '^^0^^', 'require("@nomiclabs/hardhat-etherscan");')
        contents = contents.replace(
            '^^1^^', self.fileName).replace('^^2^^', '')
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
        contents = contents.replace('^^3^^', track)

        deploy_path = os.path.join(os.path.dirname(self.currFileDir), 'deploy')
        os.makedirs(deploy_path, exist_ok=True)
        file_path = os.path.join(deploy_path, self.fileName+'_deploy.js')
        write_to_file(file_path=file_path, contents=contents)
        chmodIt(file_path)

    def deriveLocalVar(self):
        self.deriveNameAndFile()
        self.deriveCurrentDir()
        self.newFileInfo()
        self.bulkUpdateVarisInfo()
        resetArtifactsAndCache()
        CopyOriginalFile(self.currFilePath, self.originalFilePath)
        self.lines = readLines(self.currFilePath)

    def getTheVars(self):
        flatten_it(self.originalFilePath, self.currFileDir)
        self.lineTrack = contractVariablesManager(
            currFilePath=self.currFilePath, lines=self.lines).lineTrack
        pragmaVar_mgr = pragmaVariableManager(
            lineTrack=self.lineTrack, fileInfo=self.fileInfo)
        self.lineTrack = pragmaVar_mgr.lineTrack
        self.fileInfo = pragmaVar_mgr.fileInfo
        self.spdx_mgr = spdxManager(
            lineTrack=self.lineTrack, fileInfo=self.fileInfo, lines=self.lines)
        self.lineTrack = self.spdx_mgr.lineTrack
        self.fileInfo = self.spdx_mgr.fileInfo
        self.fileInfo['allVarsTrack'] = self.lineTrack
        self.bulkUpdateVarisInfo()

    def getItGoing(self):
        self.choose_original_file_path()
        self.deriveLocalVar()
        self.getTheVars()
        self.lineTrack = getInitialVars(
            self.lines, self.lineTrack, self.allLines)
        # checkName()
        self.pragmaSpec = str(
            self.fileInfo['allVarsTrack']['pragma solidity']['pragma'])
        self.bulkUpdateVarisInfo()
        self.makeConstructors()
        self.bulkUpdateVarisInfo()
        self.createFiles()
        


ContractDeployer()
