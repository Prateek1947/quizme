from django.urls.conf import path
from submission.views import *

urlpatterns = [
    path('activity/', ActivityView.as_view()),
    path('me/', SubmissionView.as_view())
]
