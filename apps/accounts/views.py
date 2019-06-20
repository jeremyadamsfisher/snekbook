from django.views import generic
from django.urls import reverse_lazy
from . import forms


class Register(generic.CreateView):  # pylint: disable=too-many-ancestors
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
