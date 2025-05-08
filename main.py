import sys
from PyQt5.QtWidgets import QApplication
from gui import StopWatch

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StopWatch()
    window.show()
    sys.exit(app.exec_())