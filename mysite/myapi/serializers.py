from .models import Branch, Category, Course, Contact
from rest_framework import serializers
from django.db import models


class CategorySerializer(serializers.Serializer):

    name = serializers.CharField(required=False, max_length=60)
    imgpath = serializers.CharField(required=False, max_length=60)

    class Meta:
        model = Category
        fields = ['name', 'imgpath']

    def __str__(self):
        return self.name

    def create(self, validated_data, *args, **kwargs):
        category = Category.objects.create(**validated_data)
        category.save()
        return category
        



class BranchSerializer(serializers.Serializer):

    latitude = serializers.CharField(required=False, max_length=60)
    longtitude = serializers.CharField(required=False, max_length=60)
    address = serializers.CharField(required=False, max_length=60)

    class Meta:
        model = Branch
        fields = ['latitude', 'longtitude', 'address']

    def create(self, validated_data, *args, **kwargs):
        branch = Branch.objects.create(**validated_data)
        branch.save()
        return branch


class ContactSerializer(serializers.Serializer):

    type = serializers.CharField(required=False, max_length = 60)
    value = serializers.CharField(required=False, max_length = 60)

    class Meta:
        model = Contact
        fields = ['value', 'type']

    def create(self, validated_data, *args, **kwargs):
        contact = Contact.objects.create(**validated_data)
        contact.save()
        return contact

    
class CourseSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField(max_length=60)
    description = serializers.CharField(max_length=60)
    category = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(),
        required = False
    )
    logo = serializers.CharField(max_length=60)
    contacts = ContactSerializer(required=False, many = True, allow_null=True)
    branches = BranchSerializer(required=False, many = True, allow_null=True)

    class Meta:
        model = Course
        fields = ['id','name', 'description', 'category', 'logo', 'contacts', 'branches']

    def __str__(self):
        return self.name

    def create(self, validated_data, *args, **kwargs):        

        contacts_data = validated_data.pop('contacts')
        branches_data = validated_data.pop('branches')
        course = Course.objects.create(**validated_data)
        course.save()

        for contact_data in contacts_data:
            Contact.objects.create(course=course, **contact_data)
            course.save()

        for branch_data in branches_data:
            Branch.objects.create(course=course, **branch_data)
            course.save() 
        
        return course