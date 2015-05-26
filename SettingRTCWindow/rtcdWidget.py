#!/bin/env python
# -*- encoding: utf-8 -*-

##
#   @file .py
#   @brief 



import thread


import optparse
import sys,os,platform
import traceback
import re
import time
import random
import commands
import math
import imp



import RTC
import OpenRTM_aist

from OpenRTM_aist import CorbaNaming
from OpenRTM_aist import RTObject
from OpenRTM_aist import CorbaConsumer
from omniORB import CORBA
import CosNaming

from PyQt4 import QtCore, QtGui

from SettingRTCConf.MTabWidget import MTabWidget



class rtcdWidget(MTabWidget):
    
    def __init__(self, parent=None):
        MTabWidget.__init__(self, None, parent)
        self.parent = parent
        self.addTextBox("textBox", u"IPアドレス", ["localhost"] , "localhost")
        self.addTextBox("filepath", u"ファイル名", [""] , "")

        self.addFilePathButton = QtGui.QPushButton(u"ファイル名設定")
        self.WidList["filepath"]["Layout"].addWidget(self.addFilePathButton)
        self.addFilePathButton.clicked.connect(self.addFilePathSlot)

        self.addLoadButton = QtGui.QPushButton(u"ファイル読み込み")
        self.WidList["filepath"]["Layout"].addWidget(self.addLoadButton)
        self.addLoadButton.clicked.connect(self.addLoadSlot)


        self.newFileButton = QtGui.QPushButton(u"新規作成")
        self.WidList["filepath"]["Layout"].addWidget(self.newFileButton)
        self.newFileButton.clicked.connect(self.newFileSlot)


        self.saveFileButton = QtGui.QPushButton(u"ファイル保存")
        self.WidList["filepath"]["Layout"].addWidget(self.saveFileButton)
        self.saveFileButton.clicked.connect(self.saveFileSlot)

        self.rtcdButton = QtGui.QPushButton(u"rtcd起動")
        self.WidList["filepath"]["Layout"].addWidget(self.rtcdButton)
        self.rtcdButton.clicked.connect(self.rtcdSlot)
        

    def rtcdSlot(self):
        try:
            self.parent.setDataCpp()
            self.parent.setDataPy()
            self.parent.control_comp._rtcconf._ptr().startRTCD_Cpp()
            self.parent.control_comp._rtcconf._ptr().startRTCD_Py()
            self.parent.control_comp._rtcconf._ptr().setSystem()
        except:
            info = sys.exc_info()
            tbinfo = traceback.format_tb( info[2] )
            for tbi in tbinfo:
                print tbi

    def addLoadSlot(self):
        self.parent.createTabs(str(self.WidList["filepath"]["Widget"].text().toLocal8Bit()))

    def addFilePathSlot(self):
        wid = self.WidList["filepath"]["Widget"]
        text = self.parent.getFilePath()
        
            
        
        wid.setText(text)

    def newFileSlot(self):
        self.parent.newFile()
        
    def saveFileSlot(self):
        pass

    def delLangSlot(self):
        wid = self.WidList["manager.supported_languages"]["Widget"]
        wid.removeItem(wid.findText(wid.currentText()))

    def createCompSlot(self):
        wid = self.WidList["manager.components.precreate"]["Widget"]
        s = str(wid.currentText().toLocal8Bit())
        
        comp = self.mgrc.mgr.createComponent(s)
        if not comp:
            self.mesBox(u"RTCの起動に失敗しました")
            return
        wid.addItem(wid.currentText())

        self.mgrc.addComp(s, comp)

    def delCompSlot(self):
        wid = self.WidList["manager.components.precreate"]["Widget"]
        self.mgrc.deleteComp(str(wid.currentText().toLocal8Bit()))
        wid.removeItem(wid.findText(wid.currentText()))

        

    def delModuleSlot(self):
        wid = self.WidList["manager.modules.preload"]["Widget"]
        wid.removeItem(wid.findText(wid.currentText()))

    def delPathSlot(self):
        wid = self.WidList["manager.modules.load_path"]["Widget"]
        wid.removeItem(wid.findText(wid.currentText()))

    def loadRTCSlot(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self,u"開く","","Python File (*.py);;All Files (*)")

        if fileName.isEmpty():
            return
        ba = str(fileName.toLocal8Bit())
        fname = os.path.basename(ba)
        name, ext = os.path.splitext(fname)
        dname = os.path.dirname(os.path.relpath(ba))
        if self.mgrc.createComp(name,[dname]) == False:
            self.mesBox(u"モジュールの読み込みに失敗しました")
            return

        wid = self.WidList["manager.components.precreate"]["Widget"]
        wid.addItem(name)

        wid = self.WidList["manager.modules.preload"]["Widget"]
        if wid.findText(fname) == -1:
            wid.addItem(fname)

        wid = self.WidList["manager.modules.load_path"]["Widget"]

        if dname == "":
            dname = "./" + dname
        if wid.findText(dname) == -1:
            
            wid.addItem(dname)
