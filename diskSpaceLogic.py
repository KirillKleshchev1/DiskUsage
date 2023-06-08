import shutil


class DiskSpaceLogic:
    def __init__(self, path: str):
        self.path = path

    """
    Функция для получения информации о диске.
    Возвращает кортеж, содержащий размер диска, используемое место на диске, свободное место на диске
    """
    def get_disk_usage(self) -> tuple:
        usage = shutil.disk_usage(self.path)
        print(usage)
        total, used, free = usage.total, usage.used, usage.free
        return total, used, free
