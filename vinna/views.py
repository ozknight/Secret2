from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic


class HomepageView(generic.TemplateView):
    template_name = 'Homepage_View.html'

    def get(self, request, *args, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        print request.user.profile.is_Profile_Set()
        if request.user.is_authenticated():
            context['page_title'] = 'Dashboard'
            if not request.user.profile.is_Profile_Set():
                return HttpResponseRedirect(
                    reverse(
                        'profile:create',
                        args=(
                            request.user.id,
                        )
                    )
                )
        else:
            context['page_title'] = 'Welcome To Vinna'
        return render(request, self.template_name, context)
