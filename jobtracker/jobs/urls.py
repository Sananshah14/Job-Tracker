# jobs/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home_redirect, name="home"),
    path('dashboard', views.dashboard, name='dashboard'),
    path('joblist/', views.job_list, name='job_list'),
    path('add/', views.add_job, name='add_job'),
    path('<int:job_id>/update/', views.update_job, name='update_job'),
    path('<int:job_id>/delete/', views.delete_job, name='delete_job'),
    path('job_statistics/', views.job_statistics, name='job_statistics'),
    path('signup/', views.SignupView.as_view(), name = 'signup'),
    path('login/', views.LoginInterfaceView.as_view(),name = 'login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
