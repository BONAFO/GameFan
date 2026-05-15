from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignUpForm(forms.Form):

    nickname = forms.CharField(
        label="Apodo",
        min_length=4,
        max_length=16,
        widget=forms.TextInput(
            attrs={
                "class": "w-full rounded-lg bg-zinc-900 border border-zinc-700 px-4 py-3 text-white focus:outline-none focus:border-primary",
                "placeholder": "Ingresa tu apodo",
            }
        ),
        required=True,
    )

    email = forms.EmailField(
        max_length=100,
        label="Correo Electrónico",
        widget=forms.EmailInput(
            attrs={
                "class": "w-full rounded-lg bg-zinc-900 border border-zinc-700 px-4 py-3 text-white focus:outline-none focus:border-primary",
                "placeholder": "Ingresa tu email",
            }
        ),
        required=True,
    )

    password = forms.CharField(
        label="Contraseña",
        min_length=8,
        max_length=32,
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full rounded-lg bg-zinc-900 border border-zinc-700 px-4 py-3 text-white focus:outline-none focus:border-primary",
                "placeholder": "Ingresa tu contraseña",
            }
        ),
        required=True,
    )

    repeat_password = forms.CharField(
        label="Repetir Contraseña",
        min_length=8,
        max_length=32,
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full rounded-lg bg-zinc-900 border border-zinc-700 px-4 py-3 text-white focus:outline-none focus:border-primary",
                "placeholder": "Repite tu contraseña",
            }
        ),
        required=True,
    )

    is_adult = forms.ChoiceField(
        label="",
        choices=[
            ("no", "Soy menor de 18"),
            ("yes", "Soy mayor de 18"),
        ],
        initial="no",
        widget=forms.RadioSelect(attrs={}),
        required=True,
    )

    def clean_nickname(self):
        nickname = self.cleaned_data["nickname"]

        print(User.objects.filter(username=nickname).exists())

        if User.objects.filter(username=nickname).exists():
            raise ValidationError("El nickname ya está en uso.")

        return nickname

    def clean_email(self):

        email = self.cleaned_data["email"]

        if User.objects.filter(email=email).exists():
            raise ValidationError("El email ya está en uso.")

        return email

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")

        if password != repeat_password:
            raise ValidationError("Las contraseñas no coinciden.")

        return cleaned_data


class LoginForm(forms.Form):

    identifier = forms.CharField(
        label="Usuario o Email",
        widget=forms.TextInput(
            attrs={
                "class": "w-full rounded-lg bg-zinc-900 border border-zinc-700 px-4 py-3 text-white focus:outline-none focus:border-primary",
                "placeholder": "Usuario o Email",
            }
        ),
    )

    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full rounded-lg bg-zinc-900 border border-zinc-700 px-4 py-3 text-white focus:outline-none focus:border-primary",
                "placeholder": "Contraseña",
            }
        ),
    )
