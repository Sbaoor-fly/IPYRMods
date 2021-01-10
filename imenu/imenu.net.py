#! /usr/bin/env python
# -*- coding:utf-8 -*-
from System import IO
import json
import pfapi
import mc
formid = {}
packid = {}
if not IO.File.Exists('./plugins/imenu/config.json'):
    IO.Directory.CreateDirectory('./plugins/imenu')
jsons = json.loads(IO.File.ReadAllText('./plugins/imenu/config.json'))
def load_plugin():
    mc.setCommandDescribe('menu','打开菜单')
    print('[IMENU] 装载成功')
    print('[IMENU] 作者：Sbaoor')
#################
def useitem(a):
    global jsons
    d = eval(a)
    if d['itemid'] == jsons['itemid']:
        sendform(d['playername'],'main')

def formselect(a):
    null = 'None'
    true = 'true'
    false = 'false'
    d = eval(a)
    formm = json.loads(IO.File.ReadAllText('./plugins/imenu/packs/'+str(packid[d['playername']])+'.json'))
    if d['selected'] != 'None':
        if str(d['formid']) == str(formid[d['playername']]):
            cmds =  str(formm['buttons'][d['selected']]['cmd'][0]['command'])
            if str(formm['buttons'][d['selected']]['cmd'][0]['type']) == 'default':
                mc.runcmdAs(pfapi.GetUUID(d['playername']),cmds)
            if str(formm['buttons'][d['selected']]['cmd'][0]['type']) == 'cmd':
                mc.runcmd(cmds.replace('@s','\"'+str(d['playername']+'\"')))
            if str(formm['buttons'][d['selected']]['cmd'][0]['type']) == 'opcmd':
                if pfapi.HasOpPermission(d['playername']):
                    mc.runcmdAs(pfapi.GetUUID(d['playername']),cmds)
                else:
                    mc.tellraw('\"'+str(d['playername'])+'\"','[§emenu§r] §4你莫得op权限不能执行这个命令')
            if str(formm['buttons'][d['selected']]['cmd'][0]['type']) == 'form':
                sendform(d['playername'],cmds)
            if str(formm['buttons'][d['selected']]['cmd'][0]['type']) == 'moneycmd':
                if int(pfapi.GetMoney(d['playername'])) > int(formm['buttons'][d['selected']]['cmd'][0]['money']):
                    mc.runcmdAs(pfapi.GetUUID(d['playername']),cmds)
                    pfapi.RemoveMoney(d['playername'],int(formm['buttons'][d['selected']]['cmd'][0]['money']))
                else:
                    mc.tellraw('\"'+str(d['playername'])+'\"','[§emenu§r] §4你钱不够哦')

def inputcommand(a):
    d = eval(a)
    if d['cmd'] == '/menu':
        sendform(d['playername'],'main')
        return False


def sendform(name,formpack):
    fom = '['
    x = 0
    formm = json.loads(IO.File.ReadAllText('./plugins/imenu/packs/'+str(formpack)+'.json'))
    num = len(formm['buttons'])
    while x < num :
        if x!= 0 :
            fom+=','
        fom +='\''+ (str(formm['buttons'][x]['text']).decode('unicode_escape')) +'\''
        x += 1
    fom += ']'
    packid[name] = formpack
    formid[name] = mc.sendSimpleForm(pfapi.GetUUID(name),formm['title'],formm['content'],str(fom).replace('\'','\"'))