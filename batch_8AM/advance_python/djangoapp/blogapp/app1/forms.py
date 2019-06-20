from django import forms

class Login(forms.Form):
    Email = forms.EmailField()
    Password = forms.CharField(max_length=40,widget=forms.PasswordInput)

class Signup(forms.Form):
    Email = forms.EmailField(label="Enter your email")
    Username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':"Enter your Email"}))
    Password = forms.CharField(max_length=40,widget=forms.PasswordInput)
    Confirm_password = forms.CharField(max_length=50,widget=forms.PasswordInput)
    Profile = forms.ImageField()
