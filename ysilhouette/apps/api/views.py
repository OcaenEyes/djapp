from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view

from .models import Resume, Skills, Education, Projects, Blogs,Jobs
from .serializers import ResumeSerializer, SkillsSerializer, EducationSerializer, ProjectsSerializer, BlogsSerializer,JobsSerializer
from .paginations import StandardResultSetPagination
from rest_framework.viewsets import ModelViewSet


# Create your views here.


class ResumeView(ModelViewSet):
    queryset = Resume.objects.get_queryset().order_by('id')
    serializer_class = ResumeSerializer
    pagination_class = StandardResultSetPagination


@api_view(['GET'])
def getresume(request, *args, **kwargs):
    if request.method == 'GET':
        id = request.GET['id']
        if id is not None:
            resume = Resume.objects.filter(id=id)
            resume_obj = StandardResultSetPagination()
            resume_page_list = resume_obj.paginate_queryset(resume, request)
            resume_ser = ResumeSerializer(instance=resume_page_list, many=True)
            response = resume_obj.get_paginated_response(resume_ser.data)
            return response
        else:
            return HttpResponse("请传id")


@api_view(['GET'])
def getskills(request, *args, **kwargs):
    if request.method == 'GET':
        id = request.GET['id']
        if id is not None:
            skills = Skills.objects.filter(s_id_id=id).order_by("-id")
            skills_obj = StandardResultSetPagination()
            skills_page_list = skills_obj.paginate_queryset(skills, request)
            skills_ser = SkillsSerializer(instance=skills_page_list, many=True)
            response = skills_obj.get_paginated_response(skills_ser.data)
            return response
        else:
            return HttpResponse("请传用户名")


@api_view(['GET'])
def getprojects(request, *args, **kwargs):
    if request.method == 'GET':
        id = request.GET['id']
        if id is not None:
            projects = Projects.objects.filter(p_id_id=id).order_by("-id")
            projects_obj = StandardResultSetPagination()
            projects_page_list = projects_obj.paginate_queryset(projects, request)
            projects_ser = ProjectsSerializer(instance=projects_page_list, many=True)
            response = projects_obj.get_paginated_response(projects_ser.data)
            return response
        else:
            return HttpResponse("请传用户名")


@api_view(['GET'])
def getjobs(request, *args, **kwargs):
    if request.method == 'GET':
        id = request.GET['id']
        if id is not None:
            jobs = Jobs.objects.filter(j_id_id=id).order_by("-id")
            jobs_obj = StandardResultSetPagination()
            jobs_page_list = jobs_obj.paginate_queryset(jobs, request)
            jobs_ser = JobsSerializer(instance=jobs_page_list, many=True)
            response = jobs_obj.get_paginated_response(jobs_ser.data)
            return response
        else:
            return HttpResponse("请传用户名")


@api_view(['GET'])
def geteducation(request, *args, **kwargs):
    if request.method == 'GET':
        id = request.GET['id']
        if id is not None:
            education = Education.objects.filter(id=id)
            education_obj = StandardResultSetPagination()
            education_page_list = education_obj.paginate_queryset(education, request)
            education_ser = EducationSerializer(instance=education_page_list, many=True)
            response = education_obj.get_paginated_response(education_ser.data)
            return response
        else:
            return HttpResponse("请传用户名")


@api_view(['GET'])
def getblogs(request, *args, **kwargs):
    if request.method == 'GET':
        id = request.GET['id']
        if id is not None:
            blogs = Blogs.objects.filter(blog_editor_id=id).order_by("-blog_id")
            blogs_obj = StandardResultSetPagination()
            blogs_page_list = blogs_obj.paginate_queryset(blogs, request)
            blogs_ser = BlogsSerializer(instance=blogs_page_list, many=True)
            response = blogs_obj.get_paginated_response(blogs_ser.data)
            return response
        else:
            return HttpResponse("请传用户名")
