from blogapp.models import Profile
from django import forms


class createProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('bio', 'iam', 'profile_pic',
                  'facebook', 'instagram', 'twitter', 'user', 'sexe')
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'id': 'username', 'type': 'hidden'}),
            'iam': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'I am'}),
            'sexe': forms.Select(attrs={'class': 'form-control'}),
            'facebook': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'facebook'}),
            'instagram': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'instagram'}),
            'twitter': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'twitter'}),

        }


class editProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('bio', 'iam', 'profile_pic',
                  'facebook', 'instagram', 'twitter', 'user', 'sexe')
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'id': 'username', 'type': 'hidden'}),
            'iam': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'i am a (an)'}),
            'facebook': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'facebook'}),
            'instagram': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'instagram'}),
            'twitter': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'twitter'}),
            'sexe': forms.Select(attrs={'class': 'form-control'}),
        }
