from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from . import views


urlpatterns = [
    # rest-auth/ includes login/, logout/:
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),

    path('users/', views.ListUser.as_view()),
    path('users/<int:pk>/', views.DetailUser.as_view()),

    path('jobs/', views.ListJob.as_view()),
    path('jobs/<int:pk>/', views.DetailJob.as_view()),

    path('saved/', views.ListSaved.as_view()),
    path('saved/<int:pk>/', views.DetailSaved.as_view()),

    path('unreviewed/', views.ListUnreviewed.as_view()),
    path('unreviewed/<int:pk>/', views.DetailUnreviewed.as_view()),

    # The body of this will contain search terms if any
    path('getghjobs/', views.get_gh_jobs),

]
