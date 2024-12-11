import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMovie  # Import QMovie for GIF animation
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("SILENT | Key")
        self.setGeometry(100, 100, 800, 600)  # x, y, width, height
        self.setWindowIcon(QIcon("C:/Users/srmus/Downloads/icons8-cryptography-100.png"))


        # Set the window flags to disable maximize
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.MSWindowsFixedSizeDialogHint)

        # Main widget to hold everything
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # Set a vertical layout
        main_layout = QVBoxLayout()

        # Create a horizontal layout for search bar alignment
        search_layout = QHBoxLayout()
        search_layout.setContentsMargins(300, 30, 300, 0)  # Adjust top margins to push it a bit down

        # Initialize the animated search GIF
        self.search_gif_label = QLabel(self)  # Create QLabel for GIF
        self.search_gif_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Load the animated search GIF with QMovie
        self.search_movie = QMovie("C:/Users/srmus/Downloads/icons8-loading-infinity.gif")  # Path to your GIF
        self.search_gif_label.setMovie(self.search_movie)
        self.search_movie.start()  # Start the GIF animation

        # Create the search bar
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Type to search...")
        self.search_bar.setStyleSheet("font-size: 16px; padding: 10px; color: aqua;")

        # Add the animated search GIF and search bar into the search layout
        search_layout.addWidget(self.search_gif_label)  # Add the animated GIF
        search_layout.addWidget(self.search_bar)  # Add the search bar

        # Add the search bar layout to the main vertical layout
        main_layout.addLayout(search_layout)

        # Add a simple label in the center
        self.label = QLabel("BHAI NE BOLA KARNE KA TOH KARNE KA", self)
        self.label.setStyleSheet("font-size: 30px; color: aqua; text-align: center;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.label)

        # Set the layout to the main widget
        main_widget.setLayout(main_layout)

        # Fix window size
        self.setFixedSize(1200, 700)


if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)

    # Create the main window
    window = MainWindow()
    window.show()

    # Execute the application
    sys.exit(app.exec())