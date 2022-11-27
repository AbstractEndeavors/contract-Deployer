import os
import subprocess
import time
import datetime
import requests
import json
import subprocess, signal
import parser as f
home,slash = f.home_it()
from sha3 import sha3_256
from eth_abi import encode_abi
from datetime import date
import codecs
homeStationary = home
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
def keys():
    if scanners == 'bscscan.com':
        key = 'JYVRVFFC32H2ZSKDY1JZKNY7XV1Y5MCJHM'
    elif scanners == 'polygonscan.com':
        key = 'S6X6NY29X4ARWRVSIZJTG1PJS4IG86B3WJ'
    elif scanners == 'ftmscan.com':
        key = 'WU2C3NZAQC9QT299HU5BF7P8QCYX39W327'
    elif scanners == 'moonbeam.moonscan.io':
        key = '5WVKC1UGJ3JMWQZQAT8471ZXT3UJVFDF4N'
    else:
        key = 'G8N1PH6Y9X7U6FH3HB4D3RNNSTRCQNIEHG'
    return key
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
    attributes = info['allVarsTrack']['constructor']['constructorVars']['attributes']
    types = info['allVarsTrack']['constructor']['constructorVars']['type']
    variables = info['allVarsTrack']['constructor']['constructorVars']['constVariables']
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
def comp_const_args(ra,name,y,alls):
    deplo = []
    for k in range(0,len(ra)):
        typeVar = ra[k]
        name = alls[k]
        if '[' in typeVar:
            
            ls = []
            for i in range(0,int(typeVar.split('[')[1].split(']')[0])):
                if 'uint' in str(typeVar):
                    end = ' (input will be multiplied by 10^'+str(int(dec))+' if * is added to the end of the input): '
                    inquire = '1'
                    
                if 'address' in typeVar:
                    end = '(if youd like to input a future input *)'
                    change = '0x0000000000000000000000000000000000000000'
                ls.append(typeVar)
                quest = ''+"is "+str(ls[i]) +' '+str(name)+' '+str(i)+' supposed to be '+str(change)+'?'
                boolAsk = f.boolAsk(quest)
                while boolAsk == False:
                    change = input('please input what youd like to change it to:'+end+'\n')
                    if 'uint' in typeVar:
                        change = dec_ast(change,dec)
                    if 'address' in typeVar and change == '*':
                        ask = getList(varis['files'],varis['count'],name+'['+str(i)+']',change)
                        print(ask)
                        change =  '*^^'+str(ask)+'^^*'
                    print(change)
                    boolAsk = f.boolAsk('are you sure you want to change '+str(typeVar) +' '+str(name)+' '+str(i)+' to '+str(change)+'?')
                ls[i] = change
               
        else:
            typeVar = ra[k]
            name = alls[k]
            ls = []
            if 'uint' in str(typeVar):
                    end = ' (input will be multiplied by 10^'+str(int(dec))+' if * is added to the end of the input): '
                    inquire = '1'
                    
            if 'address' in typeVar:
                end = '(if youd like to input a future input *)'
                inquire = '0x0000000000000000000000000000000000000000'
            ls.append(typeVar)
            quest = ''+"is "+str(ls[i]) +' '+str(name)+' '+str(i)+' supposed to be '+str(inquire)+'?'
            boolAsk = f.boolAsk(quest)
            if boolAsk == False:
                ch = False
                while ch == False:
                    change = input('please input what youd like to change it to:'+end+'\n')
                    if 'uint' in typeVar:
                        change = dec_ast(change,dec)
                    if 'address' in typeVar and change == '*':
                        ask = f.create_ask(varis['files'],'which contract would you like to choose?')
                        change =  '*^^'+varis['files'][ask]+'^^*'
                    boolAsk = f.boolAsk('are you sure you want to change '+str(typeVar) +' '+str(name)+' '+str(i)+' to '+str(change)+'?')
                    if boolAsk != False:
                        ls[i] = change
            else:
                ls[i] = inquire
        deplo.append(ls)
    return str(deplo)[1:-1].replace(' ','')
def startWhere():
    f.homeAll = home
    how = ['new','old','current']
    ask = f.create_ask(how,'where would you like to start?')
    if ask == how[0]:
      f.createNewDeploy()
    if ask == how[1]:
      f.getOldDeploy()
    if ask == how[2]:
      f.getCurrentDeploy()
