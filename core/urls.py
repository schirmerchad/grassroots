from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url('^', include('django.contrib.auth.urls'))
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
]
