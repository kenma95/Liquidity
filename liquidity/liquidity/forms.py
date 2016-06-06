from django import forms  
from django.contrib.auth.models import User  
  
class LoginForm(forms.Form):  
    username = forms.CharField(  
        required=True,  
        label=u"Username",  
        error_messages={'required': 'Please enter username'},  
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u"Username",  
            }  
        ),  
    )      
    password = forms.CharField(  
        required=True,  
        label=u"Password",  
        error_messages={'required': u'Please enter password'},  
        widget=forms.PasswordInput(  
            attrs={  
                'placeholder':u"Password",  
            }  
        ),  
    )     
    def clean(self):  
        if not self.is_valid():  
            raise forms.ValidationError(u"All required")  
        else:  
            cleaned_data = super(LoginForm, self).clean()   


class RegForm(forms.Form):
    username = forms.CharField(  
        required=True,  
        label=u"Username",  
        error_messages={'required': 'Please enter username'},  
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u"Username",  
            }  
        ),  
    )      
    password = forms.CharField(  
        required=True,  
        label=u"Password",  
        error_messages={'required': u'Please enter password'},  
        widget=forms.PasswordInput(  
            attrs={  
                'placeholder':u"Password",  
            }  
        ),  
    )     
    def clean(self):  
        if not self.is_valid():  
            raise forms.ValidationError(u"All required")  
        else:  
            cleaned_data = super(RegForm, self).clean()   
