import unittest
from unittest.mock import MagicMock
from PyQt5.QtWidgets import QApplication
from diskSpaceLogic import DiskSpaceLogic
from main import DiskSpaceWidget
import shutil
import os


class TestDiskSpaceLogic(unittest.TestCase):
    def test_get_disk_usage(self):
        logic = DiskSpaceLogic('')
        shutil.disk_usage = MagicMock(return_value=(1000000000, 500000000, 500000000))
        logic.file_types = {"Documents": ['.docx', '.pdf', '.txt']}
        os.walk = MagicMock(return_value=[('/', [], ['file.docx'])])
        os.path.getsize = MagicMock(return_value=100000000)
        total, usage = logic.get_disk_usage()
        self.assertEqual(total, 1000000000)
        self.assertEqual(usage['Documents'], 100000000)


class TestDiskSpaceWidget(unittest.TestCase):
    def test_update_disk_space(self):
        _ = QApplication([])
        window = DiskSpaceWidget()
        window.logic.get_disk_usage = MagicMock(return_value=(1000000000, {"Documents": 500000000}))
        window.update_disk_space()
        expected_value = 50
        self.assertEqual(window.progress_bar.value(), expected_value)
        expected_text = "Documents: 476.84 MB"
        self.assertEqual(window.labels["Documents"].text(), expected_text)


if __name__ == '__main__':
    unittest.main()
