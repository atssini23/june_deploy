from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^login$', views.login, name = 'login'),
    url(r'^add_user$', views.add_user, name = 'add_user'),
]
