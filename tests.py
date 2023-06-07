import unittest
from unittest.mock import MagicMock, Mock
from PyQt5.QtWidgets import QApplication
from main import DiskSpaceWidget
from diskSpaceLogic import DiskSpaceLogic
import shutil


class TestDiskSpaceLogic(unittest.TestCase):
    def test_get_disk_usage(self):
        logic = DiskSpaceLogic('/')
        shutil.disk_usage = MagicMock(return_value=(1000000000, 500000000, 500000000))
        disk_usage_mock = Mock()
        disk_usage_mock.total = 1000000000
        disk_usage_mock.used = 500000000
        disk_usage_mock.free = 500000000
        shutil.disk_usage = MagicMock(return_value=disk_usage_mock)
        total, used, free = logic.get_disk_usage()
        self.assertEqual(total, 1000000000)
        self.assertEqual(used, 500000000)
        self.assertEqual(free, 500000000)


class TestDiskSpaceWidget(unittest.TestCase):
    def test_update_disk_space(self):
        _ = QApplication([])
        window = DiskSpaceWidget()
        window.logic.get_disk_usage = MagicMock(return_value=(1000000000, 500000000, 500000000))
        window.update_disk_space()
        expected_value = int(500000000 / 1000000000 * 100)
        self.assertEqual(window.progress_bar.value(), expected_value)


if __name__ == '__main__':
    unittest.main()
