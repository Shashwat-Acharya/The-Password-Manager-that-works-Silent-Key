from PyQt6.QtWidgets import QApplication, QDialog, QMenu
import sys

app = QApplication(sys.argv)

window = QDialog()
window.setWindowTitle("SilentKey")





if __name__ == "__main__":
    window.show()
    sys.exit(app.exec())