# from django import forms
# from .models import Task

# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['title', 'description', 'status']

#     # Optional: Customize the form field for status if needed
#     status = forms.ChoiceField(choices=Task.STATUS_CHOICES, widget=forms.Select)


from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']
        widgets = {
            'status': forms.Select(choices=Task.STATUS_CHOICES),
        }

