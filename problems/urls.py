from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('problems/', views.ProblemList.as_view()),
    path('problem/<int:pk>/', views.ProblemDetail.as_view()),
    path('login/', obtain_auth_token),
    path('logout/', views.LogoutView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
