from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    error_css_class = ""
    email = forms.EmailField(
        widget = forms.TextInput(attrs = {
            'class': 'form-control input-lg',
            'placeholder': 'Username'}),
        max_length = 140,
        required = True
        )

    password = forms.CharField(
        widget = forms.PasswordInput(attrs = {
            'class': 'form-control input-lg',
            'placeholder': 'Password'})
        )
    
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if email and password:
            self.user = authenticate(username=email, password=password)
            if self.user is not None:
                if self.user.is_active:
                    print "active user"
                    return cleaned_data
                else:
                    print "disabled user"
                    raise forms.ValidationError('User has been disabled.', code = 'disabled')
            else:
                print "invalid user"
                raise forms.ValidationError('Invalid email/password combination.', code = 'invalid')