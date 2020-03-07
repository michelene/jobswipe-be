from django.urls import path
from . import views

urlpatterns = [
    path('jobs', views.ListJobs.as_view()),
    path('joblists', views.ListJobLists.as_view()),
    path('jobseekers', views.ListJobSeekers.as_view()),

    path('jobs/<int:pk>/', views.DetailJob.as_view()),
    path('joblists/<int:pk>/', views.DetailJobList.as_view()),
    path('jobseekers/<int:pk>/', views.DetailJobSeeker.as_view()),

    # path('getjobs/', views.hello_world.as_view()),
    path('getjobs/', views.hello_world)
]
