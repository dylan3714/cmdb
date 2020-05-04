import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PLUGIN_CLASS_DICT = {
    "disk": 'lib.plugins.disk.DiskPlugin',
    'memory': 'lib.plugins.memory.MemoryPlugin',
    'network': 'lib.plugins.network.NetworkPlugin',
    'basic': 'lib.plugins.basic.BasicPlugin',
    'board': 'lib.plugins.board.BoardPlugin',
}

SSH_USER = 'root'
SSH_PORT = 22
SSH_PWD = '123'

LOGGING_PATH = os.path.join(BASE_DIR,'log/cmdb.log')

LOCAL_DISK_FILE_PATH = os.path.join(BASE_DIR,'files/disk.out')

API_URL = "http://127.0.0.1:8000/api/server/"