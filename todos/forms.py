from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],
        help_text='Optional. Format: YYYY-MM-DDThh:mm'
    )

    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed', 'deadline']

    def clean_deadline(self):
        deadline = self.cleaned_data.get('deadline')
        if deadline and deadline < timezone.now():
            raise forms.ValidationError('Deadline must be in the future.')
        return deadline
