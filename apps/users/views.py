from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView

from .forms import SignUpForm , LoginForm
from apps.users.models import Profile


class SignUpView(FormView):

    template_name = 'users/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):

        user = User.objects.create_user(
            username=form.cleaned_data['nickname'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )

        Profile.objects.create(
            user=user,
            is_adult=form.cleaned_data['is_adult'] == 'yes'
        )

        login(
            self.request,
            user
        )

        return super().form_valid(form)
    



class LogoutView(LogoutView):
    next_page = reverse_lazy('home:home')


class LoginView(FormView):

    template_name = "users/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("home:home")

    def form_valid(self, form):

        identifier = form.cleaned_data["identifier"]
        password = form.cleaned_data["password"]

        user = None

        if "@" in identifier:
            
            try:
                user_obj = User.objects.get(email=identifier)
                username = user_obj.username
                user = authenticate(
                    self.request,
                    username=username,
                    password=password
                )
            except User.DoesNotExist:
                user = None

        else:

            user = authenticate(
                self.request,
                username=identifier,
                password=password
            )

        if user is None:

            form.add_error(None, "Credenciales inválidas")
            return self.form_invalid(form)

        login(self.request, user)

        return super().form_valid(form)