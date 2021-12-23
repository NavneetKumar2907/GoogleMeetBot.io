from PySide6 import QtGui
from Meet import *
import sys
from PySide6.QtCore import QLine
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog)


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets

        # Email
        self.Email = QLineEdit("Enter Email ID")
       
        
        # Password
        self.Passw = QLineEdit("Password")
        self.Passw.setEchoMode(QLineEdit.Password)

        # Url
        self.Url = QLineEdit("Meet URL")


        self.button = QPushButton("Submit")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.Email)
        layout.addWidget(self.Passw)
        layout.addWidget(self.Url)
        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)

    # Greets the user
    def greetings(self):

        if self.Email.text() and self.Passw.text() and self.Url.text():
            Meet(self.Email.text(), self.Passw.text(), self.Url.text()).Join()
