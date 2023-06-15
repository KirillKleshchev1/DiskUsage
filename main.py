from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
import sys
import argparse
from diskSpaceLogic import DiskSpaceLogic


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', type=str, help='Путь')
    return parser.parse_args()


class DiskSpaceWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Disk Space")
        self.setGeometry(100, 100, 300, 200)

        self.central_widget = QWidget(self)
        self.layout = QVBoxLayout(self.central_widget)

        self.progress_bar = QProgressBar(self)
        self.layout.addWidget(self.progress_bar)

        self.labels = {}

        for category in ["Documents", "Images", "Videos", "Music", "Archives"]:
            label = QLabel(self)
            self.layout.addWidget(label)
            self.labels[category] = label

        self.setCentralWidget(self.central_widget)

        self.logic = DiskSpaceLogic(arg_parser().path)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_disk_space)
        self.timer.start(1000)

    def update_disk_space(self):
        """
        Функция для подсчитывания веса файлов из разных категорий.
        Обновляется каждые 100 секунд.
        """
        total, usage = self.logic.get_disk_usage()
        for category, size in usage.items():
            self.labels[category].setText(f"{category}: {size / (1024 * 1024):.2f} MB")
        free_space = total - sum(usage.values())
        free_space_percent = free_space / total * 100
        self.progress_bar.setValue(int(free_space_percent))
        self.timer.start(100000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DiskSpaceWidget()
    window.show()
    sys.exit(app.exec_())
