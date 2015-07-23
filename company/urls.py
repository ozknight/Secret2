from django.conf.urls import urls
from .views import CompanyCreateView

urlpatterns = (
    url(r'^create/$', CompanyCreateView, name='create'),
)
