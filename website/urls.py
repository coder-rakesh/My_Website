from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^/Solutions/$', views.solutions_page, name='solutions_page'),
    url(r'^/Tutorials/$', views.tutorials_page, name='tutorials_page'),
    url(r'^/About/$', views.about_page, name='about_page'),
    url(r'^/solution_detail/(?P<pk>\d+)/$', views.solutions_detail, name='solutions_detail'),
    url(r'^/tutorial_detail/(?P<pk>\d+)/$', views.tutorials_detail, name='tutorials_detail'),
 ]
