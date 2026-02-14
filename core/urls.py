from django.urls import path
from . import views

urlpatterns = [path('pickup/',views.create_pickup_request,name = 'create_pickup'),path('dashboard/',views.dashboard,name ='dashboard'),]