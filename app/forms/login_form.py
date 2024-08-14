from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginModelForm(AuthenticationForm):
    username = forms.CharField(required=False)
    phone_number = forms.CharField()
    password = forms.CharField(max_length=128)

    def clean(self):
        phone_number = self.cleaned_data.get('phone_number')
        password = self.cleaned_data.get('password')
        if phone_number and password:
            self.user_cache = authenticate(self.request,
                         phone_number=phone_number,
                         password=password)
            if self.user_cache:
                self.confirm_login_allowed(self.user_cache)
            else:
                raise self.get_invalid_login_error()

        return self.cleaned_data