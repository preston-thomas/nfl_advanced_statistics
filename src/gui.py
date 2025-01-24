import sys
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QApplication, QPushButton, QMainWindow


class WelcomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("2024 NFL Performance Evaluator")

        # Button initialization
        button = QPushButton("Click here to explore...")
        button.clicked.connect(self.open_main_screen)
        button.setGeometry(50, 50, 200, 50)

    def open_main_screen(self):
        self.main_screen = MainWindow()
        self.main_screen.show()
        self.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("2024 NFL Performance Evaluator")

        layout = QVBoxLayout()
        label = QLabel("The 2024 season flew by... sigh... let's explore some stats!")
        layout.addWidget(label)

        # Back button initialization
        back_button = QPushButton("Welcome Screen")
        back_button.clicked.connect(self.go_back)
        layout.addWidget(back_button)

        # Container initilization
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def go_back(self):
        self.welcome_screen = WelcomeWindow()
        self.welcome_screen.show()
        self.close()

# Application Execution
app = QApplication(sys.argv)
welcome_screen = WelcomeWindow()
welcome_screen.show()
sys.exit(app.exec())

