from django.conf.urls import url
from .views import ProfileUpdateView, ProfileDetailView, ProfileCreateView


urlpatterns = (
    url(
        r'^$',
        ProfileDetailView.as_view(),
        name='view'
    ),
    url(
        r'^edit/$',
        ProfileUpdateView.as_view(),
        name='edit'
    ),
    url(
        r'^setup/(?P<pk>\d+)$',
        ProfileCreateView.as_view(),
        name='create'
    ),
)
