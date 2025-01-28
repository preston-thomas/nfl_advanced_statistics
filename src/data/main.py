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
    