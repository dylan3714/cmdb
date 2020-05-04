from django.shortcuts import render,redirect
from api import models
def index(request):
    """
    后台管理首页
    :param request:
    :return:
    """
    server_list = models.Server.objects.all()
    return render(request,'index.html',{'server_list':server_list})

from django import forms
class ServerModelForm(forms.ModelForm):
    class Meta:
        model = models.Server
        fields = ['hostname','business_unit','idc','cabinet_num','cabinet_order','status']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

def create_server(request):
    """
    增加服务器
    :param request:
    :return:
    """
    if request.method == "GET":
        form = ServerModelForm()
        return render(request,'create_server.html',{'form':form})
    form = ServerModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/index/')
    return render(request, 'create_server.html', {'form': form})
