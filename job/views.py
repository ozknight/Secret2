from django.views import generic


class BaseView(generic.TemplateView):

    '''
    Homepage For Jobs
    '''
    template_name = 'BaseView.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        context['page_title'] = 'Job List'
        context['nav_color'] = "green ligthen-2"
        context['page_active'] = 'job'
        return context
