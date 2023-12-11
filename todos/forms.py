from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class UserRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password = forms.CharField(widget=forms.PasswordInput)
    number = forms.CharField(validators=[RegexValidator(regex='^\+?1?\d{9,15}$', message='Enter a valid phone number.')])

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'number')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
