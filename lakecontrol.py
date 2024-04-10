#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
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
#import pyvisa as visa
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot
import tcontrol_ui
import pyvisa
# import threading
# from concurrent.futures import ThreadPoolExecutor
# import numpy as np
from time import localtime, strftime, time
import logging

# class TestApp(QtWidgets.QWidget, visalab_dialogs.sweep_Ui_Form):
	# def __init__(self):
		# super().__init__()
		# self.setupUi(self)
		
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, 
	level=logging.INFO, 
	datefmt="%H:%M:%S")
# comment next line if debug is not needed	
# logging.getLogger().setLevel(logging.DEBUG)


class lakecontrolApp(QtWidgets.QDialog, tcontrol_ui.Ui_Dialog):
	
	
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		
		#self.rm = pyvisa.ResourceManager()
		self.state={}
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
		st = self.current_dev.query('AOUT?1').strip()
		l += 'AnalogOut1: ' + st + '%\n'
		st = self.current_dev.query('AOUT?2').strip()
		l += 'AnalogOut2: ' + st + '%\n'
		st = self.current_dev.query('HTR?').strip()
		l += 'Heater output: ' + st + '%\n'
		self.houtSpin.setValue(float(st))
		st = self.current_dev.query('RAMP?1').strip()
		l += f'Ramp state: {st}\n'
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
			logging.info('Unable to unpack ramp setings')
		
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
			self.current_dev.write(f'RAMP 1, 1, {self.rampSpin.value()}')
			self.messageBox.append('Ramp on')
		elif state == 0 and not self.current_dev == None:
			self.current_dev.write(f'RAMP 1, 0')
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
		self.rm = pyvisa.ResourceManager()
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
			self.prunBtn.setEnabled(True)
			self.ptermBtn.setEnabled(True)
			self.hoffBtn.setEnabled(True)
			self.rampSwitch.setEnabled(True)
		else:
			logging.info(f'Lakeshore340 devices on GPIB bus not found')
		
		
		
					
def main(args):
	app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
	window = lakecontrolApp()  # Создаём объект класса visaLabApp
	window.show()  # Показываем окно
	app.exec_()  # и запускаем приложение

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
