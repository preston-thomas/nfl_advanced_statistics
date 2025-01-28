import sys
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QApplication, QPushButton, QMainWindow, QDialog
from PyQt5.QtCore import Qt


class WelcomeDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("2024 NFL Performance Evaluator")
        
        layout = QVBoxLayout()
        
        label = QLabel("Welcome to the 2024 NFL Performance Evaluator!")
        layout.addWidget(label)
        
        button = QPushButton("Click here to explore...")
        button.clicked.connect(self.accept)  # Close dialog and return accepted
        layout.addWidget(button)
        
        self.setLayout(layout)

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("2024 NFL Performance Evaluator")
        
        layout = QVBoxLayout()
        
        label = QLabel("The 2024 season flew by... sigh... let's explore some stats! (more coming soon!)")
        layout.addWidget(label)
        
        back_button = QPushButton("Exit Program")
        back_button.clicked.connect(self.close)  # Close current dialog
        layout.addWidget(back_button, 0, Qt.AlignRight)  # Position button in bottom-right
        
        self.setLayout(layout)

# Application Execution
app = QApplication(sys.argv)

# Create the windows only once
welcome_dialog = WelcomeDialog()
main_window = MainWindow()

def show_welcome():
    welcome_dialog.exec_()