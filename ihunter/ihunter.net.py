#! /usr/bin/env python
# -*- coding:utf-8 -*-
money = {}
def load_plugin():
    print("加载成功!")
    f = open("./plugins/ihunter/Money.txt")
    while True:
        line =f.readline()
        if line:
            line=line.rstrip("\n")
            linee = line.split(': ', 1 )
            money[linee[0]] = linee[1]
        else:
            break
    f.close()
    print(money)
    print("[ihunter] 配置文件读取完成！")
def mobdie(a):
    #print(a)
    d = eval(a)
    mobn = d['mobtype'].split('.', 2 )
    mc.runcmd("scoreboard players add \""+str(d['srcname'])+"\" money "+money[mobn[1]])
    mc.runcmd("title \""+str(d['srcname'])+"\" actionbar §2击杀奖励§6"+money[mobn[1]]+"§2金币！")