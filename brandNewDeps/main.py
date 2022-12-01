import os
import subprocess
import sys
import json
def changeGlob(x,v):
    globals()[x] = v
def check_file(x):
    return os.path.isfile(x)
def do_the_file(x,y,z):
    if check_file(x) == False:
        pen(y,z)
        return y
    return reader(z)
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
def reader_C(file):
    with open(file, 'r',encoding='utf-8-sig') as f:
        text = f.read()
        return text
def reader_B(file):
    with open(file, 'r',encoding='UTF-8') as f:
        text = f.read()

        return text
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
def home_it():
    curr = get_curr_path()
    slash = '//'
    if '//' not in str(curr):
        slash = '/'
    change_glob('slash',slash)
    change_glob('home',curr)
    return curr,slash
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
def chmodIt(x):
    st = os.stat(x)
    os.chmod(x, st.st_mode | stat.S_IEXEC)
    os.chmod(x, 0o775)
    return 'sh '+str(x)
def createPassScript():
    pen("#!/bin/bash 'npx hardhat run scripts/deploy.js'")
    os.popen(chmodIt('./bash.sh')).read()
p = os.popen("gnome-terminal -x ./bash.sh").read()
