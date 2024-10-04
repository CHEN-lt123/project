"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from myapp.views import NewsListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('index/',views.index),

    #最新消息
    path('news/', views.news, name='news'),
    path('new01/', views.new01, name='new01'),
    


    #掛號預約
    path('test/', views.test, name='test'),
    path('login/',views.login),
    path('select-department/',views.select_department), 
    path('select-doctor/',views.select_doctor),
    path('select-time/',views.select_time), 
    path('success/',views.success), 

    #掛哪一科
    #關於我們



    
    

     # path('project/<str:username>/',views.project),
         # path('api/news/', NewsListView.as_view(), name='news-list'),
   
]
    # 最新消息debug
    # base.html 中使用了 {% url 'news' %}，但 urls.py 中的 'news' URL pattern 沒有給定名稱。
    # urls.py 中的 path 添加 name 參數：
    # path('news/', views.news),
