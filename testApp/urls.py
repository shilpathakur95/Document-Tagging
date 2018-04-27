from django.urls import path
from . import views
from . import classviews


urlpatterns = [
    path('home', views.index, name='index'),
    path('upload',views.model_form_upload, name='load'),
    path('test', views.enter_text, name='enter_text'),
    path('topics',views.view_topics),
    #path('topics/(?P<pk>[0-9]+)/update/$',classviews.topicupdateview.as_view()),
    #path('topics/(?P<pk>[0-9]+)/delete/$',classviews.topicdeleteview.as_view()),
]