from PyQt5.QtCore import QTime, QTimer

class StopwatchLogic:
    def __init__(self):
        self.time = QTime(0, 0, 0, 0)
        self.timer = QTimer()
        self.timer.setInterval(10)  # 10ms update

    def reset_time(self):
        self.time = QTime(0, 0, 0, 0)

    def update_time(self):
        self.time = self.time.addMSecs(10)

    def get_formatted_time(self):
        hours = self.time.hour()
        minutes = self.time.minute()
        seconds = self.time.second()
        milliseconds = self.time.msec() // 10
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}:{milliseconds:01d}"
