#! /usr/bin/env python
# -*- coding:utf-8 -*-
import clr
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import *
#MessageBox.Show('awa','awa')
def load_plugin():
    pass
def destroyblock(a):
    d = eval(a)
    i = mc.creatPlayerObject(d['uuid'])
    i.addLevel(100)
    gui = mc.creatGUI("test")
    gui.AddLabel("123")
    gui.AddInput('随便来的什么？','写在这里哦')
    gui.AddSlider('这是游标滑块哦',1,10)
    gui.AddToggle('这是一个开关')
    gui.AddStepSlider('这是一个矩阵滑块',0,'[1,2,3]')
    gui.AddDropdown('如你所见，下拉框',0,'[1,2,3]')
    gui.SendToPlayer(d['uuid'])
    