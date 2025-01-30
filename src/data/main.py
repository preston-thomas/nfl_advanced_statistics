import sys
import os
import pandasgui as pdg

# Add the gui directory to sys.path
current_directory = os.path.dirname(os.path.abspath(__file__))
gui_directory = os.path.abspath(os.path.join(current_directory, "../gui"))
sys.path.append(gui_directory)

import gui as g
import data_ingestion as di
import transform as t

# Run the program
if __name__ == "__main__":
    di.process_raw_data()
    t.process_o_line_query()
    t.process_rb_roe_query()
    # Show initial dialog
    if g.welcome_dialog.exec_() == g.QDialog.Accepted:
        g.main_window.exec_()
        # TODO: fix GUI
        pdg.show(t.process_rb_roe_query().get_dataframe())

    