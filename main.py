import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar
from PyQt5.QtCore import QTimer
from diskSpaceLogic import DiskSpaceLogic


class DiskSpaceWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Disk Space")
        self.setGeometry(100, 100, 300, 100)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(10, 10, 280, 80)

        self.logic = DiskSpaceLogic('/')

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_disk_space)
        self.timer.start(1000)

    def update_disk_space(self):
        total, used, free = self.logic.get_disk_usage()
        free_space_percent = free / total * 100
        self.progress_bar.setValue(int(free_space_percent))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DiskSpaceWidget()
    window.show()
    sys.exit(app.exec_())
