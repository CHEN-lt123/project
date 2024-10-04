###import point###
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'index.html',locals())

#最新消息 未製作
from rest_framework import generics
from .models import news
from .serializers import NewsSerializer
class NewsListView(generics.ListAPIView):
    queryset = news.objects.all().order_by('-date')
    serializer_class = NewsSerializer

def news(request):
    return render(request, 'news.html',locals())
def new01(request):
    return render(request, 'new01.html',locals())


#掛號預約
def test(request):
    return render(request, 'test.html',locals())
def login(request):
    return render(request, 'login.html',locals())
def select_department(request):
    return render(request, 'select-department.html',locals())
def select_doctor(request):
    return render(request, 'select-doctor.html',locals())
def select_time(request):
    return render(request, 'select-time.html',locals())
def success(request):
    return render(request, 'success.html',locals())

#掛哪一科 

###import point###
from django.http import JsonResponse
import json
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt  # 导入 csrf_exempt
from django.test import TestCase
from django.urls import reverse


