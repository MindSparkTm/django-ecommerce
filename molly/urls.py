from django.conf.urls import include, url
from django.urls import path
from .views import hello

app_name = 'todos'
# this is DRF router for REST API viewsets

# register REST API endpoints with DRF router
urlpatterns =[
  path('hello',hello,name='hello'),
]
