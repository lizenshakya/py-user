from django.urls import path
from . import views

urlpatterns = [
    path('', views.getUsers),
    path('create', views.addUsers),
    path('read/<str:pk>', views.getUser),
    path('update/<str:pk>', views.updateUsers),
    path('delete/<str:pk>', views.deleteUsers),
]