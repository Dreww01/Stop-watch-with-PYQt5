from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from stopwatch import StopwatchLogic

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.logic = StopwatchLogic()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Stopwatch")

        self.time_label = QLabel("00:00:00:00", self)
        self.time_label.setAlignment(Qt.AlignCenter)

        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")
        self.reset_button = QPushButton("Reset")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e2f;
                font-family: 'Poppins', sans-serif;
                color: #00ffd5;
            }
            QLabel {
                font-size: 48px;
                font-weight: bold;
                qproperty-alignment: AlignCenter;
            }
            QPushButton {
                background-color: #00ffd5;
                color: #1e1e2f;
                font-size: 18px;
                font-weight: bold;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #00bfa3;
            }
        """)

        # Connect buttons
        self.start_button.clicked.connect(self.start_stopwatch)
        self.stop_button.clicked.connect(self.stop_stopwatch)
        self.reset_button.clicked.connect(self.reset_stopwatch)
        self.logic.timer.timeout.connect(self.update_display)

    def start_stopwatch(self):
        self.logic.timer.start()

    def stop_stopwatch(self):
        self.logic.timer.stop()

    def reset_stopwatch(self):
        self.logic.timer.stop()
        self.logic.reset_time()
        self.time_label.setText("00:00:00:00")

    def update_display(self):
        self.logic.update_time()
        self.time_label.setText(self.logic.get_formatted_time())
