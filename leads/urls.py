from django.urls import path, include
from django.urls import re_path as url
from . import views

app_name = "leads"

urlpatterns =[
    path('', views.lead_list, name='lead_list'),
    path('<int:pk>/', views.lead_detail, name='lead_detail'),
    path('create/', views.lead_create, name='lead_create' )
]

