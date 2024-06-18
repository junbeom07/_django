"""
URL configuration for ohyen_highschool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from main.views import index, jejuohyun, g_1st, g_2nd, g_3rd, my_page, grade

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('jejuohyun/', jejuohyun),
    path('1st/', g_1st),
    path('2nd/', g_2nd),
    path('3rd/', g_3rd),
    path('grade/', grade),
    path('my_page/', my_page),
]
