from django import forms
from .models import Category, Task


class CategoryForm(forms.ModelForm):
    category = forms.CharField(max_length=100, label='Category', required=True, widget=forms.TextInput(attrs={
        'id': 'user-category',
        'label': 'required',
        'type': 'text',
        'placeholder': 'New Category'
    }))

    class Meta:
        model = Category
        fields = ['category']


class TaskForm(forms.ModelForm):
    content = forms.CharField(max_length=1000, label='Content', required=True, widget=forms.Textarea(attrs={
        'id': 'category-task',
        'label': 'required',
        'type': 'text',
        'placeholder': 'New Task'
    }))

    class Meta:
        model = Task
        fields = '__all__'
