"""
This script creates a simple PyQt6 application with a dialog window.

The application demonstrates the basic structure of a PyQt6-based GUI:
- Initializes a QApplication instance.
- Creates a QDialog window with a title ("SilentKey").
- Optionally allows for setting a custom icon for the window (commented out).
- Uses an entry point to ensure proper execution of the application event loop.

Dependencies:
- PyQt6: Required for GUI components such as QApplication, QDialog, and QIcon.
- sys: For handling command-line arguments and exiting the application.

To run:
- Execute the script directly (`python script_name.py`).
- The dialog window will appear with the title "SilentKey."

To customize:
- Replace the commented-out line for `setWindowIcon` with the path to a valid `.ico` file.
"""

# Import necessary modules from PyQt6 and Python's sys library
from PyQt6.QtWidgets import QApplication, QDialog  # Import QApplication for app control and QDialog for the dialog window
from PyQt6.QtGui import QIcon  # Import QIcon to set custom window icons
import sys  # Import sys to handle command-line arguments and system-specific parameters

# Create an instance of the QApplication
# QApplication is the main application handler for GUI-based PyQt6 programs
app = QApplication(sys.argv)

# Create an instance of QDialog
# QDialog is a simple dialog-based window, suitable for single-use tasks
window = QDialog()

# Set the title of the dialog window
window.setWindowTitle("SilentKey")

# Optionally, set the window icon (uncomment and replace the path to use)
# The QIcon class is used to set custom icons for the application or window
# Ensure that the icon file path is correct and accessible
window.setWindowIcon(QIcon("GraphicLayout/icon.webp"))


# Entry point of the script
if __name__ == "__main__":
    # Display the dialog window
    window.show()

    # Execute the application event loop
    # sys.exit ensures the program exits cleanly when the GUI is closed
    sys.exit(app.exec())
