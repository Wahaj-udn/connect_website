# C:\Users\Admin\connect_website\collaborate\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('collaborate/', views.collaborate, name='collaborate'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('contribute/', views.contribute, name='contribute'),
    path('projects/', views.projects, name='projects'),
    path('profile/', views.profile, name='profile'),

    path('about/', views.placeholder_view, name='about'),
    path('milestones/', views.placeholder_view, name='milestones'),
    path('contact/', views.placeholder_view, name='contact'),
    path('share_idea/', views.placeholder_view, name='share_idea'),
]
