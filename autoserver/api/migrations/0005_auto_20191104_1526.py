# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-11-04 07:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_server_last_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='业务线')),
            ],
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='机房')),
                ('floor', models.IntegerField(default=1, verbose_name='楼层')),
            ],
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.CharField(max_length=32, verbose_name='插槽位')),
                ('manufacturer', models.CharField(blank=True, max_length=32, null=True, verbose_name='制造商')),
                ('model', models.CharField(max_length=64, verbose_name='型号')),
                ('capacity', models.FloatField(blank=True, null=True, verbose_name='容量')),
                ('sn', models.CharField(blank=True, max_length=64, null=True, verbose_name='内存SN号')),
                ('speed', models.CharField(blank=True, max_length=16, null=True, verbose_name='速度')),
            ],
        ),
        migrations.CreateModel(
            name='Nic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='网卡名称')),
                ('hwaddr', models.CharField(max_length=64, verbose_name='网卡mac地址')),
                ('netmask', models.CharField(max_length=64)),
                ('ipaddrs', models.CharField(max_length=256, verbose_name='ip地址')),
                ('up', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='server',
            name='cabinet_num',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='机柜号'),
        ),
        migrations.AddField(
            model_name='server',
            name='cabinet_order',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='机柜中序号'),
        ),
        migrations.AddField(
            model_name='server',
            name='cpu_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='CPU个数'),
        ),
        migrations.AddField(
            model_name='server',
            name='cpu_model',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='CPU型号'),
        ),
        migrations.AddField(
            model_name='server',
            name='cpu_physical_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='CPU物理个数'),
        ),
        migrations.AddField(
            model_name='server',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='制造商'),
        ),
        migrations.AddField(
            model_name='server',
            name='model',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='型号'),
        ),
        migrations.AddField(
            model_name='server',
            name='os_platform',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='系统'),
        ),
        migrations.AddField(
            model_name='server',
            name='os_version',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='系统版本'),
        ),
        migrations.AddField(
            model_name='server',
            name='sn',
            field=models.CharField(blank=True, db_index=True, max_length=64, null=True, verbose_name='SN号'),
        ),
        migrations.AlterField(
            model_name='server',
            name='last_date',
            field=models.DateField(blank=True, null=True, verbose_name='最近汇报时间'),
        ),
        migrations.AddField(
            model_name='nic',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Server'),
        ),
        migrations.AddField(
            model_name='memory',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Server'),
        ),
        migrations.AddField(
            model_name='server',
            name='business_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.BusinessUnit', verbose_name='业务线'),
        ),
        migrations.AddField(
            model_name='server',
            name='idc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.IDC', verbose_name='机房'),
        ),
    ]
