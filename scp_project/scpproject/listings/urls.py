from django.urls import path

from . import views

app_name = 'listings'
urlpatterns = [
    path('', views.index, name='index'), 
    path('<int:listing_id>/', views.show, name='show'),
]