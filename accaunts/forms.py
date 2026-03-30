from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accaunts.models import CustomUser

class CustomUserCreateForm(UserCreationForm):
    error_messages = {
        'password_mismatch': "Parollar bir-biriga mos emas.",
    }

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')
        error_messages = {
            'email': {
                'unique': 'Bu email allaqachon ro\'yxatdan o\'tgan!'
            }
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email
        if commit:
            user.save()
        return user

    first_name = forms.CharField(
        label='Ism',
        error_messages={
            'required': "Ismni kiritish majburiy.",
        },
        widget=forms.TextInput(attrs={
            'class': 'input',
            'placeholder': 'First Name',
        })
    )
    last_name = forms.CharField(
        label='Familiya',
        error_messages={
            'required': "Familiyani kiritish majburiy.",
        },
        widget=forms.TextInput(attrs={
            'class': 'input',
            'placeholder': 'Last Name',
        })
    )
    email = forms.EmailField(
        label='Elektron pochta',
        error_messages={
            'required': "Email manzilni kiritish majburiy.",
            'invalid': "To'g'ri email manzil kiriting.",
        },
        widget=forms.EmailInput(attrs={
            'class': 'input',
            'placeholder': 'Email',
            'autocomplete': 'off',
        })
    )
    password1 = forms.CharField(
        label='Parol',
        error_messages={
            'required': "Parolni kiritish majburiy.",
        },
        widget=forms.PasswordInput(attrs={
            'class': 'input',
            'placeholder': 'Password',
            'autocomplete': 'off',
        })
    )
    password2 = forms.CharField(
        label='Parolni takrorlang',
        error_messages={
            'required': "Parolni takroran kiritish majburiy.",
        },
        widget=forms.PasswordInput(attrs={
            'class': 'input',
            'placeholder': 'Repeat Password',
            'autocomplete': 'off',
        })
    )

class LoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': "Email yoki parol noto'g'ri.",
        'inactive': "Bu foydalanuvchi faol emas.",
    }

    username = forms.EmailField(
        label='Elektron pochta',
        error_messages={
            'required': "Email manzilni kiritish majburiy.",
            'invalid': "To'g'ri email manzil kiriting.",
        },
        widget = forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Elektron pochta kiriting',

        })
    )
    password = forms.CharField(
        label='Parol',
        error_messages={
            'required': "Parolni kiritish majburiy.",
        },
        widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Parol',
            'autocomplete': 'off',
        })
    )

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Ismingizni kiriting'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Familiyangizni kiriting'}),
        }