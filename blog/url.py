from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r"^(?P<pk>[0-9]+)/tag/$", views.blogTag, name='tag'),
    url(r'^about$',views.about, name='about'),
    url(r"^blog/(?P<pk>[0-9]+)$", views.blogPost, name='blogpost')

]