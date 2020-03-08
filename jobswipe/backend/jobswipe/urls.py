from django.urls import include, path
from . import views

urlpatterns = [
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),

    path('jobs', views.ListJobs.as_view()),
    # path('joblists', views.ListJobLists.as_view()),
    # path('jobseekers', views.ListJobSeekers.as_view()),

    path('jobs/<int:pk>/', views.DetailJob.as_view()),
    # path('joblists/<int:pk>/', views.DetailJobList.as_view()),
    # path('jobseekers/<int:pk>/', views.DetailJobSeeker.as_view()),

    path('getghjobs/<int:pk>/', views.get_gh_jobs),
    path('getghjobs/<int:pk>/<str:search_terms>', views.get_gh_jobs),


]
