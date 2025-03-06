import sys
import os
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QApplication, QPushButton, QMainWindow, QDialog
from PyQt5.QtCore import Qt
current_directory = os.path.dirname(os.path.abspath(__file__))
data_directory = os.path.abspath(os.path.join(current_directory, "../main"))
sys.path.append(data_directory)
import main as m

# NOTE: Add buttons that will then open a pandasgui window when clicked (invoked by calling show() on a dataframe)

class WelcomeDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("2024 NFL Performance Evaluator")
        
        layout = QVBoxLayout()
        
        label = QLabel("Welcome to the 2024 NFL Performance Evaluator!")
        layout.addWidget(label)
        
        button = QPushButton("Explore...")
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
        
        back_button.clicked.connect(self.close)  # Close current dialog when clicked
        layout.addWidget(back_button, 0, Qt.AlignRight)  # Position button in bottom-right

        rb_button.clicked.connect(m.rb_processing)
        layout.addWidget(rb_button, 0, Qt.AlignLeft)
        self.setLayout(layout)

# Application Execution
app = QApplication(sys.argv)
# Define buttons to allow calls in main
back_button = QPushButton("Exit")
rb_button = QPushButton("Running Backs")

# Create the windows only once
welcome_dialog = WelcomeDialog()
main_window = MainWindow()

def show_welcome():
    welcome_dialog.exec_()

def new_main_window():
    new_main_window = MainWindow()
    return new_main_window