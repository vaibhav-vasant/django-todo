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
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter todo title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter todo description'}),
            'completed': forms.CheckboxInput(),
        }

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.fields['deadline'].widget.format = '%Y-%m-%dT%H:%M'
        self.fields['deadline'].input_formats = ('%Y-%m-%dT%H:%M',)
