#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author : Sbaoor
# date   : 2021/1/8
import mc
import tool
def load_plugin():
    mc.setCommandDescribe('motd','服务器查询')
    print('[BlackBeTool] 云黑插件已装载')
    
def respawn(a):
    d = eval(a)
    ifban = tool.HttpGet('http://blackbe.xyz/api/check?id='+str(d['playername']),'')
    if ifban != '0':
        mc.disconnectClient(d['uuid'],'§4很抱歉您在BlackBe黑名单上，不能在此服务器游玩')
        print('[BlackBe] 发现玩家'+d['playername']+'在BlackBe黑名单上，已断开连接')

def inputcommand(a):
    d = eval(a)
    if d['cmd'].startswith('/motd'): 
        cmmd = str(d['cmd']).split(' ',2)
        pl = '\"'+str(d['playername'])+'\"'
        ser = eval(tool.HttpGet('http://motdpe.blackbe.xyz/api.php?ip='+cmmd[1]+'&port='+cmmd[2],''))
        if ser['status'] != 'offline':
            msg = '---§2M§3O§6T§eD§r---\n'+'§2描述§r：'+str(ser['motd'])+'\n'+'§3在线人数§r：'+str(ser['online'])+'/'+str(ser['max'])+'\n'+'§e延迟§r：'+str(ser['delay'])+'\n感谢BlackBe提供的MOTD接口'
            mc.tellraw(pl,msg)
            return False
        else:
            mc.tellraw(pl,'[MOTD] §4服务器离线')
            return False