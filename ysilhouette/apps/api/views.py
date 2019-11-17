from django.shortcuts import render
from django.http import HttpResponse
from apps.api.models import Resume
# Create your views here.


def base_info(request):
    resume = Resume.objects.all()[0]

    name = resume.name
    phone = resume.phone
    email = resume.email
    blog = resume.blog
    website = resume.website
    resumes = (name,phone,email,blog,website)

    return HttpResponse(resumes)
