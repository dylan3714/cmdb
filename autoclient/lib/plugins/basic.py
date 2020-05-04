import traceback
from .base import BasePlugin
from lib.utils.log import logger
from lib.utils.response import BaseResponse

class BasicPlugin(BasePlugin):
    """
    采集硬盘信息
    """
    def process(self,ssh,hostname):
        response = BaseResponse()
        try:
            uname = ssh(hostname, 'uname').strip()
            version = ssh(hostname, 'cat /etc/issue').strip().split('\n')[0]
            response.data = {
                'uname':uname,
                'version':version,
            }
        except Exception as e:
            logger.error(traceback.format_exc())
            response.status = False
            response.error = traceback.format_exc()
        return response.dict