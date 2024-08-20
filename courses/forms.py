from django import forms
from .models import Course, CourseInstance

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'code', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

class CourseInstanceForm(forms.ModelForm):
    class Meta:
        model = CourseInstance
        fields = ['course', 'year', 'semester']
        widgets = {
            'semester': forms.TextInput(attrs={'placeholder': 'e.g., Fall, Spring'}),
        }