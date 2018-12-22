from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('relevence/', views.relevence , name='relevence'),
    path('cosrelevence/', views.cosrelevence , name='cosrelevence'),    
    path('',views.preprocess, name='preprocess'),
]