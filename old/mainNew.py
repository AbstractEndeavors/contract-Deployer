import os
import subprocess
import time
import datetime
import requests
import json
import subprocess, signal
import parserbetterone as f
home,slash = f.home_it()
from sha3 import sha3_256
from eth_abi import encode_abi
from datetime import date
import codecs
homeStationary = home
import web3
from web3 import Web3
def changeGlob(x,v):
    globals()[x] = v
def clean_folder(x):
    ls = f.list_files(x)
    for i in range(0,len(ls)):
        if ls[i] != 'flattened':
            del_file(f.createPath(x,ls[i]))
def del_file(x):
    os.remove(x)
def iterable(x):
    return '"{libraries:{IterableMapping:"'+str(x)+'"}}",'
def date():
    from datetime import date
    today = str(date.today())

    return today
def read_hex(hb):
    h = "".join(["{:02X}".format(b) for b in hb])
    return h
def const_it(x,y):
    return read_hex(encode_abi([x],[y]))

def bash_it(x):
    global name_all,cou
    f.pen(' ',f.createPath(all_dirs['terminal'],str(name_all)+'_build_up.txt'))
    save = str(x) + ' >> '+f.createPath(all_dirs['terminal'],str(name_all)+'.txt')+';'
    f.pen(save,f.createPath(all_dirs['terminal'],str(name_all)+'_build_up.txt'))
    bash_it_good()
def get_wall_txn(x):
   return sites('https://api-testnet.snowtrace.io/api?module=account&action=txlist&address='+str(x)+'&startblock=0&endblock=99999999&sort=asc&apikey=G8N1PH6Y9X7U6FH3HB4D3RNNSTRCQNIEHG')
def bash_it_good():
    global name_all,cou
    pa = f.createPath(all_dirs['terminal'],str(name_all)+'_build_up.txt')
    x = f.reader(pa)
    sh_str = f.reader(f.createPath(all_dirs['samples'],'samplesh.txt'))
    f.pen(sh_str.replace('^^killme^^',x+'echo im done >> '+str(pa)+';'),f.createPath(all_dirs['bash'],'script.sh'))
    gnome = "gnome-terminal -x ./bash/script.sh"
    print(gnome)
    p = os.popen(gnome ).read()
    #while 'im done' not in f.read_lines(pa)[-1]:
        #time.sleep(2)
        #print('waiting for exit')
    
    f.pen(f.reader(pa).replace('im done','ended'),pa)
    speak = f.read_lines(pa)
    if len(speak) < int(10):
        x = speak
    else:
        x = speak[-10:-1]
    for i in range(0,len(x)):
        if str(x[i]) != '\n':
            print(x[i].replace('\n',''))
def verify_it(x):
    api,cont,contract,name,ver,args,licens = x['api'],x['contract_address'],f.reader(f.createPath(all_dirs['contracts'],str(name_all)+'.sol')),x['name'],x['version'],x['args'],x['license']
    data={"apikey":0,"module":"contract","action":"verifysourcecode","contractaddress":0,"sourceCode":0,"codeformat":"solidity-single-file","contractname":0,"compilerversion":0,"optimizationUsed":"1","runs":"200","constructorArguements":'[]',"evmversion":"default","licenceType":0}
    data["apikey"],data["contractaddress"],data["sourceCode"],data["contractname"],data["compilerversion"],data["constructorArguements"],data["licenceType"] = api,cont,f.reader(f.createPath(all_dirs['contracts'],str(name_all)+'.sol')),name,ver,args,licens
    r = requests.post(url = 'https://api-testnet.snowtrace.io/api', data = data)
    pastebin_url = r.text
    print("The pastebin URL is:%s"%pastebin_url)
def reques_timer():
    f.exists_make('0',f.createPath(all_dirs['python_vars'],'last.txt'))
    import datetime
    now = datetime.datetime.now().timestamp()
    i = (float(now) - float(f.reader(f.createPath(all_dirs['python_vars'],'last.txt'))))
    if float(i) < float(0.3):
        return (float(0.3) - float(i)), now
    return 0, now
def sites(A):
    U = [A]
    for url in U:
        X = str(U[0])
        i,now = reques_timer()
        time.sleep(i)
        r = requests.get(X)
        f.pen(str(now),f.createPath(all_dirs['python_vars'],'last.txt'))
        PS = r.text
        JS = json.loads(PS)
    return JS

def clean_folder(x):
    ls = f.list_files(x)
    for i in range(0,len(ls)):
        if ls[i] != 'flattened':
            del_file(f.createPath(x,ls[i]))
def del_file(x):
    os.remove(x)
def get_api(x):
    return 'https://api-testnet.snowtrace.io/api?module=account&action=txlist&address='+str(x)+'&startblock=0&endblock=99999999&sort=asc&apikey=G8N1PH6Y9X7U6FH3HB4D3RNNSTRCQNIEHG'
