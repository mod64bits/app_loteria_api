from django.views.generic import CreateView, UpdateView, FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy

from .models import User
from .forms import UserAdminCreationForm


class HomeUserView(LoginRequiredMixin, TemplateView):
    template_name = 'users/home_user.html'


class RegisterView(CreateView):
    form_class = UserAdminCreationForm
    template_name = 'accounts/register.html'
    model = User
    success_url = reverse_lazy('login')


# class UpdateUserView(LoginRequiredMixin, UpdateView):
#
#     model = User
#     fields = ['username', 'name', 'email']
#     template_name = 'users/update_user.html'
#     success_url = reverse_lazy('users:user_home')
#
#     def get_object(self):
#         return self.request.user
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['profileForm'] = ProfileForm



class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'users/update_password.html'
    success_url = reverse_lazy('users:user_home')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(UpdatePasswordView, self).form_valid(form)