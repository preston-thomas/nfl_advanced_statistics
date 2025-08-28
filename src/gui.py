import sys
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
    def __init__(self, parent=None, stat_type="rb"):
        super(PlotWindow, self).__init__(parent)
        self.stat_type = stat_type
        self.setWindowTitle(f"{stat_type.upper()} Stats")
        self.setMinimumSize(1200, 800)
        
        # Main layout
        layout = QVBoxLayout()
        
        # Create the plot canvas
        self.canvas = MatplotlibCanvas(self, width=12, height=8)
        layout.addWidget(self.canvas)
        
        # Button layout
        button_layout = QHBoxLayout()
        back_button = QPushButton("Back to Main Menu")
        back_button.clicked.connect(self.accept)
        button_layout.addWidget(back_button)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
        
        # Generate and display the plot
        if self.stat_type == "rb":
            self.plot_rb_data()
        elif self.stat_type == "wr":
            self.plot_wr_data()
        elif self.stat_type == "qb":
            self.plot_qb_data()
        elif self.stat_type == "oline":
            self.plot_oline_data()
    
    def plot_rb_data(self):
        di.process_raw_data()
        rb_df = t.process_rb_roe_query().get_dataframe()
        rb_df["player_label"] = rb_df["player_display_name"] + " (" + rb_df["team_abbr"] + ")"
        self.canvas.axes.clear()
        
        self.canvas.axes.scatter(rb_df['player_label'], rb_df['rush_over_exp_pg'], 
                                label='Yards Over Expected Per Carry', color='blue', marker='o')
        self.canvas.axes.scatter(rb_df['player_label'], rb_df['efficiency'], 
                                label='Efficiency Rating', color='red', marker='s')

        for i in range(len(rb_df)):
            self.canvas.axes.text(i, rb_df['rush_over_exp_pg'].iloc[i], 
                                 f"{rb_df['rush_over_exp_pg'].iloc[i]:.2f}", 
                                 fontsize=8, ha='right', va='top', color='blue')
            self.canvas.axes.text(i, rb_df['efficiency'].iloc[i], 
                                 f"{rb_df['efficiency'].iloc[i]:.2f}", 
                                 fontsize=10, ha='left', va='bottom', color='red')

        self.canvas.axes.set_title("Running Back 2024 Efficiency & Yards Over Expected Per Carry")
        self.canvas.axes.set_xlabel("Player (Team)")
        self.canvas.axes.set_ylabel("Value")
        self.canvas.axes.legend()
        self.canvas.axes.set_xticks(range(len(rb_df)))
        self.canvas.axes.set_xticklabels(rb_df["player_label"], rotation=45, ha='right')
        self.canvas.axes.grid(True)
        self.canvas.fig.tight_layout()
        self.canvas.draw()

    def plot_wr_data(self):
        di.process_raw_data()
        wr_df = t.process_wr_query().get_dataframe()
        # Filter to top WR per team based on avg_yac_above_expectation
        wr_df = wr_df.loc[wr_df.groupby('team_abbr')['avg_yac_above_expectation'].idxmax()]
        wr_df = wr_df.sort_values('avg_yac_above_expectation', ascending=False).reset_index(drop=True)
        wr_df["player_label"] = wr_df["player_display_name"] + " (" + wr_df["team_abbr"] + ")"
        self.canvas.axes.clear()
        
        self.canvas.axes.scatter(wr_df['player_label'], wr_df['avg_yac_above_expectation'], 
                                label='YAC Over Expected Per Reception', color='blue', marker='o')
        self.canvas.axes.scatter(wr_df['player_label'], wr_df['catch_percentage'], 
                                label='Catch Percentage', color='red', marker='s')

        for i in range(len(wr_df)):
            self.canvas.axes.text(i, wr_df['avg_yac_above_expectation'].iloc[i], 
                                 f"{wr_df['avg_yac_above_expectation'].iloc[i]:.2f}", 
                                 fontsize=8, ha='right', va='top', color='blue')
            self.canvas.axes.text(i, wr_df['catch_percentage'].iloc[i], 
                                 f"{wr_df['catch_percentage'].iloc[i]:.2f}", 
                                 fontsize=10, ha='left', va='bottom', color='red')

        self.canvas.axes.set_title("Top Wide Receiver Per Team: 2024 Catch Percentage & YAC Over Expected Per Reception")
        self.canvas.axes.set_xlabel("Player (Team)")
        self.canvas.axes.set_ylabel("Value")
        self.canvas.axes.legend()
        self.canvas.axes.set_xticks(range(len(wr_df)))
        self.canvas.axes.set_xticklabels(wr_df["player_label"], rotation=90, ha='center')
        self.canvas.axes.grid(True)
        self.canvas.fig.tight_layout()
        self.canvas.draw()

    def plot_qb_data(self):
        di.process_raw_data()
        qb_df = t.process_qb_query().get_dataframe()
        qb_df["player_label"] = qb_df["player_display_name"] + " (" + qb_df["team_abbr"] + ")"
        self.canvas.axes.clear()
        
        self.canvas.axes.scatter(qb_df['player_label'], qb_df['completion_percentage_above_expectation'], 
                                label='Completion % Over Expected', color='blue', marker='o')
        self.canvas.axes.scatter(qb_df['player_label'], qb_df['aggressiveness'], 
                                label='Aggressiveness', color='red', marker='s')

        for i in range(len(qb_df)):
            self.canvas.axes.text(i, qb_df['completion_percentage_above_expectation'].iloc[i], 
                                 f"{qb_df['completion_percentage_above_expectation'].iloc[i]:.2f}", 
                                 fontsize=8, ha='right', va='top', color='blue')
            self.canvas.axes.text(i, qb_df['aggressiveness'].iloc[i], 
                                 f"{qb_df['aggressiveness'].iloc[i]:.2f}", 
                                 fontsize=10, ha='left', va='bottom', color='red')

        self.canvas.axes.set_title("Quarterback 2024 Aggressiveness & Completion % Over Expected")
        self.canvas.axes.set_xlabel("Player (Team)")
        self.canvas.axes.set_ylabel("Value")
        self.canvas.axes.legend()
        self.canvas.axes.set_xticks(range(len(qb_df)))
        self.canvas.axes.set_xticklabels(qb_df["player_label"], rotation=45, ha='right')
        self.canvas.axes.grid(True)
        self.canvas.fig.tight_layout()
        self.canvas.draw()

    def plot_oline_data(self):
        di.process_raw_data()
        oline_df = t.process_o_line_query().get_dataframe()
        self.canvas.axes.clear()
        
        self.canvas.axes.bar(range(len(oline_df)), oline_df['szn_rush_yds_before_contact_weighted_avg'], 
                            label='Yards Before Contact Per Carry', color='blue')

        for i in range(len(oline_df)):
            self.canvas.axes.text(i, oline_df['szn_rush_yds_before_contact_weighted_avg'].iloc[i], 
                                 f"{oline_df['szn_rush_yds_before_contact_weighted_avg'].iloc[i]:.2f}", 
                                 fontsize=8, ha='center', va='bottom', color='blue')

        self.canvas.axes.set_title("Offensive Line 2024 Yards Before Contact Per Carry")
        self.canvas.axes.set_xlabel("Team")
        self.canvas.axes.set_ylabel("Value")
        self.canvas.axes.legend()
        self.canvas.axes.set_xticks(range(len(oline_df)))
        self.canvas.axes.set_xticklabels(oline_df["team"], rotation=45, ha='right')
        self.canvas.axes.grid(True)
        self.canvas.fig.tight_layout()
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

        # Wide Receivers button
        wr_button = QPushButton("Wide Receivers")
        wr_button.clicked.connect(self.show_wr_plot)
        layout.addWidget(wr_button, 0, alignment=Qt.AlignLeft)

        # Quarterbacks button
        qb_button = QPushButton("Quarterbacks")
        qb_button.clicked.connect(self.show_qb_plot)
        layout.addWidget(qb_button, 0, alignment=Qt.AlignLeft)

        # Offensive Line button
        oline_button = QPushButton("Offensive Lines")
        oline_button.clicked.connect(self.show_oline_plot)
        layout.addWidget(oline_button, 0, alignment=Qt.AlignLeft)
        
        self.setLayout(layout)
    
    def show_rb_plot(self):
        self.hide()
        plot_window = PlotWindow(self, stat_type="rb")
        result = plot_window.exec_()
        if result == QDialog.Accepted:
            new_main_window = MainWindow()
            new_main_window.exec_()

    def show_wr_plot(self):
        self.hide()
        plot_window = PlotWindow(self, stat_type="wr")
        result = plot_window.exec_()
        if result == QDialog.Accepted:
            new_main_window = MainWindow()
            new_main_window.exec_()

    def show_qb_plot(self):
        self.hide()
        plot_window = PlotWindow(self, stat_type="qb")
        result = plot_window.exec_()
        if result == QDialog.Accepted:
            new_main_window = MainWindow()
            new_main_window.exec_()

    def show_oline_plot(self):
        self.hide()
        plot_window = PlotWindow(self, stat_type="oline")
        result = plot_window.exec_()
        if result == QDialog.Accepted:
            new_main_window = MainWindow()
            new_main_window.exec_()

def run_app():
    app = QApplication(sys.argv)
    welcome_dialog = WelcomeDialog()
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
        button.clicked.connect(self.accept)
        layout.addWidget(button)
        self.setLayout(layout)