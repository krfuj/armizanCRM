from django.urls import path, include
from django.urls import re_path as url
from . import views

app_name = "leads"

urlpatterns =[
    path('', views.landing_page, name='landing_page'), 
    path('lead_list', views.lead_list, name='lead_list'),
    path('<int:pk>/', views.lead_detail, name='lead_detail'),
    path('update/<int:pk>/',views.lead_update, name='lead_update'),
    path('delete/<int:pk>', views.lead_delete, name='lead_delete'),
    path('create/', views.lead_create, name='lead_create' ),
]

