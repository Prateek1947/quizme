from user.models import *
from problems.models import Problem
from django.contrib.auth.hashers import make_password


# Create your models here.

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_correct = models.BooleanField(default=False)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    solution_submitted = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return 'Submission for ' + self.problem.title

    def save(self, **kwargs):
        self.is_correct = False
        if make_password(self.solution_submitted, salt='hello') == self.problem.answer:
            self.is_correct = True
            self.problem.solvers.add(self.user)
            self.problem.no_of_solvers = self.problem.solvers.count()
            self.problem.save()
            print(self.problem.no_of_solvers)
        super().save(**kwargs)
