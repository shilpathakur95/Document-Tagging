from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name='index'),
    path('upload',views.model_form_upload, name='load'),
    path('test', views.enter_text, name='enter_text')
]