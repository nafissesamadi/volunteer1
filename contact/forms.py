from django import forms
from .models import ContactUs


# class ContactUsForm(forms.Form):
#     full_name = forms.CharField(
#         label='Full Name',
#         max_length=50,
#         required=False,
#         error_messages={
#             'required': 'Please Enter Your Full Name ',
#             'max_length': 'It is more than 50 character'
#         },
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Full Name'
#         })
#     )
#     email = forms.EmailField(
#         label='Email',
#         widget=forms.EmailInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Email'
#         })
#     )
#     subject = forms.CharField(
#         label='Title',
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Title'
#         })
#     )
#     text = forms.CharField(
#         label='Message',
#         widget=forms.Textarea(attrs={
#             'class': 'form-control',
#             'placeholder': 'Message Text',
#             'rows': '5'
#         }))


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs

        fields = ['full_name', 'email', 'title', 'message']
        # fields='__all__'
        # exclude=['response']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'id': 'message'
            })
        }

        labels = {
            'full_name': 'Full Name',
            'email': 'Email',
            'title': 'Title',
            'message': 'Message Text'
        }

        error_messages = {
            'full_name': {
                'required': 'Please Enter Your Full Name'
            }
        }


# class ProfileForm(forms.Form):
#     user_image=forms.ImageField()
#     # user_image = forms.FileField()
