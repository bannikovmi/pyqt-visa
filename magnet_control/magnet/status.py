# pyqt-related imports
from PyQt5.QtWidgets import QGridLayout, QGroupBox, QTextEdit

class QSourceStatusWidget(QGroupBox):

    def __init__(self, config, data, label = "Source status"):

        super().__init__(label)
        self.config = config
        self.data = data
        self.initUI()

    def initUI(self):
        
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        # Status textedit
        self.status_te = QTextEdit()
        self.status_te.setDisabled(True)
        
        self.grid.addWidget(self.status_te, 0, 0)