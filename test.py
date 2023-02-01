#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test.py
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
#import numpy as np
import pyvisa as visa
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, QRegExp
from PyQt5.QtGui import QRegExpValidator, QFont
#from guiqwt.builder import make
import test_ui  # Это наш конвертированный файл дизайна
import numpy as np
#import socket
from time import time, gmtime

class ExampleApp(QtWidgets.QWidget, test_ui.Ui_Form):
	def __init__(self):
    # Это здесь нужно для доступа к переменным, методам
    # и т.д. в файле esp_meteo_ui.py
		super().__init__()
		self.setupUi(self)  # Это нужно для инициализации нашего дизайна
		
		self.dev_list=[]
		self.current_instr=''
		self.run_timer = QTimer()
		self.try_count = 0
				
		self.startBtn.setEnabled(False)
		self.stopBtn.setEnabled(False)
		self.qEdit.setEnabled(False)
		self.aEdit.setReadOnly(True)
				
		
		self.scanBtn.clicked.connect(self.onScan)
		self.startBtn.clicked.connect(self.onStart)
		self.stopBtn.clicked.connect(self.onStop)
		self.devCombo.currentTextChanged.connect(self.onDevChange)
		self.exitBtn.clicked.connect(self.close)
		self.run_timer.timeout.connect(self.getData)
		
	def onDevChange(self):
		print('Current device changed!')
		self.current_instr = self.devCombo.currentText()
		print('Selected device is {0}'.format(self.current_instr))
	
	def onScan(self):
		#print('Scan clicked!')
		try:
			self.rm = visa.ResourceManager()
			self.dev_list = self.rm.list_resources()
			for d in self.dev_list:
				self.devCombo.addItem(d)
			self.startBtn.setEnabled(True)
			self.qEdit.setEnabled(True)
			self.current_instr=self.devCombo.currentText()
			print(self.current_instr)
		except Exception:
			print('Error reading device list!')
		
	def onStart(self):
		print('Start clicked!')
		self.run_timer.setInterval(self.delaySpin.value()*1000)
		self.run_timer.start()
		self.stopBtn.setEnabled(True)
		self.devCombo.setEnabled(False)
		self.qEdit.setEnabled(False)
		self.startBtn.setEnabled(False)
		
	def onStop(self):
		print('Stop clicked!')
		self.run_timer.stop() # останавливаем таймер
		self.devCombo.setEnabled(True)
		self.qEdit.setEnabled(True)
		self.stopBtn.setEnabled(False)
		self.startBtn.setEnabled(True)
			
	def getData(self):
		try:
			inst = self.rm.open_resource(self.current_instr)
			self.aEdit.setText(inst.query(self.qEdit.text()))
		except Exception:
			print('Device communication failed!')
			if self.try_count<3:
				self.try_count = self.try_count + 1
			else:
				self.try_count = 0
				self.onStop()
		
		
def main(args):
	app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
	window = ExampleApp()  # Создаём объект класса ExampleApp
	window.show()  # Показываем окно
	app.exec_()  # и запускаем приложение
	
	
#	inst = rm.open_resource('GPIB0::16::INSTR')
#	while True:
#		print(inst.query("FETCh?"))
#		time.sleep(1)
		
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
