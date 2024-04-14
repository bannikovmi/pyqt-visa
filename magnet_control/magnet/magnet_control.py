# third-party imports
import numpy as np

# pyqt-related imports
from PyQt5.QtWidgets import QGridLayout, QGroupBox

import pyqtgraph as pg

# local imports
from .metrics import QMagnetMetricsWidget
from .programmer import QSourceProgrammerWidget
from .ramp import QSourceRampWidget
from .status import QSourceStatusWidget

class QMagnetControlWidget(QGroupBox):

    def __init__(self, config, data, label = "Magnet control"):

        super().__init__(label)
        self.config = config
        self.data = data
        self.initUI()

    def initUI(self):
        
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        # Initialize custom widgets
        self.magnet_metrics_widget = QMagnetMetricsWidget(self.config, self.data)
        self.source_ramp_widget = QSourceRampWidget(self.config, self.data)
        self.source_programmer_widget = QSourceProgrammerWidget(self.config, self.data)
        self.source_status_widget = QSourceStatusWidget(self.config, self.data)

        # Let ramp widget know about source field updates
        self.magnet_metrics_widget.source_field_le.textChanged.connect(
            self.source_ramp_widget.on_field_change)

        # Disable Programmer interface on ramp start and enable it on ramp abort
        self.source_ramp_widget.ramp_aborted.connect(lambda:
            self.source_programmer_widget.disable_interface(False))
        self.source_ramp_widget.ramp_started.connect(lambda:
            self.source_programmer_widget.disable_interface(True))

        # Disable Ramp interface on programmer execute and enable it on programmer abort
        self.source_programmer_widget.exec_aborted.connect(lambda:
            self.source_ramp_widget.disable_interface(False))
        self.source_programmer_widget.exec_started.connect(lambda:
            self.source_ramp_widget.disable_interface(True))

        # Add custom widgets to grid
        self.grid.addWidget(self.magnet_metrics_widget, 0, 0)
        self.grid.addWidget(self.source_ramp_widget, 1, 0)
        self.grid.addWidget(self.source_programmer_widget, 2, 0)
        self.grid.addWidget(self.source_status_widget, 3, 0)

        self.grid.setRowStretch(3, 1)
