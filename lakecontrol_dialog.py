# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'py-tcontrol.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import logging

class tc_ui_Form(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(Dialog.minimumSizeHint())
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.scanButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scanButton.setFont(font)
        self.scanButton.setObjectName("scanButton")
        self.gridLayout_2.addWidget(self.scanButton, 1, 0, 1, 1)
        self.instrList = QtWidgets.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.instrList.setFont(font)
        self.instrList.setObjectName("instrList")
        self.gridLayout_2.addWidget(self.instrList, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)
        self.getButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.getButton.setFont(font)
        self.getButton.setObjectName("getButton")
        self.gridLayout_3.addWidget(self.getButton, 1, 0, 1, 1)
        self.ConfigBox = QtWidgets.QTextEdit(Dialog)
        self.ConfigBox.setObjectName("ConfigBox")
        self.gridLayout_3.addWidget(self.ConfigBox, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.setpUpd = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.setpUpd.setFont(font)
        self.setpUpd.setObjectName("setpUpd")
        self.verticalLayout_3.addWidget(self.setpUpd)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.setpSpin = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.setpSpin.setObjectName("setpSpin")
        self.setpSpin.setMinimum(0)
        self.setpSpin.setMaximum(350)
        self.verticalLayout_3.addWidget(self.setpSpin)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.rampUpd = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rampUpd.setFont(font)
        self.rampUpd.setObjectName("rampUpd")
        self.verticalLayout_4.addWidget(self.rampUpd)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.rampSpin = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.rampSpin.setObjectName("rampSpin")
        self.rampSpin.setMinimum(0)
        self.rampSpin.setMaximum(20)
        self.verticalLayout_4.addWidget(self.rampSpin)
        self.rampSwitch = QtWidgets.QCheckBox(self.groupBox)
        self.rampSwitch.setObjectName("rampSwitch")
        self.verticalLayout_4.addWidget(self.rampSwitch)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.heaterCombo = QtWidgets.QLabel(self.groupBox_2)
        self.heaterCombo.setObjectName("heaterCombo")
        self.gridLayout_4.addWidget(self.heaterCombo, 1, 0, 1, 1)
        self.hrangeCombo = QtWidgets.QComboBox(self.groupBox_2)
        self.hrangeCombo.setObjectName("hrangeCombo")
        self.gridLayout_4.addWidget(self.hrangeCombo, 2, 0, 1, 1)
        self.heaterUpd = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.heaterUpd.setFont(font)
        self.heaterUpd.setObjectName("heaterUpd")
        self.gridLayout_4.addWidget(self.heaterUpd, 0, 0, 1, 1)
        self.analogSpin = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.analogSpin.setObjectName("analogSpin")
        self.analogSpin.setMinimum(0)
        self.analogSpin.setMaximum(100)
        self.gridLayout_4.addWidget(self.analogSpin, 12, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 11, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 1, 1, 1, 1)
        self.houtSpin = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.houtSpin.setObjectName("houtSpin")
        self.gridLayout_4.addWidget(self.houtSpin, 2, 1, 1, 1)
        self.loopCombo = QtWidgets.QComboBox(self.groupBox_2)
        self.loopCombo.setObjectName("loopCombo")
        self.gridLayout_4.addWidget(self.loopCombo, 8, 1, 1, 1)
        self.analogUpd = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.analogUpd.setFont(font)
        self.analogUpd.setObjectName("analogUpd")
        self.gridLayout_4.addWidget(self.analogUpd, 10, 0, 1, 1)
        self.analogCombo = QtWidgets.QComboBox(self.groupBox_2)
        self.analogCombo.setObjectName("analogCombo")
        self.gridLayout_4.addWidget(self.analogCombo, 12, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 11, 1, 1, 1)
        self.powerSwitch = QtWidgets.QCheckBox(self.groupBox_2)
        self.powerSwitch.setObjectName("powerSwitch")
        self.gridLayout_4.addWidget(self.powerSwitch, 8, 0, 1, 1)
        self.hoffBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.hoffBtn.setObjectName("hoffBtn")
        self.gridLayout_4.addWidget(self.hoffBtn, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 5, 0, 1, 1)
        self.setResBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.setResBtn.setObjectName("setResBtn")
        self.gridLayout_4.addWidget(self.setResBtn, 6, 1, 1, 1)
        self.hResSpin = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.hResSpin.setObjectName("hResSpin")
        self.hResSpin.setMinimum(1)
        self.hResSpin.setMaximum(10000)
        self.gridLayout_4.addWidget(self.hResSpin, 6, 0, 1, 1)
        self.loopLabel = QtWidgets.QLabel(self.groupBox_2)
        self.loopLabel.setObjectName("loopLabel")
        self.gridLayout_4.addWidget(self.loopLabel, 7, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 2, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout.setObjectName("formLayout")
        self.prunBtn = QtWidgets.QPushButton(self.groupBox_3)
        self.prunBtn.setObjectName("prunBtn")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.prunBtn)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_7)
        self.ptermBtn = QtWidgets.QPushButton(self.groupBox_3)
        self.ptermBtn.setObjectName("ptermBtn")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.ptermBtn)
        self.programCombo = QtWidgets.QComboBox(self.groupBox_3)
        self.programCombo.setObjectName("programCombo")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.programCombo)
        self.gridLayout.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.messageLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.messageLabel.setFont(font)
        self.messageLabel.setObjectName("messageLabel")
        self.verticalLayout.addWidget(self.messageLabel)
        self.messageBox = QtWidgets.QTextEdit(Dialog)
        self.messageBox.setObjectName("messageBox")
        self.verticalLayout.addWidget(self.messageBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.exitButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout_2.addWidget(self.exitButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Lakecontrol"))
        self.label.setText(_translate("Dialog", "Instruments List"))
        self.scanButton.setText(_translate("Dialog", "Scan for Lakeshores"))
        self.label_2.setText(_translate("Dialog", "Current instrument configuration"))
        self.getButton.setText(_translate("Dialog", "Get Current State"))
        self.groupBox.setTitle(_translate("Dialog", "Setpoint config"))
        self.setpUpd.setText(_translate("Dialog", "Update Setpoint"))
        self.label_3.setText(_translate("Dialog", "Current Setpoint [K]"))
        self.rampUpd.setText(_translate("Dialog", "Update Ramp"))
        self.label_5.setText(_translate("Dialog", "Ramp value [K/min]"))
        self.rampSwitch.setText(_translate("Dialog", "Ramp ON"))
        self.groupBox_2.setTitle(_translate("Dialog", "Heater config"))
        self.heaterCombo.setText(_translate("Dialog", "Heater Range"))
        self.heaterUpd.setText(_translate("Dialog", "Update Heater Settings"))
        self.label_8.setText(_translate("Dialog", "Analog Output [%]"))
        self.label_4.setText(_translate("Dialog", "Heater output [%]"))
        self.analogUpd.setText(_translate("Dialog", "Update AnalogOutput"))
        self.label_9.setText(_translate("Dialog", "Analog Channel"))
        self.powerSwitch.setText(_translate("Dialog", "Powerup Enable"))
        self.hoffBtn.setText(_translate("Dialog", "Heater off"))
        self.label_6.setText(_translate("Dialog", "Heater resistance"))
        self.setResBtn.setText(_translate("Dialog", "Set heater resistance"))
        self.loopLabel.setText(_translate("Dialog", "Control Loop"))
        self.groupBox_3.setTitle(_translate("Dialog", "Program settings"))
        self.prunBtn.setText(_translate("Dialog", "Run program"))
        self.label_7.setText(_translate("Dialog", "Program number"))
        self.ptermBtn.setText(_translate("Dialog", "Terminate program"))
        self.messageLabel.setText(_translate("Dialog", "Message Box"))
        self.exitButton.setText(_translate("Dialog", "Close"))

class lakecontrolApp(QtWidgets.QDialog, tc_ui_Form):
	
	
	def __init__(self, rm):
		super().__init__()
		self.setupUi(self)
		
		#self.rm = pyvisa.ResourceManager()
		self.flag = True
		self.state={}
		self.rm = rm
		self.current_dev = None
		self.analogCombo.addItems(['1','2'])
		self.loopCombo.addItems(['1'])
		self.hrangeCombo.addItems(['0', '1', '2', '3', '4', '5'])
		self.programCombo.addItems(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])							
		
		self.prunBtn.setEnabled(False)
		self.ptermBtn.setEnabled(False)
		self.hoffBtn.setEnabled(False)
		self.rampSwitch.setEnabled(False)
		
		
		self.getButton.clicked.connect(self.onGet)
		self.setpUpd.clicked.connect(self.onSetp)
		self.rampUpd.clicked.connect(self.onRamp)
		self.heaterUpd.clicked.connect(self.onHupd)
		self.hoffBtn.clicked.connect(self.onHoff)
		self.scanButton.clicked.connect(self.onScan)
		self.rampSwitch.stateChanged.connect(self.rSwitchchange)
		self.powerSwitch.stateChanged.connect(self.pSwitchchange)
		self.setResBtn.clicked.connect(self.onSetRes)
		self.exitButton.clicked.connect(self.close)
		self.analogUpd.clicked.connect(self.onAUpd)
		self.instrList.currentTextChanged.connect(self.onChange)
		self.prunBtn.clicked.connect(self.onRun)		
		self.ptermBtn.clicked.connect(self.onTerminate)		
		
	def onRun(self):
		if not self.current_dev == None:
			self.current_dev.write(f'PGMRUN {self.programCombo.currentText()}')
			self.prunBtn.setEnabled(False)
			self.ptermBtn.setEnabled(True)
			self.messageBox.append(f'Program {self.programCombo.currentText()} started')
	
	def onTerminate(self):
		if not self.current_dev == None:
			self.current_dev.write(f'PGMRUN 0')
			self.prunBtn.setEnabled(True)
			self.ptermBtn.setEnabled(False)
			self.messageBox.append(f'Program terminated')
	
	def onChange(self):
		self.current_dev = self.rm.open_resource(self.instrList.currentText())
		logging.info(f'onChange: current device is {self.instrList.currentText()}\n')
		self.updateState()
	
	def updateState(self):
		l=''
		self.flag = True
		st = self.current_dev.query('AOUT?1').strip()
		l += 'AnalogOut1: ' + st + '%\n'
		st = self.current_dev.query('AOUT?2').strip()
		l += 'AnalogOut2: ' + st + '%\n'
		st = self.current_dev.query('HTR?').strip()
		l += 'Heater output: ' + st + '%\n'
		self.houtSpin.setValue(float(st))
		st = self.current_dev.query('RAMP?1').strip()
		#l += f'Ramp state: {st}\n'
		try:
			ramp_on, ramp_rate = st.split(',')
			if ramp_on == '1':
				ramp = 'ON'
				self.rampSwitch.setChecked(True)
			elif ramp_on == '0':
				ramp = 'OFF'
				self.rampSwitch.setChecked(False)
			l += 'Ramp settings: ' + f'Ramp {ramp}, Ramp rate={ramp_rate}K/min' + '\n'
			self.rampSpin.setValue(float(ramp_rate))
		except Exception:
			logging.info('updateSettings: Unable to unpack ramp setings')
		
		st = self.current_dev.query('RAMPST?1').strip()
		if st == '0':
			st = 'idle'
		if st == '1':
			st = 'running'
		l += 'Ramp status: ' + st + '\n'
		st = self.current_dev.query('SETP?1').strip()
		l += 'Current setpoint: ' + st + 'K\n'	
		self.setpSpin.setValue(float(st))	
		st = self.current_dev.query('RANGE?').strip()
		if st == '0':
			l += 'Heater off'+'\n'
			self.hoffBtn.setEnabled(False)
		else:
			l += 'Heater range: ' + st + '\n'
			self.hoffBtn.setEnabled(True)
			
		self.hrangeCombo.setCurrentIndex(int(st))
		st = self.current_dev.query('CDISP?1').strip()
		disp_list = st.split(',')
		self.hResSpin.setValue(float(disp_list[1]))
		l += 'Display settings: ' + st + '\n'	
		st = self.current_dev.query('CSET?1').strip()
		loop_list = st.split(',')
		if loop_list[-1] == '1':
			self.powerSwitch.setChecked(True)
		elif loop_list[-1] == '0': 
			self.powerSwitch.setChecked(False)
		l += 'Loop1 settings: ' + st + '\n'
		st = self.current_dev.query('PGMRUN?').strip()
		logging.debug(f'Lakecontrol: program state = {st}')
		program, status = st.split(',')
		if program == '00':
			self.prunBtn.setEnabled(True)
			self.ptermBtn.setEnabled(False)
		else:
			l +=f'Program {program} is running'
			self.prunBtn.setEnabled(False)
			self.ptermBtn.setEnabled(True)
		self.ConfigBox.setText(l)
				
	
	def onAUpd(self):
		logging.debug('onAUpd: Update AnalogOut clicked!')
		if not self.current_dev == None:
			self.current_dev.write(f'ANALOG {self.analogCombo.currentText()},0,2,,,,,{self.analogSpin.value()}')
			self.messageBox.append(f'Analog out {self.analogCombo.currentText()} is set to {self.analogSpin.value()}')
	
	
	def onSetRes(self):
		logging.debug('onSetRes: Set resistivity clicked!')
		self.messageBox.append('Set resistivity clicked!')
		self.messageBox.append(f'Heater resistance is set to {self.hResSpin.value()}')
	
	def rSwitchchange(self, state):
		logging.info(f'Ramp switch state: {state}!')
		if state == 2 and not self.current_dev == None:
			if not self.flag == True:
				self.current_dev.write(f'RAMP 1, 1, {self.rampSpin.value()}')
			else:
				self.flag = False
			self.messageBox.append('Ramp on')
		elif state == 0 and not self.current_dev == None:
			if not self.flag == True:
				self.current_dev.write(f'RAMP 1, 0')
			else:
				self.flag = False
			self.messageBox.append('Ramp off')
			
	
	def pSwitchchange(self, state):
		logging.debug(f'Power switch state: {state}!')
		if state == 2 and not self.current_dev == None:
			self.current_dev.write(f'CSET 1,,,,1')
			self.messageBox.append('Loop1 powerup on')
		elif state == 0 and not self.current_dev == None:
			self.current_dev.write(f'CSET 1,,,,0')
			self.messageBox.append('Loop1 powerup off')
	
	def onGet(self):
		logging.debug('onGet: Get clicked!')
		if not self.current_dev == None:
			self.updateState()
	
	def onSetp(self):
		logging.debug('onSetp: Update setpoint clicked!')
		if not self.current_dev == None:
			self.current_dev.write(f'SETP 1,{self.setpSpin.value()}')
			self.messageBox.append(f'Setpoint is set to {self.setpSpin.value()}K')
		
	def onRamp(self):
		logging.debug('onRamp: Update ramp clicked!')
		if not self.current_dev == None:
			self.current_dev.write(f'RAMP 1,1,{self.rampSpin.value()}')
			self.messageBox.append(f'Ramp is set to {self.rampSpin.value()}K/min')
		
	def onHupd(self):
		logging.info('onHupd: Update heater clicked!')
		if not self.current_dev == None:
			self.current_dev.write(f'RANGE {self.hrangeCombo.currentText()}')
			self.messageBox.append(f'Heater range changed to {self.hrangeCombo.currentText()}')
			self.hoffBtn.setEnabled(True)
		
	def onHoff(self):
		logging.info('Heater off clicked!')
		if not self.current_dev == None:
			self.current_dev.write('RANGE 0')
			self.hoffBtn.setEnabled(False)
			self.messageBox.append('Heater off')
		
	def onScan(self):
		#logging.info('Scan clicked!')
		self.instrList.clear()
		#self.rm = pyvisa.ResourceManager()
		self.dev_list = self.rm.list_resources()
		for dev in self.dev_list:
			if not dev.find('GPIB') == -1:
				try:
					inst = self.rm.open_resource(dev)
					id_str = inst.query("*IDN?")
					if not id_str.find('MODEL340')==-1:
						self.instrList.addItem(dev)
						logging.info('onScan: LS340 found!')
				except Exception:
					logging.exception(f'OnScan: Error communicating with device {dev}!')
		if len(self.instrList)>0:
			self.current_dev = self.rm.open_resource(self.instrList.currentText())
			self.updateState()
			logging.info(f'onScan: current device is {self.instrList.currentText()}\n')
			#self.prunBtn.setEnabled(True)
			#self.ptermBtn.setEnabled(True)
			self.hoffBtn.setEnabled(True)
			self.rampSwitch.setEnabled(True)
		else:
			logging.info(f'Lakeshore340 devices on GPIB bus not found')