global all_dirs,str_names,verify_strs,pragmas,dep_str,adds,alls,ad,na,args,name_all,cou,all_dirs,pragmas
startWhere()
changeGlob('varis',json.loads(f.reader('current/varis.py').replace("'",'"')))
for i in range(int(varis['count']),len(varis['files'][0])):
    input('ready to go??')
    print
    name = varis['names'][i]
    clean_folder('contracts')
    currFile = varis['currFilePaths'][i]
    f.pen(f.reader(varis['currFilePaths'][i]),f.createPath(f.createPath(home,'contracts'),name+'.sol'))
    changeGlob('info',f.reader(f.createPath(varis['currFileDirs'][i],'info.json')).replace("'",'"'))
    buildUp = f.createPath(varis['currFileDirs'][i],'buildUp.txt')
    info = json.loads(f.reader(f.createPath(varis['currFileDirs'][i],'info.json')).replace("'",'"'))
    config = f.createPath(varis['currFileDirs'][i],'hardhat.config.js')
    f.copyIt(config,home)
    conf = f.reader('variables/samples/config_sample.txt').replace('^^killme^^','{\n\tversion: "'+str(info['allVarsTrack']['pragma solidity']['pragma'])+'",\n\tsettings: {\n\t\toptimizer: {\n\tenabled: true,\n\truns: 200\n\t}\n\t}\n\t},')
    f.pen(conf,'hardhat.config.js')
    currentFold = f.createPath(varis['home'],'current')
    time.sleep(2)
    varis['currFilePaths'][i],constVars = costPrep(varis['currFileDirs'][i],varis['currFilePaths'][i])
    deployFile = f.createPath(varis['currFileDirs'][i],name+'_deploy.js')
    constVars = comp_const_args(info['allVarsTrack']['constructor']['constructorVars']['attributes'],info['name'],info['allVarsTrack']['constructor']['constructorVars']['type'],info['allVarsTrack']['constructor']['constructorVars']['constVariables'])
    deplo = f.reader('variables/samples/deploy.js').replace('^^0^^','require("@nomiclabs/hardhat-etherscan");').replace('^^1^^',name).replace('^^2^^','').replace('^^3^^',str(constVars))
    f.pen(deplo,deployFile)
    f.pen(f.reader('/home/bigrugz/Desktop/newTester/variables/samples/sample_whole_sh.txt').replace('^^killme^^', '" solc-select install '+info['allVarsTrack']['pragma solidity']['pragma']+'; solc-select use '+info['allVarsTrack']['pragma solidity']['pragma']+';  cd '+str(home)+'; npx hardhat run '+str(deployFile)+' --network FUJI_avax;'),f.createPath(varis['currFileDirs'][i],'script.sh'))
    gnome = "gnome-terminal -x ."+f.createPath(varis['currFileDirs'][i].split(home)[1],"script.sh")
    p = os.popen(gnome).read()
    #if name[i-1] == "BigBurgNode":
    #    stat = sites(get_wall_txn(str(vr(["adds","BigBurgNode"]))))
    #    new = stat['result'][-1]['hash']
    #    enc.add_hash = adds["BigBurgNode"],new
    #    adds["JoePair"] = enc.x
    args = ''
    #if vr(['alls',name,"deplo"]) !='':
    #    args = const.get_em(name,alls[name]["deplo"])
    #vs(["verify_strs","args"],args)
    current = {"verify_strs":["verify_strs"],"args":[args]}
    varis['count'] = int(varis['count']) +int(1)
    f.pen(' ',f.createPath(all_dirs['terminal'],str(name)+'.txt'))
    bash_it('npm start contracts/'+str(name)+'.sol')
    f_name = name+'_deploy.js'
    #temp = dep_str
    al = [alls[name]["deplo"],alls[name]["deplo"],alls[name]["const_vars"]]
    for ii in range(0,len(al)):
        if ii == 0 and al[ii] == 1:
            al[0] = 'require("@nomiclabs/hardhat-etherscan");'
        if type(al[ii]) is list:
            al[ii] = str(al[ii])[1:-1]
        temp = temp.replace('^^'+str(ii)+'^^',al[ii])
    temp = temp.replace(',);',');')
    f.pen(temp,f.createPath(all_dirs['python_vars'],'scripts/'+f_name))
    f.pen(temp,f.createPath(all_dirs['scripts'],f_name))
    vs(["verify_strs","contract_address"],deploy_it(f_name,str(args).lower()))
    vs([adds,n],["verify_strs","contract_address"])
    f.pen(variables.adds,'current.txt')

    verify_it(verify_strs)
