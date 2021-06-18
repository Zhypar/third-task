from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^category/', views.CategoryAPIViews.as_view()),
    url(r'^branch/', views.BranchAPIViews.as_view()),
    url(r'^contact/', views.ContactAPIViews.as_view()),
    url(r'^courses/', views.CourseAPIViews.as_view()),
]