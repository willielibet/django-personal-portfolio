from django.urls import path
# import the views.py file in the blog folder
from . import views 

app_name = 'blog'

urlpatterns = [
    # acts as the blog homepage
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>', views.detail, name='detail'),
]




