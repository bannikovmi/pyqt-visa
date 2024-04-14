# pyqt-related imports
from PyQt5.QtWidgets import QGridLayout, QGroupBox, QLabel, QLineEdit, QPushButton

class QMagnetMetricsWidget(QGroupBox):

    def __init__(self, config, data, label = "Metrics"):

        super().__init__(label)
        self.config = config
        self.data = data
        self.initUI()

    def initUI(self):
        
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        # Source current
        self.source_current_label = QLabel("Source current [A]")

        self.source_current_le = QLineEdit()
        self.source_current_le.setDisabled(True)
        self.source_current_le.setText("%.3f" % 0)

        self.grid.addWidget(self.source_current_label, 0, 0)
        self.grid.addWidget(self.source_current_le, 0, 1)

        # Source voltage
        self.source_voltage_label = QLabel("Source voltage [V]")

        self.source_voltage_le = QLineEdit()
        self.source_voltage_le.setDisabled(True)
        self.source_voltage_le.setText("%.1f" % 0)

        self.grid.addWidget(self.source_voltage_label, 1, 0)
        self.grid.addWidget(self.source_voltage_le, 1, 1)

        # Current to field ratio (TPA)
        self.tpa_label = QLabel("Tesla per Amper")

        self.tpa_le = QLineEdit()
        self.tpa_le.setDisabled(True)
        self.tpa_le.setText("%.4f" % self.config["magnet_source"]["TPA"])

        self.grid.addWidget(self.tpa_label, 2, 0)
        self.grid.addWidget(self.tpa_le, 2, 1)

        # Source output field
        self.source_field_label = QLabel("Source output field [T]")

        self.source_field_le = QLineEdit()
        self.source_field_le.setDisabled(True)
        self.source_field_le.setText("%.3f" % 0)

        self.grid.addWidget(self.source_field_label, 0, 2)
        self.grid.addWidget(self.source_field_le, 0, 3)

        # Shunt field
        self.shunt_label = QLabel("Shunt field [T]")

        self.shunt_le = QLineEdit()
        self.shunt_le.setDisabled(True)
        self.shunt_le.setText("%.3f" % 0)

        self.grid.addWidget(self.shunt_label, 1, 2)
        self.grid.addWidget(self.shunt_le, 1, 3)

        # Hall sensor field
        self.hall_sensor_label = QLabel("Hall sensor field [T]")

        self.hall_sensor_le = QLineEdit()
        self.hall_sensor_le.setDisabled(True)
        self.hall_sensor_le.setText("%.3f" % 0)

        self.grid.addWidget(self.hall_sensor_label, 2, 2)
        self.grid.addWidget(self.hall_sensor_le, 2, 3)

        # He-level sensor
        self.helium_level_label = QLabel("Helium level [mm]")

        self.helium_level_le = QLineEdit()
        self.helium_level_le.setDisabled(True)
        self.helium_level_le.setText("%d" % 0)

        self.helium_level_pb = QPushButton("Update helium level")

        self.grid.addWidget(self.helium_level_label, 3, 0)
        self.grid.addWidget(self.helium_level_le, 3, 1)
        self.grid.addWidget(self.helium_level_pb, 3, 2, 1, 2)