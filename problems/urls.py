from django.urls import path
from . import views

urlpatterns = [
    path('', views.Problems.as_view())
]
