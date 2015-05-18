from django.conf.urls import url 
from polls import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),      # /polls/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),       # /polls/5/
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),     # /polls/5/results/
    url(r'^(?P<pk>\d+)/vote/$', views.vote, name='vote'),      # /polls/5/vote/
]
