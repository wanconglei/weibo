from django.contrib.auth.forms import UserCreationForm
from .models import WBUser


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = WBUser
        fields = ('username', 'email')

