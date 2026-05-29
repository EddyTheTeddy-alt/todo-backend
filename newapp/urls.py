from django.urls import path
from . import views
urlpatterns = [


    path('', views.task_list),    
    path('login/', views.login),
    path('register/', views.register),
    path('create/', views.task_create),
    path('update/<int:pk>/', views.task_update),
    path('partial-update/<int:pk>/', views.task_partial_update),
    path('delete/<int:pk>/', views.task_delete),
    path('login/', views.login),
    path('register/', views.register)
]