from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^/solutions/$', views.solutions_page, name='solutions'),
    url(r'^/tutorials/$', views.tutorials_page, name='tutorials'),
    url(r'^/about/$', views.about_page, name='about'),
    url(r'^/solution_detail/(?P<pk>\d+)/$', views.solutions_detail, name='solution_detail'),
    url(r'^/tutorial_detail/(?P<pk>\d+)/$', views.tutorials_detail, name='tutorial_detail'),
 ]
