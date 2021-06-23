from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactSerializer, CategorySerializer, BranchSerializer, CourseSerializer
from .models import Contact, Category, Branch, Course


class CategoryAPIViews(APIView):
    serializer_class = CategorySerializer

    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response({"category": serializer.data})

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            name = serializer.data.get('name')
            success = "Category '{0}' has been added successfully".format(name)
            return Response({'success': success})
        else:
            return  Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BranchAPIViews(APIView):
    serializer_class = BranchSerializer

    def get(self, request):
        branch = Branch.objects.all()
        serializer = BranchSerializer(branch, many=True)
        return Response({"branch": serializer.data})

    def post(self, request):
        serializer = BranchSerializer(data=request.data)
        if serializer.is_valid():
            address = serializer.data.get('address')
            success = "Branch '{0}' has been added successfully".format(address)
            return Response({'success': success})
        else:
            return  Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactAPIViews(APIView):
    serializer_class = ContactSerializer

    def get(self, request):
        contact = Contact.objects.all()
        serializer = ContactSerializer(contact, many=True)
        return Response({"contact": serializer.data})

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            type = serializer.data.get('type')
            success = "Contact '{0}' has been added successfully".format(type)
            return Response({'success': success})

        else:
            return  Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseAPIViews(APIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        courses = Course.objects.all()
        return courses

    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params["id"]
            if id != None:
                course = Course.objects.get(id=id)
                serializer = CourseSerializer(course)
        except:
            courses = self.get_queryset()
            serializer = CourseSerializer(courses, many = True)

        return Response(serializer.data)


    def delete(self, request, *args, **kwargs):
        try:
            id = request.query_params["id"]
            if id != None:
                course = Course.objects.get(id=id)
                course.delete()
        except Course.DoesNotExist:
            return Response({'message': 'The course does not exist'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'message': 'Course has been deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        

    def post(self, request):
        serializer = CourseSerializer(data= self.request.data)
        if serializer.is_valid():
            serializer.save()
            success = "Course has been added successfully!"
            return Response({'success': success})
        else:
            return  Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

