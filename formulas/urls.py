from django.conf.urls import patterns, url
from django.views.generic import ListView
from .models import Formula

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=Formula), name='home'),
)
