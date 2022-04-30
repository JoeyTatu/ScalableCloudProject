from django.urls import path

from . import views

app_name = 'rekognitions'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:key>/', views.show, name='show')
]
