from django.conf.urls import url
from .import views
from django.contrib.auth.views import login,logout

urlpatterns = [
    url(r'^$', views.home),
    url(r'login/$', login, {'template_name': 'accounts/login.html'}),
    url(r'logout/$', logout, {'template_name': 'accounts/logout.html'}),
    url(r'^register/$',views.register,name='register'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^profile/edit$', views.editprofile, name='editprofile'),
    url(r'^password/$', views.change_password, name='change_password'),

]