#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author : Sbaoor
# date   : 2021/1/7
import mc
import tool
import json
import time
import thread
from System import IO
motd = []
player = 0
def load_plugin():
    if not tool.IfFile('./plugins/DynamicMotd/motd.txt'):
        tool.CreateDir('./plugins/DynamicMotd')
        tool.AppendAllText('./plugins/DynamicMotd/motd.txt','Dedicated Server')
    d = tool.ReadAllLine('./plugins/DynamicMotd/motd.txt')
    x = 0
    while x < len(d): 
        motd.append(d[x])
        print d[x]
        x +=1
    print('[DynamicMotd] 动态motd已加载！')

def changemotd():
    print '[DynamicMotd] 线程开启！'
    while True:
        for x in range(len(motd)):
            mc.setServerMotd(motd[x],True)
            time.sleep(30)
        
def respawn(a):
    global player
    if player == 0:
        thread.start_new_thread(changemotd,())
        player += 1
