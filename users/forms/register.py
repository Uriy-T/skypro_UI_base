from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomBaseUser
from configuration import AVAILABLE_COUNTRIES


class CreateUser(UserCreationForm):
    username = forms.CharField(max_length=50, required=True)
    country = forms.ChoiceField(
        choices=AVAILABLE_COUNTRIES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=True
    )

    class Meta:
        model = CustomBaseUser
        fields = ('email', 'username', 'first_name', 'last_name', 'avatar', 'country', 'phone_number','password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

            if field_name in ['password1', 'password2']:
                field.help_text = ''


class UpdateUser(UserChangeForm):
    username = forms.CharField(max_length=50, required=True)
    country = forms.ChoiceField(
        choices=AVAILABLE_COUNTRIES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=True
    )
    class Meta:
        model = CustomBaseUser
        fields = ('email', 'username', 'first_name', 'last_name', 'avatar', 'country', 'phone_number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

            if field_name == 'country':
                field.widget.attrs['class'] = 'form-select'