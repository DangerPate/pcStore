from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    # 🔑 required=True на уровне поля Django
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'you@example.com'})
    )
    phone = forms.CharField(
        label='Телефон',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 (999) 123-45-67'})
    )
    password1 = forms.CharField(
        label='Пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control pe-5', 'placeholder': '••••••••', 'id': 'id_password1'})
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '••••••••'})
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'phone', 'password1', 'password2')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if CustomUser.objects.filter(phone=phone).exists():
            raise forms.ValidationError('Этот номер телефона уже зарегистрирован')
        return phone

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'you@example.com', 'autofocus': True, 'required': True})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '••••••••', 'required': True})
    )