import json
import datetime

from django.views import View
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from api import models
from api.service.disk import process_disk_info

# @method_decorator(csrf_exempt,name='dispatch')
# class ServerView(View):

class ServerView(APIView):

    def get(self,request,*args,**kwargs):
        """
        获取今日未采集的资产信息
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        today = datetime.date.today()
        server_queryset = models.Server.objects.filter(Q(last_date__lt=today) | Q(last_date__isnull=True)).filter(status=1).values_list(
            'hostname')
        #filter(status=1)  除去某个不合适的字段属性用exclude(status = 2)
        server_list = [item[0] for item in server_queryset]
        return JsonResponse({'status': True, 'data': server_list})

    def post(self,request,*args,**kwargs):
        """
        获取中控机汇报的资产信息，并进行入库操作及变更记录。
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        content = request.body.decode('utf-8')
        server_info_dict = json.loads(content)
        hostname = server_info_dict['host']
        info_dict = server_info_dict['info']

        host_object = models.Server.objects.filter(hostname=hostname).first()
        if not host_object:
            print('服务器不存在')
            return HttpResponse('服务器不存在')
        process_disk_info(host_object, info_dict['disk'])

        host_object.last_date = datetime.date.today()
        host_object.save()
        # 获取数据之后，把他们放到数据库
        return HttpResponse('成功')