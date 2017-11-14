from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^sothana/?$', views.sothana, name='sothana'),
	url(r'^study/?$', views.study, name='study'),
	url(r'^activity/?$', views.activity, name='activity'),
	url(r'^reward/?$', views.reward, name='reward'),
	url(r'^tarlent/?$', views.tarlent, name='tarlent'),
]
