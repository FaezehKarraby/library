from django.urls import path

from chat import views

urlpatterns =[
    path('', views.QA, name='qa'),
    path('change_seen_status/', views.change_seen_status, name='chane_seen_status'),
]