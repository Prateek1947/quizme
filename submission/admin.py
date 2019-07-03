from django.contrib import admin
from submission.models import Submission


# Register your models here.
class SubmissionAdmin(admin.ModelAdmin):
    readonly_fields = ('is_correct',)


admin.site.register(Submission, SubmissionAdmin)
