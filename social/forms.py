from django import forms
from django.contrib.auth.models import User
from social.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # These are the additional fields we want users to have on top of the
        # ones provided by Django's base 'User' model
        fields = ('picture', 'location', 'bio', 'dob', 'university' )
        

# Don't think we need to add any forms for Universities/subjects/etc as
# this is handled by the Superusers/admins of the site ?
# Also the reason why we only improt UserProfile
