from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(required=True, max_length=100)

    class Meta:
        model = User
        fields = ('name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['name']
        if commit:
            user.save()
        return user
