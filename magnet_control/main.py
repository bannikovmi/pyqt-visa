#!/usr/bin/python

"""
This module contains a set of commands for communication with Thyracont VSP transducers
based on PyVISA library and custom data_packages module.

Author: Mikhail Bannikov bannikovmi96@gmail.com
"""

# standard library imports
import sys

# pyqt-related imports
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget

# local imports
from magnet.tab import QMagnetTab

# load configurations
import tomli
with open("config.toml", mode='rb') as config_file:
    config = tomli.load(config_file)

class MainWindow(QMainWindow):

    def __init__(self, config):
        
        super().__init__()

        self.config = config
        self.data = {
        }
        self.initUI()

    def initUI(self):

        # Create tab widgets
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.magnet_tab = QMagnetTab(self.config, self.data)
        self.tabs.addTab(self.magnet_tab, "Magnet")

        # Resize main window and set title
        self.setWindowTitle('21T_control')

        self.show()

def main():

    app = QApplication(sys.argv)
    window = MainWindow(config)

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
