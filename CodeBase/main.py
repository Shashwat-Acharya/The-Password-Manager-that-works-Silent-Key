# Import necessary modules from PyQt6 and Python's sys

from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QWidget
from PyQt6.QtGui import QIcon
import sys

class Welcome_Window(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle("Silent Key")

        # Set the window icon
        self.setWindowIcon(QIcon("GraphicLayout/Icon.ico"))

        # Create a label widget
        label = QLabel(self)
        label.setStyleSheet("font-size: 20px; font-weight: bold; color: blue;")
        label.setText("Welcome to Silent Key")

        # Set the position and size of the label
        label.setGeometry(100, 100, 200, 50)


# Entry point of the script
if __name__ == "__main__":
    # Create an instance of QApplication
    app = QApplication(sys.argv)

    # Create an instance of the Welcome_Window
    window = Welcome_Window()

    # Show the window
    window.show()

    # Execute the application.
    sys.exit(app.exec())
