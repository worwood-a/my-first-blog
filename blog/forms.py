from django import forms
from .models import Post, EducationItem, WorkItem, TechnicalItem, OtherItem

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class EducationForm(forms.ModelForm):

    class Meta:
        model = EducationItem
        fields = ('name', 'start_year', 'end_year', 'description')

class TechnicalForm(forms.ModelForm):

    class Meta:
        model = TechnicalItem
        fields = ('title', 'content')

class WorkForm(forms.ModelForm):

    class Meta:
        model = WorkItem
        fields = ('title', 'start_year', 'end_year', 'description')

class OtherForm(forms.ModelForm):

    class Meta:
        model = OtherItem
        fields = ('name', 'content')