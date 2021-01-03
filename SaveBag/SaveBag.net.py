#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author : Sbaoor
# date   : 2021/1/3
import mc
import tool
import json
import time
import thread
uuid = {}
name = []
player = 0
def load_plugin():
    if not tool.IfDir('./plugins/SaveBag'):
        tool.CreateDir('./plugins/SaveBag')
        print('[SaveBag] 文件夹创建成功！')
    print('[SaveBag] 背包保存已加载！')

def load_name(a):
    d = eval(a)
    name.append(d['playername'])
    uuid[d['playername']] = d['uuid']
def player_left(a):
    d = eval(a)
    uuid.pop(d['playername'])
    name.remove(d['playername'])

def savepack():
    print '[SaveBag] 线程开启！'
    while True:
        if name:
            for x in range(len(name)):
                i = mc.creatPlayerObject(uuid[name[x]])
                packdict = json.loads(i.InventoryContainer)
                xx = 0
                pack = ''
                while xx < int(len(packdict)):
                    if not packdict[xx]["id"] == 0:
                        pack += packdict[xx]["item"] + '@' + str(packdict[xx]["count"]) +'\n'
                    xx += 1
                tool.WriteAllText('./plugins/SaveBag/'+name[x]+'.txt',pack)
                if not len(name) == 0:
                    print '[SaveBag] 数据保存完成,保存了'+str(len(name))+'个玩家的背包数据'
        time.sleep(60)
def respawn(a):
    global player
    if player == 0:
        thread.start_new_thread(savepack,())
        player += 1
