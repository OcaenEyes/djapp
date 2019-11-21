from rest_framework import serializers
from .models import Resume, Skills, Education, Projects, Blogs


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ('id', 'name', 'phone', 'email', 'blog', 'website')


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ('s_id', 's_name', 's_grade')


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('e_id', 'e_name', 'e_major', 'e_sdate', 'e_edate')


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('p_id', 'p_name', 'p_sdate', 'p_edate', 'p_content')


class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = ('blog_id', 'blog_title', 'blog_content', 'blog_editor', 'blog_ctime', 'blog_utime')
