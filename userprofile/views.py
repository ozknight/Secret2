from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views import generic
from django.http import Http404
from .forms import ProfileCreateForm
from .models import Profile


class ProfileDetailView(generic.TemplateView):
    template_name = 'Profile_Detail_View.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        context['page_title'] = "Profile"
        context['body_background'] = "green lighten-2"
        return context


class ProfileUpdateView(generic.UpdateView):
    template_name = 'Profile_Update_View.html'
    success_url = '/profile/view'


class ProfileCreateView(generic.UpdateView):

    model = Profile
    form_class = ProfileCreateForm
    template_name = 'Profile_Create_View.html'
    success_url = '/profile/view/'

    def get_context_data(self, **kwargs):
        context = super(ProfileCreateView, self).get_context_data(**kwargs)
        context['page_title'] = 'Setup Profile'
        context['body_background'] = "green lighten-2"
        if self.request.user != context['profile'].user:
            raise Http404('Not Authorized Personel')
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        if form.is_valid():
            messages.add_message(
                self.request, messages.INFO,
                'You\'ve Successfully Setup your account!'
            )
        return super(ProfileCreateView, self).form_valid(form)
