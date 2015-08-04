from django.conf.urls import url
from .views import *

urlpatterns = (
    url(
        r'^$',
        BaseView.as_view(),
        name='home'
    ),
)
