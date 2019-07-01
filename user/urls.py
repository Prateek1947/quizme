from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('profile/', views.ProfileView.as_view()),
    path('profiles/all/', views.AllProfilesView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
