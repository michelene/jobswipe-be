from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from . import views


urlpatterns = [
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),


    path('jobs', views.ListJobs.as_view()),
    path('joblists', views.ListJobLists.as_view()),

    path('jobs/<int:pk>/', views.DetailJob.as_view()),
    path('joblists/<int:pk>/', views.DetailJobList.as_view()),

    path('getghjobs/<int:pk>/', views.get_gh_jobs),
    path('getghjobs/<int:pk>/<str:search_terms>', views.get_gh_jobs),


]
