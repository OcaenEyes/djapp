"""ysilhouette URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from . import settings
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from apps.api import views
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="index.html")),
    path('api/getresume',views.getresume),
    path('api/getskills',views.getskills),
    path('api/getprojects',views.getprojects),
    path('api/getjobs',views.getjobs),
    path('api/geteducation',views.geteducation),
    path('api/getblogs',views.getblogs),
    re_path(r'^api/resume/(?P<pk>\d+)/$',views.ResumeView.as_view({'get': 'retrieve','delete':'destroy','put':'update','patch':'partial_update'})),
    re_path(r'^api/media/(?P<path>.*)$',serve,{"document_root":settings.MEDIA_ROOT})


] + staticfiles_urlpatterns()
