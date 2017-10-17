from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView


from django.contrib.auth.views import LoginView, LogoutView

from menus.views import HomeView
from profiles.views import ProfileFollowToggle, RegisterView, activate_user_view

from menus.views import (
    #ItemCreateView,
    #ItemDetailView,
    #ItemListView,
    ItemUpdateView,
)

urlpatterns = [
    #url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    #url(r'^$', HomeView.as_view(), name='home'),
    url(r'^$', TemplateView.as_view(template_name='landing.html'), name='home'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^activate/(?P<code>[a-z0-9].*)/$', activate_user_view, name='activate'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^profile-follow/$', ProfileFollowToggle.as_view(), name='follow'),
    url(r'^u/', include('profiles.urls', namespace='profiles')),
    url(r'^items/', include('menus.urls', namespace='menus')),
    url(r'^restaurants/', include('restaurants.urls', namespace='restaurants')),
    url(r'^genre/$', TemplateView.as_view(template_name='genre.html'), name='genre'),
    url(r'^lorem/$', TemplateView.as_view(template_name='lorem.html'), name='lorem'),
    url(r'^ipsum/$', TemplateView.as_view(template_name='ipsum.html'), name='ipsum'),
    url(r'^(?P<slug>[\w-]+)/$', ItemUpdateView.as_view(), name='detail'),
    #url(r'^reset-password/$', password_reset, name='reset_password'),
]
