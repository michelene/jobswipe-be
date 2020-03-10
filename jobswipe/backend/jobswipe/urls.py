from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from . import views


urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),

    path('users/', views.UserListView.as_view()),

    path('jobs/', views.ListJobs.as_view()),
    path('joblists/', views.ListNewJobLists.as_view()),

    path('jobs/<int:pk>/', views.DetailJob.as_view()),
    path('joblists/<int:pk>/', views.DetailNewJobList.as_view()),

    path('getghjobs/', views.get_gh_jobs),
    path('getghjobs/<str:search_terms>', views.get_gh_jobs),


]
