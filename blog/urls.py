from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('comment/create/<int:blog_id>/', views.comment_create, name='comment_create'),
    path('blog/create/', views.blog_create, name='blog_create'),
]