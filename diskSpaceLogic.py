import shutil


class DiskSpaceLogic:
    def __init__(self, path: str):
        self.path = path

    def get_disk_usage(self) -> tuple:
        usage = shutil.disk_usage(self.path)
        print(usage)
        total, used, free = usage.total, usage.used, usage.free
        return total, used, free
