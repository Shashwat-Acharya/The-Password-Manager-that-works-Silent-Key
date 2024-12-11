from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit,
    QTableWidget, QTableWidgetItem, QHeaderView, QListWidget
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class PasswordManagerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Manager")
        self.setFixedSize(1024, 768)  # Disable resizing

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        
        self.setup_ui()

    def setup_ui(self):
        # Main layout
        main_layout = QVBoxLayout()
        self.main_widget.setLayout(main_layout)

        # Header
        header = QLabel("Password Manager Dashboard")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        header.setStyleSheet("color: teal;")
        main_layout.addWidget(header)

        # Search Bar
        search_layout = QHBoxLayout()
        search_input = QLineEdit()
        search_input.setPlaceholderText("Search passwords...")
        search_input.setStyleSheet("padding: 5px; font-size: 14px;")
        search_button = QPushButton("Search")
        search_button.setStyleSheet("background-color: teal; color: white; padding: 5px 10px;")
        search_layout.addWidget(search_input)
        search_layout.addWidget(search_button)
        main_layout.addLayout(search_layout)

        # Sidebar and Table layout
        content_layout = QHBoxLayout()

        # Sidebar
        sidebar = QListWidget()
        sidebar.addItems(["Favorites", "Recently Modified", "Shared with Me", "Expired"])
        sidebar.setStyleSheet("background-color: #f5f5f5; font-size: 14px;")
        content_layout.addWidget(sidebar)

        # Password Table
        self.table = QTableWidget()
        self.table.setRowCount(10)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Name", "Username", "Password", "URI"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setStyleSheet("background-color: #ffffff; font-size: 14px;")
        content_layout.addWidget(self.table)

        main_layout.addLayout(content_layout)

        # Footer with Theme Switching
        footer_layout = QHBoxLayout()
        light_theme_btn = QPushButton("Light Theme")
        dark_theme_btn = QPushButton("Dark Theme")
        neon_theme_btn = QPushButton("Neon Teal Theme")

        light_theme_btn.clicked.connect(lambda: self.apply_theme("light"))
        dark_theme_btn.clicked.connect(lambda: self.apply_theme("dark"))
        neon_theme_btn.clicked.connect(lambda: self.apply_theme("neon"))

        for btn in [light_theme_btn, dark_theme_btn, neon_theme_btn]:
            btn.setStyleSheet("padding: 5px 10px; font-size: 14px;")
            footer_layout.addWidget(btn)

        main_layout.addLayout(footer_layout)

    def apply_theme(self, theme):
        if theme == "light":
            self.setStyleSheet("background-color: #ffffff; color: #000000;")
        elif theme == "dark":
            self.setStyleSheet("background-color: #2c2c2c; color: #ffffff;")
        elif theme == "neon":
            self.setStyleSheet("background-color: #001f3f; color: #39ff14;")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = PasswordManagerApp()
    window.show()
    sys.exit(app.exec())
