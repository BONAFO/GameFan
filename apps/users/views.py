from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login

from .forms import SignUpForm
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
    
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


class LogoutView(LogoutView):
    next_page = reverse_lazy('home:home')
    