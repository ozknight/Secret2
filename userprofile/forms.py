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
        label='Birthday',
        error_messages={
            'required': ("Please set Your Birthdate"),
            'invalid': ("Invalid Birthdate")
        },
        widget=forms.DateTimeInput(
            attrs={
                'placeholder': 'mm/dd/yyyy',
                'type': 'date',
                'class': 'datepicker'
            }
        )
    )
    gender = forms.ChoiceField(
        error_messages={
            'invalid': ("Invalid Gender")
        },
        choices=GENDER,
        widget=forms.Select(
            attrs={
                'placeholder': 'Select A Gender'
            }
        )
    )
    phone = forms.CharField(
        error_messages={
            'invalid': ("Invalid Phone Number")
        },
        widget=forms.TextInput(
            attrs={
                'type': 'number',
                'placeholder': 'Phone Number',
                'maxlength': '15'
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
