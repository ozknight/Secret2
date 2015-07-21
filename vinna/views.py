from django.views import generic


class HomepageView(generic.TemplateView):
    template_name = 'Homepage_View.html'

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context['page_title'] = 'Welcome To Vinna'
        return context
