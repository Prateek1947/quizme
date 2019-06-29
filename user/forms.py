from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from user.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'following')


class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'
