from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view

from .models import Resume,Skills,Education,Projects,Blogs
from .serializers import ResumeSerializer,SkillsSerializer,EducationSerializer,ProjectsSerializer,BlogsSerializer
from .paginations import StandardResultSetPagination
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class ResumeView(ModelViewSet):
    queryset = Resume.objects.get_queryset().order_by('id')
    serializer_class = ResumeSerializer
    pagination_class = StandardResultSetPagination


@api_view(['GET'])
def getresume(request,format=None,*args, **kwargs):
    if request.method == 'GET':
        id = request.GET['id']
        if id is not None:
            resume = Resume.objects.filter(id=id)
            resume_obj = StandardResultSetPagination()
            resume_page_list = resume_obj.paginate_queryset(resume,request)
            resume_ser = ResumeSerializer(instance=resume_page_list,many=True)
            response = resume_obj.get_paginated_response(resume_ser.data)
            return response
        else:
            return HttpResponse("请传id")


def getskills(request,format=None,*args,**kwargs):
    if request.method == 'GET':
        s_id = request.GET['id']
        if s_id is not None:
            skills = Skills.objects.filter(s_id=s_id)
            skills_obj = StandardResultSetPagination()
            skills_page_list = skills_obj.paginate_queryset(skills,request)
            skills_ser = SkillsSerializer(instance=skills_page_list,many=True)
            response = skills_obj.get_paginated_response(skills_ser.data)
            return response
        else:
            return HttpResponse("请传用户名")





