import os
import shutil
from collections import defaultdict


class DiskSpaceLogic:
    def __init__(self, path):
        self.file_types = {
            "Documents": ['.docx', '.pdf', '.txt', '.rtf', '.cdd',
                          '.doc', '.docm', '.dot', 'dotm', '.dotx',
                          '.pages', '.sdf', '.wpd', '.xps', '.xltx',
                          '.xlt', '.xltm', '.xlsx', '.xls', '.xlr',
                          '.xlsb', 'xlsm', '.snb', '.pub', '.sldm'],
            "Images": ['.jpg', '.png', '.gif', '.jpeg', '.raw', '.tiff',
                       '.psd', '.bmp', '.jp2', '.did', '.tif'],
            "Videos": ['.mp4', '.mkv', '.flv', '.3g2', '.3gp'
                       '.3gp2', '.3gpp', '.asf', '.avi', '.drv',
                       '.dat', 'f4v', '.gtp', '.h264', '.m4v',
                       '.mov', '.mpg', '.mts', '.rmvb', '.rm',
                       '.swf', '.ts', '.vid', '.vob', '.webm'
                       '.wmv', '.yuv'],
            "Music": ['.mp3', '.wav', '.m4a', '.aif', '.aud',
                      '.iff', '.m3u', '.m4b', '.m4r', '.mid',
                      '.midi', '.mod', '.mpa', '.ogg', '.ram',
                      '.sib', '.wav'],
            "Archives": ['.zip', '.tar', '.rar', '.ace', '.arj',
                         '.jar', '.7z', '.cab', '.cbr', '.exe',
                         '.deb', '.gz', '.gzip', '.one', '.pak',
                         '.pkg', '.ppt', '.sh', '.rpm', '.sib',
                         '.sis', '.sisx', '.sit', '.sitx', '.spl',
                         '.tar', '.tar-gz', '.tgz', '.xar', '.zipx']
        }

        self.path = path

    """
    Функция для получения информации о диске.
    Возвращает кортеж, содержащий размер диска, используемое место на диске
    """

    def get_disk_usage(self):
        total, _, _ = shutil.disk_usage(self.path)
        walk_gen = os.walk(self.path)
        usage = defaultdict(int)
        for root, _, files in walk_gen:
            for file in files:
                try:
                    full_path = os.path.join(root, file)
                    file_size = os.path.getsize(full_path)
                    for category, extensions in self.file_types.items():
                        if any(file.endswith(ext) for ext in extensions):
                            usage[category] += file_size
                            break
                    else:
                        usage["Other"] += file_size
                except Exception as e:
                    print(f"Error on file {full_path}: {str(e)}")
                    usage["Other"] += file_size
        return total, usage
