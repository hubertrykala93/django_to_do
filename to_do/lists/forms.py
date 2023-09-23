from django import forms
from .models import Category, Task
from django.core.validators import ValidationError


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
    category = forms.Select()
    name = forms.CharField(max_length=100, label='Task Name', required=True, widget=forms.TextInput(attrs={
        'id': 'category-task-name',
        'label': 'required',
        'type': 'text',
        'placeholder': 'Task Name'
    }))

    description = forms.CharField(max_length=1000, label='Task Description', required=True,
                                  widget=forms.Textarea(attrs={
                                      'id': 'category-task-description',
                                      'label': 'required',
                                      'type': 'text',
                                      'placeholder': 'Task Description'
                                  }))

    class Meta:
        model = Task
        fields = ['category', 'name', 'description']
