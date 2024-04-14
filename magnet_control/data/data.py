#!/usr/bin/python

"""
This module contains a set of commands for communication with Thyracont VSP transducers
based on PyVISA library and custom data_packages module.

Author: Mikhail Bannikov bannikovmi96@gmail.com
"""

# pyqt-related imports
from PyQt5.QtCore import pyqtSignal, Qt, QObject 
from PyQt5.QtWidgets import (QCheckBox, QGridLayout, QGroupBox, QHeaderView,
	QTableWidget, QTableWidgetItem)

# third-party imports
import numpy as np

class QDataWidget(QGroupBox):

    def __init__(self, config, label="Data in files"):
        
        super().__init__(label)
        
        self.config = config
        self.data_dict = {}
        
        for name in self.config["data"]:
        	
        	is_updated = False
        	format_string = self.config["data"][name]["format_string"]
        	units = self.config["data"][name]["units"]
        	is_in_file = True
        	max_points_count = self.config["history"]["max_points_count"]

        	self.data_dict[name] = DataStorage(
        		name=name,
        		is_updated=is_updated,
        		format_string=format_string,
        		units=units,
        		is_in_file=is_in_file,
        		max_points_count=max_points_count
        	)

        self.initUI()

    def initUI(self):

        # Setup a grid layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        # Initialize a table widget
        self.table_widget = QTableWidget()
        self.grid.addWidget(self.table_widget, 0, 0)
      
      	# Set headers and max stretch to first column
        self.table_headers = ["name", "units", "value", "show in file", "format string"]
        self.table_widget.setColumnCount(len(self.table_headers))
        self.table_widget.setHorizontalHeaderLabels(self.table_headers)

       	self.table_widget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)

       	# Fill data dictionary with instances of DataStorage class
       	for row, name in enumerate(self.data_dict):

       		self.table_widget.insertRow(row)
       		self.table_widget.setItem(row, 0, QTableWidgetItem(name))
       		self.table_widget.setItem(row, 1, QTableWidgetItem(self.data_dict[name].units))
       		
       		# value
       		self.table_widget.setItem(row, 2, QTableWidgetItem(str("")))
       		self.data_dict[name].item = self.table_widget.item(row, 2)

       		self.table_widget.setItem(row, 3, QTableWidgetItem())
       		self.table_widget.item(row, 3).setCheckState(Qt.Checked)
       		self.table_widget.setItem(row, 4,
       			QTableWidgetItem(self.data_dict[name].format_string))

       		# Disable editing of items
       		for col in range(3):
       			item = self.table_widget.item(row, col)
       			if item is not None:
       				item.setFlags(item.flags() ^ Qt.ItemIsEditable) 


class DataStorage(QObject):
	
	value_updated = pyqtSignal()

	def __init__(self, 
		name: str = "",
		is_updated: bool = False,
		format_string: str = ".3f",
		units: str = "",
		is_in_file: bool = False,
		max_points_count: int = 10000, 
	):
		
		super().__init__()

		# Save data to local variables except is_updated flag,
		# which should remain False by default
		self.name = name
		self.format_string = format_string
		self.units = units
		self.is_in_file = is_in_file
		self.max_points_count = max_points_count

		# Create a list for storing history and a QTableWidgetItem for value updates 
		self.array = []
		self.item = None

	def update_value(self, value):
		
		self.item.setText(f'{value:{self.format_string}}')
		self.array.append(value)

		# Do not store too much data in an history
		if len(self.array) > self.max_points_count: 
			del self.array[0:len(self.array) - self.max_points_count]

		self.is_updated = True
		self.value_updated.emit()

		