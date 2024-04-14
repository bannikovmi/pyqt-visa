# third-party imports
import numpy as np

# pyqt-related imports
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QCheckBox, QDoubleSpinBox, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QPushButton, QRadioButton)

class QSourceRampWidget(QGroupBox):

    ramp_aborted = pyqtSignal()
    ramp_started = pyqtSignal()

    FIELD_RAMP_BOUNDARIES = np.array([0, 16, 17.1, 18, 19])
    FIELD_RAMP_RATES = np.array([0.241, 0.157, 0.102, 0.057, 0.043])

    def __init__(self, config, data, label = "Ramp"):

        super().__init__(label)
        self.config = config
        self.data = data
        self.source_field = 0

        self.initUI()

    def initUI(self):
        
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        # Target field
        self.target_field_label = QLabel("Target field [T]")

        self.target_field_sb = QDoubleSpinBox()
        self.target_field_sb.setRange(-19, 19)
        self.target_field_sb.setDecimals(3)
        self.target_field_sb.setSingleStep(0.1)

        self.grid.addWidget(self.target_field_label, 0, 0)
        self.grid.addWidget(self.target_field_sb, 0, 1)

        # Rate
        self.target_rate_label = QLabel("Target rate [T/min]")

        self.target_rate_sb = QDoubleSpinBox()
        self.target_rate_sb.setRange(0, 0.241)
        self.target_rate_sb.setDecimals(4)
        self.target_rate_sb.setSingleStep(0.001)

        self.actual_rate_label = QLabel("Actual rate [T/min]")
        self.actual_rate_le = QLineEdit()
        self.actual_rate_le.setDisabled(True)
        self.actual_rate_le.setText("%.3f" % 0)

        self.grid.addWidget(self.target_rate_label, 1, 0)
        self.grid.addWidget(self.target_rate_sb, 1, 1)
        self.grid.addWidget(self.actual_rate_label, 1, 2)
        self.grid.addWidget(self.actual_rate_le, 1, 3)

        # Buttons
        self.start_pb = QPushButton("Start")
        self.abort_pb = QPushButton("Abort")
        self.abort_pb.setDisabled(True)

        self.grid.addWidget(self.start_pb, 0, 2)
        self.grid.addWidget(self.abort_pb, 0, 3)

        self.start_pb.clicked.connect(self.on_ramp_start)
        self.abort_pb.clicked.connect(self.on_ramp_abort)

        # Persistent switch

        self.persistent_switch_widget = QPersistentSwitchWidget(self.config)
        self.grid.addWidget(self.persistent_switch_widget, 2, 0, 1, 4)

        # Estimated time of arrival
        self.eta_label = QLabel("Estimated time of arrival")

        self.relative_rb = QRadioButton("Relative")
        self.absolute_rb = QRadioButton("Absolute")
        self.relative_rb.setChecked(True)

        self.eta_le = QLineEdit()
        self.eta_le.setText("00:00:00")
        self.eta_le.setDisabled(True)

        self.grid.addWidget(self.eta_label, 3, 0)
        self.grid.addWidget(self.relative_rb, 3, 1)
        self.grid.addWidget(self.absolute_rb, 3, 2)
        self.grid.addWidget(self.eta_le, 3, 3)

        # Connect signals
        self.target_rate_sb.valueChanged.connect(self.on_rate_change)

    def disable_interface(self, state):

        self.start_pb.setDisabled(state)
        self.target_field_sb.setDisabled(state)
        self.target_rate_sb.setDisabled(state)
        self.persistent_switch_widget.persistent_mode_cb.setDisabled(state)

        # Enable ramp_current_to_zero checkbox only if persistent_mode checkbox is checked
        if state: 
            self.persistent_switch_widget.ramp_current_to_zero_cb.setDisabled(True)
        else:
            self.persistent_switch_widget.ramp_current_to_zero_cb.setEnabled(
                self.persistent_switch_widget.persistent_mode_cb.isChecked())
            
    def on_field_change(self, field):
        
        self.source_field = float(field)
        self.actual_rate_le.setText(f"{min(self.target_rate_sb.value(),
            self._max_ramp_rate(float(field))):.4f}")

    def on_rate_change(self, new_rate):

        self.actual_rate_le.setText(f"{min(new_rate,
            self._max_ramp_rate(float(self.source_field))):.4f}")

    def on_ramp_abort(self):

        self.ramp_aborted.emit()
        self.disable_interface(False)
        self.abort_pb.setDisabled(True)

    def on_ramp_start(self):

        self.ramp_started.emit()
        self.disable_interface(True)
        self.abort_pb.setDisabled(False)


    def _max_ramp_rate(self, field):

        # Find index of closest yet smaller bound
        array = np.abs(field) - self.FIELD_RAMP_BOUNDARIES
        min_bound_index = np.where(array > 0, array, np.inf).argmin()
        
        return self.FIELD_RAMP_RATES[min_bound_index]

class QPersistentSwitchWidget(QGroupBox):

    def __init__(self, config, label = "Persistent switch"):

        super().__init__(label)
        self.config = config
        self.initUI()

    def initUI(self):
        
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.persistent_mode_cb = QCheckBox("Go to persistent mode on next target")
        self.persistent_mode_cb.setChecked(False)

        self.ramp_current_to_zero_cb = QCheckBox("Ramp source current to zero on next target")
        self.ramp_current_to_zero_cb.setChecked(False)
        self.ramp_current_to_zero_cb.setDisabled(True)

        self.grid.addWidget(self.persistent_mode_cb, 0, 0, 1, 2)
        self.grid.addWidget(self.ramp_current_to_zero_cb, 0, 2, 1, 2)

        self.heater_label = QLabel("Heater state")
        self.heater_le = QLineEdit()
        self.heater_le.setDisabled(True)
        self.heater_le.setText("OFF")

        self.grid.addWidget(self.heater_label, 2, 0)
        self.grid.addWidget(self.heater_le, 2, 1)

        self.persistent_field_label = QLabel("Persistent field [T]")
        self.persistent_field_le = QLineEdit()
        self.persistent_field_le.setDisabled(True)
        self.persistent_field_le.setText("%.3f" % 0)

        self.grid.addWidget(self.persistent_field_label, 2, 2)
        self.grid.addWidget(self.persistent_field_le, 2, 3)

        # Connect signals
        self.persistent_mode_cb.clicked.connect(self.on_persistent_mode)

    def on_persistent_mode(self, state):

        self.ramp_current_to_zero_cb.setEnabled(state)
