#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  visalab_dialogs.py
#  
#  Copyright 2022 Cryogenic System <Cryogenic System@CRYOGENICSYSTEM>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from PyQt5 import QtCore, QtGui, QtWidgets

class sweep_Ui_Form(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(400, 100)
		
		self.tumbler = QtWidgets.QCheckBox(self)
		self.tumbler.setObjectName('sweepTumbler')
		self.tumbler.setChecked(True)
		self.okBtn = QtWidgets.QPushButton(Dialog)
		self.okBtn.setObjectName('okBtn')
    
		self.cancelBtn = QtWidgets.QPushButton(Dialog)
		self.cancelBtn.setObjectName('cancelBtn')
		self.scanBtn = QtWidgets.QPushButton(Dialog)
		self.scanBtn.setObjectName('scanBtn')
		self.devList = QtWidgets.QComboBox(Dialog)
		self.devList.setObjectName('devList')
		self.increment = QtWidgets.QDoubleSpinBox(Dialog)
		self.increment.setObjectName('increment')
		self.increment.setValue(0)
		self.increment.setMinimum(-100000)
		self.increment.setMaximum(100000)
		self.vStart = QtWidgets.QDoubleSpinBox(Dialog)
		self.vStart.setObjectName('vStart')
		self.vStart.setValue(0)
		self.vStart.setMinimum(-100000)
		self.vStart.setMaximum(100000)
		self.vStop = QtWidgets.QDoubleSpinBox(Dialog)
		self.vStop.setObjectName('vStop')
		self.vStop.setValue(0)
		self.vStop.setMinimum(-100000)
		self.vStop.setMaximum(100000)
		self.vCurrent = QtWidgets.QLineEdit(Dialog)
		self.vCurrent.setObjectName('vCurrent')
		self.vCurrent.setText('0')
		self.vCurrent.setReadOnly(True)
		self.command = QtWidgets.QLineEdit(Dialog)
		self.command.setObjectName('command')
		self.label1 = QtWidgets.QLabel(Dialog)
		self.label1.setObjectName('label1')
		self.label2 = QtWidgets.QLabel(Dialog)
		self.label2.setObjectName('label1')
		self.label3 = QtWidgets.QLabel(Dialog)
		self.label3.setObjectName('label1')
		self.label4 = QtWidgets.QLabel(Dialog)
		self.label4.setObjectName('label1')
		self.label5 = QtWidgets.QLabel(Dialog)
		self.label5.setObjectName('label1')
		self.label6 = QtWidgets.QLabel(Dialog)
		self.label6.setObjectName('label1')
	    
		self.vlayout = QtWidgets.QVBoxLayout()
		self.vlayout.setObjectName('vlayout')
		self.hlayout = QtWidgets.QHBoxLayout()
		self.hlayout.setObjectName('hlayout')
		self.mainlayout = QtWidgets.QVBoxLayout(Dialog)
		self.mainlayout.setObjectName('mainlayout')
		self.hlayout.addWidget(self.okBtn)
		self.hlayout.addWidget(self.cancelBtn)
		self.vlayout.addWidget(self.tumbler)
		self.vlayout.addWidget(self.scanBtn)
		self.vlayout.addWidget(self.label5)
		self.vlayout.addWidget(self.devList)
		self.vlayout.addWidget(self.label6)
		self.vlayout.addWidget(self.command)
		self.vlayout.addWidget(self.label4)
		self.vlayout.addWidget(self.vCurrent)
		self.vlayout.addWidget(self.label1)
		self.vlayout.addWidget(self.vStart)
		self.vlayout.addWidget(self.label2)
		self.vlayout.addWidget(self.vStop)
		self.vlayout.addWidget(self.label3)
		self.vlayout.addWidget(self.increment)
		self.mainlayout.addLayout(self.vlayout)
		self.mainlayout.addLayout(self.hlayout)
    # ~ vlayout=new QVBoxLayout;
    # ~ hlayout=new QHBoxLayout;
    # ~ mainlayout=new QVBoxLayout;
    # ~ hlayout->addWidget(okButton);
    # ~ hlayout->addWidget(cancelButton);
    # ~ vlayout->addWidget(tumbler);
    # ~ vlayout->addWidget(scanButton);
    # ~ vlayout->addWidget(label5);
    # ~ vlayout->addWidget(devList);
    # ~ vlayout->addWidget(label6);
    # ~ vlayout->addWidget(command);
    # ~ vlayout->addWidget(label4);
    # ~ vlayout->addWidget(vCurrent);
    # ~ vlayout->addWidget(label1);
    # ~ vlayout->addWidget(vStart);
    # ~ vlayout->addWidget(label2);
    # ~ vlayout->addWidget(vStop);
    # ~ vlayout->addWidget(label3);
    # ~ vlayout->addWidget(increment);
    # ~ mainlayout->addLayout(vlayout);
    # ~ mainlayout->addLayout(hlayout);
		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)
	
	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Sweep dialog", "Sweep dialog"))
		self.okBtn.setText(_translate("OK", "OK"))
		self.cancelBtn.setText(_translate("Cancel", "Cancel"))
		self.scanBtn.setText(_translate("Scan for instruments", 
        "Scan for instruments"))
		self.tumbler.setText(_translate("Enable sweep", "Enable sweep"))
        # ~ QLabel *label1=new QLabel(tr("Start value:"), this);
    # ~ QLabel *label2=new QLabel(tr("Stop value:"), this);
    # ~ QLabel *label3=new QLabel(tr("Increment value:"), this);
    # ~ QLabel *label4=new QLabel(tr("Current value:"), this);
    # ~ QLabel *label5=new QLabel(tr("Device list"), this);
    # ~ QLabel *label6=new QLabel(tr("Write Command:"), this);
		self.label1.setText(_translate("Start value:", "Start value:"))
		self.label2.setText(_translate("Stop value:", "Stop value:"))
		self.label3.setText(_translate("Increment value:", "Increment value:"))
		self.label4.setText(_translate("Current value:", "Current value:"))
		self.label5.setText(_translate("Device list", "Device list"))
		self.label6.setText(_translate("Write command", "Write command"))
 
class sweepDialog(QtWidgets.QDialog, sweep_Ui_Form):
	
	def __init__(self):
		super(sweepDialog, self).__init__()
		self.setupUi(self)
		self.setWindowTitle('Sweep settings')
		
		self.okBtn.clicked.connect(self.accept)
		self.cancelBtn.clicked.connect(self.reject)
		self.tumbler.stateChanged.connect(self.toggleEnabled)
	
	def toggleEnabled(self, state):
		if state == 2:
			self.scanBtn.setEnabled(True)
			self.devList.setEnabled(True)
			self.command.setEnabled(True)
			self.increment.setEnabled(True)
			self.vStart.setEnabled(True)
			self.vStop.setEnabled(True)
			self.vCurrent.setEnabled(True)
		else:
			self.scanBtn.setEnabled(False)
			self.devList.setEnabled(False)
			self.command.setEnabled(False)
			self.increment.setEnabled(False)
			self.vStart.setEnabled(False)
			self.vStop.setEnabled(False)
			self.vCurrent.setEnabled(False)
