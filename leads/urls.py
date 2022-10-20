from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.lead_list, name='lead_list'),

]