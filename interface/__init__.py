import json
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QFrame, QSplitter, QLabel, \
    QGridLayout, QTextBrowser, QTextEdit, QPlainTextEdit

from simulation.Simulator import ICPSimulator


class ICPSimulatorInterface(QWidget):

    def __init__(self):
        super().__init__()
        # interface code
        self.status_title_label = QLabel()
        self.log_label = QLabel()
        self.textedit_log = QTextBrowser(self)
        self.devices_status_log = QPlainTextEdit()
        self.textedit_log.ensureCursorVisible()
        self.left = QFrame(self)
        self.right = QFrame(self)
        self.splitter = QSplitter(Qt.Horizontal)
        self.right_layout = QGridLayout(self.right)
        self.left_layout = QGridLayout(self.left)
        self.setWindowTitle("Visual Simulation of ICP")
        self.resize(800, 500)
        self.load_ui()
        self.show()

        # simulator code
        self.simulator = ICPSimulator(self)
        self.devices_status = None

    def make_splitter(self):
        self.left.setFrameShape(QFrame.StyledPanel)
        self.right.setFrameShape(QFrame.StyledPanel)
        self.splitter.addWidget(self.left)
        self.splitter.addWidget(self.right)

    def add_widget(self, layout, widget):
        layout.addWidget(widget)

    def load_ui(self):
        hbox = QHBoxLayout(self)
        self.make_splitter()
        self.log_label.setText("Log de operações")
        self.log_label.setAlignment(Qt.AlignCenter)
        self.add_widget(self.right_layout, self.log_label)
        self.add_widget(self.right_layout, self.textedit_log)
        self.add_widget(self.left_layout, self.devices_status_log)
        self.status_title_label.setText("Status dos dispositivos")
        self.status_title_label.setAlignment(Qt.AlignCenter)
        self.status_title_label.setStyleSheet('color: red')
        self.left_layout.addWidget(self.status_title_label)
        self.add_widget(hbox, self.splitter)
        self.setLayout(hbox)

    def read_log(self):
        with open('log', 'r') as log_file:
            return log_file.read()

    def initialize(self):
        self.simulator.start()

    def update_log_text(self):
        self.textedit_log.insertPlainText("\n" + "\n".join(self.read_log().split("\n")[-10:-1]))
        self.textedit_log.setReadOnly(True)
        self.textedit_log.ensureCursorVisible()

    def update_devices_status(self):
        with open('devices_status', 'r') as devices_status:
            self.devices_status = json.loads(devices_status.read())
        devices_string = ""
        for device, status in self.devices_status.items():
            status = "ONLINE" if status == 1 else "OFFLINE"
            devices_string += f"{device} [{status}]\n"
        self.devices_status_log.setPlainText("")
        self.devices_status_log.insertPlainText(devices_string)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    interface = ICPSimulatorInterface()
    interface.initialize()
    sys.exit(app.exec_())
