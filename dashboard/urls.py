# dashboard/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('datapoints/', views.DataPointList.as_view(), name='datapoint-list'),
]