def clean_list(x):
    y = []
    for i in range(0,len(x)):
        n = x[i]
        while n[0] in ['"',"'",' ']:
            n = n[1:]
        while n[-1] in ['"',"'",' ']:
            n = n[:-1]
        y.append(n)
    return y
def cre_dir(x):
    n = ''
    if type(x) is not list:
        x = [x]
    for i in range(0,len(x)):
        n = f.createPath(n,x[i])
    return n
def is_int(x):
    try:
        x = int(x)
        return True
    except:
        return False
def flatten_it():
    f.pen('cd ~/Desktop/contract_station/contract_station_test/solidity-flattener; npm start "contracts/'+str(name_all)+'.sol";','python_toolz/python_vars/terminal/'+str(name_all)+'_build_up.txt')
    bash_it_good()
def rem_quotes(x):
    return str(x).replace('"','').replace("'",'')
def deploy_it(x,y):
    global verify_strs,alls
    prev_last = sites(get_api(str(adds['main'])))['result'][-1]['contractAddress']
    name = x.replace('_deploy.js','')
    sol_name = str(name)+'.sol'
    txt_name = str(name)+'.txt'
    cmd = 'npx hardhat run scripts/'+str(x)+' --network FUJI_avax'
    bash_it(cmd)
    go = 0
    while go == 0:
        new = sites(get_api(str(adds['main'])))['result'][-1]['contractAddress']
        if new == prev_last:
            go = 0
            time.sleep(2)
            print('waiting')
        else:
            go = 1
    bash_it('npx hardhat verify '+str(new)+ ' "'+str(y)+'"')
    f.copy_it(f.createPath(all_dirs['terminal'],txt_name),f.createPath(all_dirs['python_vars'],'/dep_cmd/'+txt_name))
    return new

def costPrep(currFileDir,currFilePath):
    name = info['name']
    if currFilePath != f.createPath(currFileDir,name+'.sol'):
        clean_folder('contracts')
        f.pen(f.reader(currFilePath),f.createPath(varis['currFileDirs'][i],name+'.sol'))
        f.delFile(currFilePath)
        f.pen(f.reader(currFilePath),f.createPath('contracts',name+'.sol'))
        currFilePath = f.createPath(currFileDir,name+'.sol')
        changeGlob('file',name+'.sol')
    file = info['file']
    attributes = info['allVarsTrack']['contract'][name]["constructor"]["attributes"]
    types = info['allVarsTrack']['contract'][name]["constructor"]['type']
    variables = info['allVarsTrack']['contract'][name]["constructor"]['constVariables']
    constAll = []
    for i in range(0,len(attributes)):
        attNow = attributes[i]
        constAll.append(attNow)
        if '[' in attNow:
            att = attNow.split('[')[0]
            attInt = int(attNow.split('[')[1].split(']')[0])
            lsN= []
            for k in range(0,attInt):
                lsN.append(att)
            constAll[i] = lsN
    return currFilePath,constAll[1:-1]
def getList(ls,k,name,current):
    if int(k)-1 > -1:
        return f.create_ask(ls[:k],'which contract would you like to choose?')
    ask = f.create_ask(['Add recursive deployment','input new address','use current address '+str(current)+':'],'looks as if there are no prior deployed useable in this current batch; you may add a deployment in which '+info['name']+'will launch afterwords; you may add an already deployed contract address to take the place of '+str(info['allVarsTrack']['abstract contract']['names'][int(f.findIt(name,info['allVarsTrack']['abstract contract']['addresses']))])+'; or we can leave the address as '+current+':') 
    if str(ask) == 'a':
        varis = f.changeSchedule()
        f.copyAll(x,f.pathMk(home,'current'))
    if ask == 'b':
        input('input new address')
    if ask == 'c':
        return current
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
def isList(ls):
    if type(ls) is list:
        return True
    return False
def makeListEven(ls,ls2):
    lsN,lsN2  = [],[]
    N,N2 = checkLists(ls,ls2)
    for i in range(0,len(N)):
        N[i],N2[i] = checkLists(N[i],N2[i])
        lsN.append(N[i])
        lsN2.append(N2[i])
    return lsN,lsN2
def checkLists(ls,ls2):
    if isList(ls) == True and isList(ls2) == False:
        lsN.append(ls2)
        for i in range(len(lsN),len(ls)):
            lsN.append(ls[i])
        return ls,lsN
    elif isList(ls) == False and isList(ls2) == True:
        return ls,ls2[0]
    elif isList(ls) == True and isList(ls2) == True:
        if len(ls2)>len(ls):
            lsN = []
            for i in range(0,len(ls)):
                lsN.append(ls2[i])
            return ls,lsN
        elif len(ls2)<len(ls):
            for i in range(len(ls2),len(ls)): 
                ls2.append(ls[i])
            return ls,ls2
    else:
            return ls,ls2
