import datetime
from django import forms
from ckeditor.fields import forms
from ckeditor.fields import RichTextFormField


class CreatePost(forms.Form):
    title = forms.CharField(max_length=1000)
    subtitle = forms.CharField(max_length=1000)
    content = RichTextFormField()
    publish_date = forms.DateTimeField()

    
    