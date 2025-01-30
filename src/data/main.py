import sys
import os
import matplotlib.pyplot as plt

# Add the gui directory to sys.path
current_directory = os.path.dirname(os.path.abspath(__file__))
gui_directory = os.path.abspath(os.path.join(current_directory, "../gui"))
sys.path.append(gui_directory)

import gui as g
import data_ingestion as di
import transform as t

def main():
    # Process data
    di.process_raw_data()
    ol_df = t.process_o_line_query().get_dataframe()
    rb_df = t.process_rb_roe_query().get_dataframe()

    # Create scatter plot
    plt.figure(figsize=(35, 26))  # Adjust figure size for better visibility
    plt.scatter(rb_df['player_display_name'], rb_df['rush_over_exp_pg'], label='Yards Over Expected Per Carry', color='blue', marker='o')
    plt.scatter(rb_df['player_display_name'], rb_df['efficiency'], label='Efficiency Rating', color='red', marker='s')

    # Annotate each dot with its corresponding value
    for i in range(len(rb_df)):
        plt.text(rb_df['player_display_name'][i], rb_df['rush_over_exp_pg'][i], 
                f"{rb_df['rush_over_exp_pg'][i]:.2f}", fontsize=10, ha='right', va='bottom', color='blue')
        
        plt.text(rb_df['player_display_name'][i], rb_df['efficiency'][i], 
                f"{rb_df['efficiency'][i]:.2f}", fontsize=10, ha='right', va='top', color='red')

    # Customize graph
    plt.title("Running Back 2024 Efficiency & Yards Over Expected Per Carry")
    plt.xlabel("Player")
    plt.ylabel("Value")
    plt.legend()
    plt.xticks(rotation=45, ha='right')  # Rotate player names for readability
    plt.grid(True)

    # Show initial dialog
    if g.welcome_dialog.exec_() == g.QDialog.Accepted:
        g.main_window.exec_()
        plt.show()


# Run the program
if __name__ == "__main__":
    main()

    