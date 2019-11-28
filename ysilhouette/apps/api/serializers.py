from rest_framework import serializers
from .models import Resume, Skills, Education, Projects, Blogs, Jobs


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ('id', 'name', 'phone', 'email', 'blog', 'website')


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ('id', 's_name', 's_grade')


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('id', 'e_name', 'e_major', 'e_sdate', 'e_edate')


class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ('id', 'j_name', 'j_sdate', 'j_edate', 'j_content')


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'p_name', 'p_sdate', 'p_edate', 'p_content')


class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = ('blog_id', 'blog_title', 'blog_content', 'blog_editor', 'blog_ctime', 'blog_utime')
