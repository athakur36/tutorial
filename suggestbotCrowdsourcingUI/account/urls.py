from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home),
    url(r'^about/$', views.about),
    url(r'^help/$', views.help),
    url(r'^introduction1/$', views.introduction1),
    url(r'^task/$', views.task),
    url(r'^questionaire/$', views.get),
    url(r'^intention/$',views.getIntention),
    url(r'^thankyou/$', views.thankyou),
    url(r'^feedback/$', views.feedback),
]
