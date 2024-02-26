from django.utils.translation import gettext, gettext_lazy as _
from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.forms.widgets import TextInput, PasswordInput, EmailInput, Select


User = get_user_model()


class UserForm(UserCreationForm):

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),
        help_text=password_validation.password_validators_help_text_html(),

    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),
        strip=False,
        help_text="Enter the same password as before, for verification.",

    )

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email',
        ]

        widgets = {
            'username': TextInput(attrs={'placeholder': 'Enter username'}),
            'first_name': TextInput(attrs={'placeholder': 'Enter first name'}),
            'last_name': TextInput(attrs={'placeholder': 'Enter last name'}),
            'email': EmailInput(attrs={'placeholder': 'Enter email'}),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # For case sensitive Username
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("This username is already in use.")
        return username


class LoginForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )

    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }
