"""
CMDB表结构
"""
from django.db import models

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=32)


class BusinessUnit(models.Model):
    """
    业务线(部门)
    """
    name = models.CharField('业务线', max_length=64, unique=True)

class IDC(models.Model):
    """
    机房信息：世纪互联6层、兆维8层
    """
    name = models.CharField('机房', max_length=32)
    floor = models.IntegerField('楼层', default=1)


class Server(models.Model):
    """服务器表"""

    status_choice = (
        (1,'上线'),
        (2,'下线'),
    )
    status = models.IntegerField(verbose_name='状态',choices=status_choice,default=1)

    business_unit = models.ForeignKey(verbose_name="业务线",to='BusinessUnit',blank=True,null=True)

    # IDC有关
    idc = models.ForeignKey(verbose_name='机房',to='IDC',blank=True,null=True)
    cabinet_num = models.CharField('机柜号', max_length=30, null=True, blank=True)
    cabinet_order = models.CharField('机柜中序号', max_length=30, null=True, blank=True)

    hostname = models.CharField(verbose_name="主机名",max_length=32)
    last_date = models.DateField(verbose_name='最近汇报时间',null=True,blank=True)
    # 系统信息
    os_platform = models.CharField('系统', max_length=16, null=True, blank=True)
    os_version = models.CharField('系统版本', max_length=16, null=True, blank=True)

    # 主板
    sn = models.CharField('SN号', max_length=64, db_index=True,null=True,blank=True)
    manufacturer = models.CharField(verbose_name='制造商', max_length=64, null=True, blank=True)
    model = models.CharField('型号', max_length=64, null=True, blank=True)
    # CPU信息
    cpu_count = models.IntegerField('CPU个数', null=True, blank=True)
    cpu_physical_count = models.IntegerField('CPU物理个数', null=True, blank=True)
    cpu_model = models.CharField('CPU型号', max_length=128, null=True, blank=True)


class Disk(models.Model):
    """
    硬盘表
    """
    slot = models.CharField(verbose_name='槽位',max_length=32)
    pd_type = models.CharField(verbose_name='类型',max_length=32)
    capacity = models.CharField(verbose_name='容量',max_length=32)
    model = models.CharField(verbose_name='型号',max_length=32)
    server = models.ForeignKey(verbose_name='服务器',to='Server')


class Memory(models.Model):
    """
	内存信息
	"""
    slot = models.CharField('插槽位', max_length=32)
    manufacturer = models.CharField('制造商', max_length=32, null=True, blank=True)
    model = models.CharField('型号', max_length=64)
    capacity = models.FloatField('容量', null=True, blank=True)
    sn = models.CharField('内存SN号', max_length=64, null=True, blank=True)
    speed = models.CharField('速度', max_length=16, null=True, blank=True)

    server = models.ForeignKey('Server', on_delete=models.CASCADE)

class AssetsRecord(models.Model):
    """
    资产变更记录
    """
    content = models.TextField(verbose_name='内容')
    server = models.ForeignKey(verbose_name='服务器',to='Server')
    create_date = models.DateTimeField(verbose_name='时间',auto_now_add=True)


class Nic(models.Model):
    """
    网卡信息
    """
    name = models.CharField('网卡名称', max_length=128)
    hwaddr = models.CharField('网卡mac地址', max_length=64)
    netmask = models.CharField(max_length=64)
    ipaddrs = models.CharField('ip地址', max_length=256)
    up = models.BooleanField(default=False)
    server = models.ForeignKey('Server', on_delete=models.CASCADE)












