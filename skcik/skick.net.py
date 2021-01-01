#! /usr/bin/env python
# -*- coding:utf-8 -*-
import mc
import pfapi
list1 = []
def load_plugin():
    mc.setCommandDescribe('skick','踢人')
def load_name(a):
    d = eval(a)
    list1.append(d['playername'])
def player_left(a):
    d= eval(a)
    list1.remove(d['playername'])
def inputcommand(a):
    d = eval(a)
    if d['cmd'].startswith('/skick'):
        if pfapi.HasOpPermission(d['playername']):
            gui = mc.creatGUI('§2skick面板')
            gui.AddLabel("§e让我猜猜要踢谁呢")
            gui.AddDropdown('要踢谁？',0,str(list1))
            gui.AddInput('提示语是啥？','写在这里哦')
            gui.SendToPlayer(d['uuid'])
            return False
def formselect(a):
    d = eval(str(a).replace('null','None'))
    if not d['selected'] == None:
        mc.disconnectClient(pfapi.GetUUID(list1[d['selected'][1]]),d['selected'][2])
