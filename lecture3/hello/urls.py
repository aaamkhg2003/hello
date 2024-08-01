from django.urls import path
from . import views
urlpatterns=[
  path ("", views.index, name='hello'),
  path ("ahmed", views.ahmed, name='ahmed'),
  path ("<str:name>", views.greet, name='greet')
  ]