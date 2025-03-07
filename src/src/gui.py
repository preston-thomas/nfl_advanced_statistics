import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QApplication, QPushButton, QMainWindow, QDialog, QHBoxLayout
from PyQt5.QtCore import Qt
import data_ingestion as di
import transform as t

class MatplotlibCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MatplotlibCanvas, self).__init__(self.fig)

class PlotWindow(QDialog):
    def __init__(self, parent=None):
        super(PlotWindow, self).__init__(parent)
        self.setWindowTitle("Running Back Stats")
        # Make the window larger to accommodate the plot
        self.setMinimumSize(1200, 800)
        
        # Main layout
        layout = QVBoxLayout()
        
        # Create the plot canvas
        self.canvas = MatplotlibCanvas(self, width=12, height=8)
        layout.addWidget(self.canvas)
        
        # Button layout
        button_layout = QHBoxLayout()
        # Back button to return to main window
        back_button = QPushButton("Back to Main Menu")
        back_button.clicked.connect(self.accept)  # Will close this dialog and return to previous
        button_layout.addWidget(back_button)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
        
        # Generate and display the plot
        self.plot_rb_data()
    
    def plot_rb_data(self):
        # Process data
        di.process_raw_data()
        rb_df = t.process_rb_roe_query().get_dataframe()

        # Create custom x-axis labels
        rb_df["player_label"] = rb_df["player_display_name"] + " (" + rb_df["team_abbr"] + ")"

        # Clear the axes for fresh plotting
        self.canvas.axes.clear()
        
        # Create scatter plot
        self.canvas.axes.scatter(rb_df['player_label'], rb_df['rush_over_exp_pg'], 
                                 label='Yards Over Expected Per Carry', color='blue', marker='o')
        self.canvas.axes.scatter(rb_df['player_label'], rb_df['efficiency'], 
                                 label='Efficiency Rating', color='red', marker='s')

        # Annotate each dot with its corresponding value
        for i in range(len(rb_df)):
            self.canvas.axes.text(i, rb_df['rush_over_exp_pg'].iloc[i], 
                      f"{rb_df['rush_over_exp_pg'].iloc[i]:.2f}", 
                      fontsize=8, ha='right', va='top', color='blue')
            
            self.canvas.axes.text(i, rb_df['efficiency'].iloc[i], 
                      f"{rb_df['efficiency'].iloc[i]:.2f}", 
                      fontsize=10, ha='left', va='bottom', color='red')

        # Customize graph
        self.canvas.axes.set_title("Running Back 2024 Efficiency & Yards Over Expected Per Carry")
        self.canvas.axes.set_xlabel("Player (Team)")
        self.canvas.axes.set_ylabel("Value")
        self.canvas.axes.legend()
        self.canvas.axes.set_xticks(range(len(rb_df)))
        self.canvas.axes.set_xticklabels(rb_df["player_label"], rotation=45, ha='right')
        self.canvas.axes.grid(True)
        
        # Adjust layout
        self.canvas.fig.tight_layout()
        
        # Refresh canvas
        self.canvas.draw()

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("2024 NFL Performance Evaluator")
        
        layout = QVBoxLayout()
        
        label = QLabel("The 2024 season flew by... sigh... let's explore some stats! (more coming soon!)")
        layout.addWidget(label)
        
        # Exit button
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.close)
        layout.addWidget(exit_button, 0, alignment=Qt.AlignRight)

        # Running Backs button
        rb_button = QPushButton("Running Backs")
        rb_button.clicked.connect(self.show_rb_plot)
        layout.addWidget(rb_button, 0, alignment=Qt.AlignLeft)
        
        self.setLayout(layout)
    
    def show_rb_plot(self):
        # Hide the main window while showing the plot
        self.hide()
        
        # Show the plot window
        plot_window = PlotWindow(self)
        result = plot_window.exec_()
        if result == QDialog.Accepted:
            new_main_window = MainWindow()
            new_main_window.exec_()
        
        # After plot window is closed, show main window again
        # self.show()

# Application Execution
def run_app():
    app = QApplication(sys.argv)
    
    # Create the welcome dialog
    welcome_dialog = WelcomeDialog()
    
    # If welcome dialog is accepted, show main window
    if welcome_dialog.exec_() == QDialog.Accepted:
        main_window = MainWindow()
        main_window.exec_()

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