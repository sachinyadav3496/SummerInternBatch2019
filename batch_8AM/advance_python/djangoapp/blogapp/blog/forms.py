from django import forms
import datetime
class Blog(forms.Form):
    title = forms.CharField(max_length=50)
    post = forms.CharField(widget=forms.Textarea,max_length=100)
    date = forms.DateField(initial=datetime.date.today)