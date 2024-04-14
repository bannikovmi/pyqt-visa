#!/usr/bin/python

"""
Author: Mikhail Bannikov bannikovmi96@gmail.com
"""

# pyqt-related imports
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QGridLayout, QWidget

# local imports
from .magnet_control import QMagnetControlWidget
from .magnet_graph import QMagnetMonitorWidget

class QMagnetTab(QWidget):

    def __init__(self, config, data):
        
        super().__init__()
        
        self.config = config
        self.data = data
        self.initUI()

    def initUI(self):
    
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.magnet_control_widget = QMagnetControlWidget(self.config, self.data)
        self.grid.addWidget(self.magnet_control_widget, 0, 0)
        
        self.magnet_monitor_widget = QMagnetMonitorWidget(self.config, self.data)
        self.grid.addWidget(self.magnet_monitor_widget, 0, 1)

        self.grid.setColumnStretch(1, 1)

    # def on_timer_event(self):

    #     self.temp_monitor_widget.on_timer_event()
    #     self.temp_control_widget.on_timer_event()
