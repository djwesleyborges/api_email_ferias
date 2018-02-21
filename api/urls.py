from django.conf.urls import url
from api.views import RecursoListView, RecusoView

urlpatterns = [
    url(r'^api/$', RecursoListView.as_view(), name='recurso'),
    #url(r'^api/(?P<pk>[0-9]+)/$', RecusoView.as_view(), name='get_recurso'),
    url(r'^api/(?P<data_json>.+)/$', RecusoView.as_view()),
]
