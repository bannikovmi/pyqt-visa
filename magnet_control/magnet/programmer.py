# third-party imports
import numpy as np

# pyqt-related imports
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QGridLayout, QGroupBox, QLabel, QPushButton, QTextEdit)

import pyqtgraph as pg

class QSourceProgrammerWidget(QGroupBox):

    exec_started = pyqtSignal()
    exec_aborted = pyqtSignal()

    def __init__(self, config, data, label = "Programmer"):

        super().__init__(label)
        self.config = config
        self.data = data
        self.initUI()

    def initUI(self):
        
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.code_label = QLabel("Code")
        self.code_te = QTextEdit()
        
        self.grid.addWidget(self.code_label, 0, 0)
        self.grid.addWidget(self.code_te, 1, 0, 1, 3)

        self.preview_pb = QPushButton("Preview")
        self.exec_pb = QPushButton("Execute")
        self.abort_pb = QPushButton("Abort")

        self.grid.addWidget(self.preview_pb, 2, 0)
        self.grid.addWidget(self.exec_pb, 2, 1)
        self.grid.addWidget(self.abort_pb, 2, 2)
        self.abort_pb.setDisabled(True)

        self.output_label = QLabel("Output")
        self.output_te = QTextEdit()
        self.output_te.setDisabled(True)

        self.grid.addWidget(self.output_label, 3, 0)
        self.grid.addWidget(self.output_te, 4, 0, 1, 3)

        # Connect signals
        self.preview_pb.clicked.connect(self.on_preview)
        self.exec_pb.clicked.connect(self.on_exec)
        self.abort_pb.clicked.connect(self.on_abort)

    def on_preview(self):
        pass

    def on_exec(self):

        self.preview_pb.setDisabled(True)
        self.exec_pb.setDisabled(True)
        self.abort_pb.setDisabled(False)
        self.exec_started.emit()

    def on_abort(self):

        self.preview_pb.setDisabled(False)
        self.exec_pb.setDisabled(False)
        self.abort_pb.setDisabled(True)
        self.exec_aborted.emit()

    def disable_interface(self, state):

        self.preview_pb.setDisabled(state)
        self.exec_pb.setDisabled(state)
        self.code_te.setDisabled(state)
