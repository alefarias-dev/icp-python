import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QFrame, QSplitter, QPushButton, QTextEdit, QLabel, \
    QGridLayout


class ICPSimulatorInterface(QWidget):

    def __init__(self):
        super().__init__()
        hbox = QHBoxLayout(self)
        left = QFrame(self)
        left.setFrameShape(QFrame.StyledPanel)
        right = QFrame(self)
        right.setFrameShape(QFrame.StyledPanel)

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(left)
        splitter.addWidget(right)

        self.log_label = QLabel()
        self.log_label.setText("Log de operações")
        self.log_label.setAlignment(Qt.AlignCenter)
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.right_layout = QGridLayout(right)
        self.right_layout.addWidget(self.log_label)
        self.right_layout.addWidget(self.text_edit)

        # left buttons
        self.status_title_label = QLabel()
        self.status_title_label.setText("Status dos dispositivos")
        self.status_title_label.setAlignment(Qt.AlignCenter)
        self.status_title_label.setStyleSheet('color: red')
        self.left_layout = QGridLayout(left)
        self.left_layout.addWidget(self.status_title_label)
    
        hbox.addWidget(splitter)
        self.setLayout(hbox)
        self.resize(800, 500)
        self.setWindowTitle('QSplitter')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    interface = ICPSimulatorInterface()
    sys.exit(app.exec_())