def comp_const_args(varNames):
    infConsts,inputs = info['allVarsTrack']['contract'][name]["constructor"]["deployerVars"],info['allVarsTrack']['contract'][name]["constructor"]["input"]
    for k in range(0,len(infConsts)):
        infConst = infConsts[k]
        inpu = inputs[k]
        varName = varNames[k]
        if '[' in infConst:
            lsN = []
            for i in range(0,int(infConst.split('[')[1].split(']')[0])):
                infCon = infConst[i]
                inp = inpu[i]
                if 'uint' in str(infCon):
                    end = ' (input will be multiplied by 10^'+str(int(dec))+' if * is added to the end of the input): '
                    inquire = inp
                elif 'address' in infCon:
                    end = '(if youd like to input a future input *)'
                    inquire = inp
                quest = ''+"is "+str(infCon) +' '+str(varName)+' '+str(i)+' supposed to be '+str(inquire)+'?'
                ch = f.boolAsk(quest)
                if ch == True:
                    inputs[k][i] = inp
                while ch == False:
                    change = input('please input what youd like to change it to:'+end+'\n')
                    if 'uint' in infCon:
                        change = dec_ast(change,dec)
                    elif 'address' in infCon and change == '*':
                        ask = getList(varis['files'],varis['count'],varName+'['+str(i)+']',change)
                        print(ask)
                        change =  '*^^'+str(ask)+'^^*'
                    boolAsk = f.boolAsk('are you sure you want to change '+str(infCon) +' '+str(varName)+' '+str(i)+' to '+str(change)+'?')
                    if boolAsk == True:
                        inputs[k][i] = change
                        ch = True
        else:
            if 'uint' in str(infConst):
                    end = ' (input will be multiplied by 10^'+str(int(dec))+' if * is added to the end of the input): '
                    inquire = inpu
                    
            if 'address' in infConst:
                end = '(if youd like to input a future input *)'
                inquire = inpu
            quest = ''+"is "+str(infConst) +' '+str(varName)+' supposed to be '+str(inquire)+'?'
            boolAsk = f.boolAsk(quest)
            if boolAsk == False:
                ch = False
                while ch == False:
                    change = input('please input what youd like to change it to:'+end+'\n')
                    if 'uint' in infConst:
                        change = dec_ast(change,dec)
                    elif 'address' in infConst and change == '*':
                        ask = f.create_ask(varis['files'],'which contract would you like to choose?')
                        change =  '*^^'+varis['files'][ask]+'^^*'
                    boolAsk = f.boolAsk('are you sure you want to change '+str(infConst) +' '+str(varName)+' to '+str(change)+'?')
                    print(boolAsk)
                    if boolAsk == True:
                        inputs[k] = change
                        ch = True
            else:
                inputs[k] = inquire
        
    info['allVarsTrack']['contract'][name]["constructor"]['depoyerVars'] = infConsts
    info['allVarsTrack']['contract'][name]["constructor"]["input"] = inputs
    f.pen(info,infoFilePath)
    return inputs
global all_dirs,str_names,verify_strs,pragmas,dep_str,adds,alls,ad,na,args,name_all,cou,all_dirs,pragmas,scanners,net,ch_id,main_tok,w3

f.startWhere()
changeGlob('varis',json.loads(f.reader('current/varis.py').replace("'",'"')))
for i in range(0,len(varis['files'])):
    input('ready to go??')
    name = varis['names'][i]
    contractFile =name+'.sol'
    contractFolder = f.createPath(home,'contracts')
    clean_folder(f.mkAllDir(contractFolder))
    currFile = varis['currFilePaths'][i]
    currFileFold = varis['currFileDirs'][i]
    changeGlob('infoFilePath',f.createPath(varis['currFileDirs'][i],'info.json'))
    contractDeployPath= f.createPath(contractFolder,contractFile)
    f.pen(f.reader(f.createPath(varis['currFileDirs'][i],contractFile)),contractDeployPath)
    f.pen(f.reader(f.createPath(varis['currFileDirs'][i],'hardhat.config.js')),'hardhat.config.js')
    changeGlob('info',json.loads(f.reader(infoFilePath).replace("'",'"')))
    currentDeployFold = f.createPath(varis['home'],'current')
    foldNow,constVars = costPrep(currFileFold,currFile)
    deployScript = f.createPath(currFileFold,name+'_deploy.js')
    
    #f.pen(f.reader(deployScript).replace('^^2^^','').replace('^^3^^',str(comp_const_args(info['allVarsTrack']['contract'][name]["constructor"]['constVariables']))[1:-1]),deployScript)
    gnome = "gnome-terminal -x sh ."+f.createPath(currFileFold.split(home)[1],"script.sh")
    p = os.popen(gnome).read()
    varis['count'] = int(varis['count']) +int(1)
