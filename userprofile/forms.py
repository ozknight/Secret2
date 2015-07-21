from django import forms
from .models import Profile, GENDER


class ProfileCreateForm(forms.ModelForm):

    ''' Create Profile For User Instance '''
    avatar = forms.ImageField(
        label=('User Avatar'),
        required=False,
        error_messages={
            'invalid': ("Image files only")},
        widget=forms.FileInput(
            attrs={
                'type': 'image',
                'placeholder': 'Select Avatar'
            }
        )
    )
    birthdate = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'placeholder': 'mm/dd/yyyy',
                'type': 'date',
                'class': 'datepicker'
            }
        )
    )
    gender = forms.ChoiceField(
        choices=GENDER,
        widget=forms.RadioSelect()
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Phone Number'
            }
        )
    )
    about_you = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': '5'
            }
        )
    )

    class Meta:
        model = Profile
        exclude = ('status', 'id', 'user')
