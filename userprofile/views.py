from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from .forms import ProfileCreateForm


class ProfileDetailView(generic.TemplateView):
    template_name = 'Profile_Detail_View.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        context['page_title'] = "Profile"
        return context


class ProfileUpdateView(generic.UpdateView):
    template_name = 'Profile_Update_View.html'
    success_url = 'profile:view'


class ProfileCreateView(generic.CreateView):
    form_class = ProfileCreateForm
    template_name = 'Profile_Create_View.html'
    success_url = 'profile:view'

    def get_context_data(self, **kwargs):
        context = super(ProfileCreateView, self).get_context_data(**kwargs)
        context['page_title'] = 'Setup Profile'
        return context

    def get_queryset(self):
        return User.objects.get(pk=self.request.user.id)
