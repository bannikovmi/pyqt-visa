# standart library imports
import sys, os

# pyqt-related imports
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QCheckBox, QGridLayout, QGroupBox, QLabel, QLineEdit, QWidget
import pyqtgraph as pg


class QMagnetMonitorWidget(QGroupBox):

    def __init__(self, config, data, label="Field monitor"):

        super().__init__(label)
        self.config = config
        self.data = data
        self.initUI()

    def initUI(self):

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.current_graph_widget = QCurrentGraphWidget()
        self.grid.addWidget(self.current_graph_widget, 0, 0)

        self.field_graph_widget = QFieldGraphWidget()
        self.grid.addWidget(self.field_graph_widget, 1, 0)

class QCurrentGraphWidget(pg.PlotWidget):
    
    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        self.setBackground('w')

        self.styles = {'color':'b', 'font-size':'12pt'}
        self.setLabel('bottom', 'Time (s)', **self.styles)
        self.setLabel('left', 'Current (A)', **self.styles)
        
        self.ticks_font = QFont()
        self.ticks_font.setPixelSize(15)
        self.plotItem.getAxis("bottom").setTickFont(self.ticks_font)
        self.plotItem.getAxis("left").setTickFont(self.ticks_font)

        self.plotItem.showGrid(x=True, y=True)
        self.pen = pg.mkPen(color=(0, 0, 0), width=3)

        self.line = self.plotItem.plot([], [], pen=self.pen)

class QFieldGraphWidget(pg.PlotWidget):
    
    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        self.setBackground('w')

        self.styles = {'color':'b', 'font-size':'12pt'}
        self.setLabel('bottom', 'Time (s)', **self.styles)
        self.setLabel('left', 'Field (T)', **self.styles)
        
        self.ticks_font = QFont()
        self.ticks_font.setPixelSize(15)
        self.plotItem.getAxis("bottom").setTickFont(self.ticks_font)
        self.plotItem.getAxis("left").setTickFont(self.ticks_font)

        self.plotItem.showGrid(x=True, y=True)
        self.pen = pg.mkPen(color=(0, 0, 0), width=3)

        self.line = self.plotItem.plot([], [], pen=self.pen)



class QTempMonitorWidget(QGroupBox):

    def __init__(self, config, data, label="Temperature monitor"):

        super().__init__(label)
        self.config = config
        self.data = data
        self.initUI()

    def initUI(self):

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.temp_graph_widget = QTempGraphWidget()
        self.grid.addWidget(self.temp_graph_widget, 0, 0, 3, 1)

        self.sp_cb = QCheckBox("Show SP")
        # self.sp_cb.checked.connect()
        self.temp_label = QLabel("Temperature[K]")
        self.temp_le = QLineEdit()
        self.temp_le.setDisabled(True)

        self.rate_label = QLabel('Temp rate [K/min]')
        self.rate_le = QLineEdit()
        self.rate_le.setDisabled(True)

        self.grid.addWidget(self.sp_cb, 0, 1, 2, 1)
        self.grid.addWidget(self.temp_label, 0, 2)
        self.grid.addWidget(self.temp_le, 0, 3)

        self.grid.addWidget(self.rate_label, 1, 2)
        self.grid.addWidget(self.rate_le, 1, 3)  

        self.rate_method_widget = QRateMethodWidget()
        self.grid.addWidget(self.rate_method_widget, 0, 4, 2, 1)

        self.rate_graph_widget = QTempRateGraphWidget()
        self.grid.addWidget(self.rate_graph_widget, 2, 1, 1, 4)

        self.grid.setColumnStretch(0, 1)

    def on_timer_event(self):
        pass

class QTempGraphWidget(pg.PlotWidget):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        self.setBackground('w')

        self.styles = {'color':'b', 'font-size':'12pt'}
        self.setLabel('bottom', 'Time (s)', **self.styles)
        
        self.ticks_font = QFont()
        self.ticks_font.setPixelSize(15)
        self.plotItem.getAxis("bottom").setTickFont(self.ticks_font)
        self.plotItem.getAxis("left").setTickFont(self.ticks_font)

        self.plotItem.showGrid(x=True, y=True)
        self.pen = pg.mkPen(color=(0, 0, 0), width=3)

        self.line = self.plotItem.plot([], [], pen=self.pen)

class QTempRateGraphWidget(pg.PlotWidget):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        self.setBackground('w')

        self.styles = {'color':'b', 'font-size':'12pt'}
        self.setLabel('bottom', 'Time (s)', **self.styles)
        
        self.ticks_font = QFont()
        self.ticks_font.setPixelSize(15)
        self.plotItem.getAxis("bottom").setTickFont(self.ticks_font)
        self.plotItem.getAxis("left").setTickFont(self.ticks_font)

        self.plotItem.showGrid(x=True, y=True)
        self.pen = pg.mkPen(color=(0, 0, 0), width=3)

        self.line = self.plotItem.plot([], [], pen=self.pen)
