from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email',)

class CustomUserChangeForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)

