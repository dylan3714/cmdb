from concurrent.futures import ThreadPoolExecutor

import requests
import settings
from lib.plugins import get_server_info

def ssh(hostname,cmd):
    import paramiko

    # 创建SSH对象
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname=hostname, port=settings.SSH_PORT, username=settings.SSH_USER, password=settings.SSH_PWD)
    # 执行命令
    stdin, stdout, stderr = ssh.exec_command(cmd)
    # 获取命令结果
    result = stdout.read()
    # 关闭连接
    ssh.close()
    return result.decode('utf-8')

def task(host):
    server_info = get_server_info(ssh, host)
    result = requests.post(
        url=settings.API_URL,
        json={'host': host, 'info': server_info}
    )
    print(result)

def get_server_list():
    response = requests.get(settings.API_URL)
    return response.json()['data']
def run():
    host_list = get_server_list()
    pool = ThreadPoolExecutor(10)
    for host in host_list:
        pool.submit(task,host)

if __name__ == '__main__':
    run()

