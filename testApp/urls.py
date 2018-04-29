from django.urls import path,re_path
from . import views
from . import classviews


urlpatterns = [
    path('home', views.index, name='index'),
    path('upload',views.model_form_upload, name='load'),
    path('test', views.enter_text, name='enter_text'),
    path('topics',views.view_topics, name='topics'),
    path('input',views.view_input, name='inputs'),
    re_path('topics/(?P<pk>[\w|\W]+)/update/$', classviews.topicupdateview.as_view()),
    re_path('topics/(?P<pk>[\w|\W]+)/delete/$',classviews.topicdeleteview.as_view()),
]