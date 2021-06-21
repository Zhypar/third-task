from .models import Branch, Category, Course, Contact
from rest_framework import serializers
from django.db import models


class CategorySerializer(serializers.Serializer):

    name = serializers.CharField(max_length=60)
    imgpath = serializers.CharField(max_length=60)

    class Meta:
        model = Category
        fields = ['name', 'imgpath']



class BranchSerializer(serializers.Serializer):

    latitude = serializers.CharField(max_length=60)
    longtitude = serializers.CharField(max_length=60)
    address = serializers.CharField(max_length=60)
    branch_course = serializers.CharField(required=False, max_length=60)

    class Meta:
        model = Branch
        fields = ['latitude', 'longtitude', 'adress', 'course']


class ContactSerializer(serializers.Serializer):

    type = serializers.CharField(max_length = 20)
    value = serializers.CharField(max_length = 60)
    contact_course = serializers.CharField(required=False, max_length = 60)

    class Meta:
        model = Contact
        fields = ['value', 'type']

    
class CourseSerializer(serializers.Serializer):

    id = serializers.IntegerField(default = True)
    name = serializers.CharField(max_length=60)
    description = serializers.CharField(max_length=60)
    category = serializers.CharField(max_length=60)
    logo = serializers.CharField(max_length=60)
    contacts = serializers.CharField(required=False, max_length=60)
    branches = serializers.CharField(required=False, max_length=60)
    contacts = ContactSerializer(required=False, many = True)
    branches = BranchSerializer(required=False, many = True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'category', 'logo', 'contacts', 'branches']


    def create(self, validated_data):
        contacts_data = validated_data.pop('contacts')
        branches_data = validated_data.pop('branches')
        course = Course.objects.create(**validated_data)

        for contact_data in contacts_data:
            Contact.objects.create(course=course, **contact_data)

        for branch_data in branches_data:
            Branch.objects.create(course=course, **branch_data)
        
        return course
