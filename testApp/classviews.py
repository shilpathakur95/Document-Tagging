from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from testApp.models import *
from django.template.loader import get_template
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

class topicupdateview(UpdateView):
    model = Topics
    fields = ('topic','cutoff_25','cutoff_50','cutoff_75','data')

    def get_success_url(self):
        return reverse("topics")

    def get_object(self, queryset=None):
        topic = self.kwargs.get('pk')
        result = Topics.objects.all().get(topic=topic)
        return result

class topicdeleteview(DeleteView):
    model = Topics
    fields = ('topic','cutoff_25','cutoff_50','cutoff_75','data')

    def get_success_url(self):
        return reverse("topics")

    def get_object(self, queryset=None):
        topic = self.kwargs.get('pk')
        result = Topics.objects.all().get(topic=topic)
        return result

