"""
用于采集内存信息
"""
import traceback
from .base import BasePlugin
from lib.utils.log import logger
from lib.utils.response import BaseResponse
from lib.utils import convert
from .base import BasePlugin
class MemoryPlugin(BasePlugin):
    """
    采集内存信息
    """

    def process(self,ssh,hostname):
        # 假设执行了命令
        response = BaseResponse()
        try:
            result = ssh(hostname, 'dmidecode  -q -t 17 2>/dev/null')
            response.data = self.parse(result)
        except Exception as e:
            logger.error(traceback.format_exc())
            response.status = False
            response.error = traceback.format_exc()
        return response.dict

    def parse(self, content):
        """
        解析shell命令返回结果
        :param content: shell 命令结果
        :return:解析后的结果
        """
        ram_dict = {}
        key_map = {
            'Size': 'capacity',
            'Locator': 'slot',
            'Type': 'model',
            'Speed': 'speed',
            'Manufacturer': 'manufacturer',
            'Serial Number': 'sn',

        }
        devices = content.split('Memory Device')
        for item in devices:
            item = item.strip()
            if not item:
                continue
            if item.startswith('#'):
                continue
            segment = {}
            lines = item.split('\n\t')
            for line in lines:
                if len(line.split(':')) > 1:
                    key, value = line.split(':')
                else:
                    key = line.split(':')[0]
                    value = ""
                if key in key_map:
                    if key == 'Size':
                        segment[key_map['Size']] = convert.convert_mb_to_gb(value, 0)
                    else:
                        segment[key_map[key.strip()]] = value.strip()
            ram_dict[segment['slot']] = segment
        return ram_dict