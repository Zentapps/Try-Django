
from django import forms
from django.forms.widgets import TextInput, Textarea, Select,DateInput
from django.utils.translation import ugettext_lazy as _
from posts.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ['creator', 'updater', 'auto_id', 'is_deleted', ]
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Enter title'}),
            'publication_date': DateInput(attrs={'type': 'date','placeholder': 'Enter publication date'}),
        }
