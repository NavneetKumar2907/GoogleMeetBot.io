import sys
from PySide6.QtCore import QLine
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog)
from Meet import *

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        self.Email = QLineEdit("Enter Email ID")
        self.Passw = QLineEdit("Password")
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
        Meet(self.Email.text(), self.Passw.text(), self.Url.text()).Join()

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())