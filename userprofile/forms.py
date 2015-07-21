from django import forms
from .models import Profile, GENDER

CUSTOM_BOOLEAN = ((True, 'Yes'), (False, 'No'))


class ProfileCreateForm(forms.ModelForm):

    ''' Create Profile For User Instance '''
    avatar = forms.ImageField(
        label='User Avatar',
        required=False,
        error_messages={
            'invalid': ("Image files only")},
        widget=forms.FileInput(
            attrs={
                'type': 'image',
                'class': 'btn',
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
        choices=GENDER, widget=forms.Select(
            attrs={
                'placeholder': 'Select A Gender'
            }
        )
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
                'class': 'materialize-textarea',
                'rows': '5'
            }
        )
    )

    class Meta:
        model = Profile
        exclude = ('employer','status', 'id', 'user')
