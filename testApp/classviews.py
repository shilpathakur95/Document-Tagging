from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from testApp.models import *
from django.template.loader import get_template
from django.http import HttpResponseRedirect, HttpResponse


class topicupdateview(UpdateView):
    model = Topics
    fields = ('topic','cutoff_25','cutoff_50','cutoff_75','data')

    def get_success_url(self):
        return HttpResponseRedirect("/topics")

    def get_object(self, queryset=None):
        id = self.kwargs.get('pk')
        result = Topics.objects.all().get(id=id)
        return result

class topicdeleteview(DeleteView):
    model = Topics
    fields = ('topic','cutoff_25','cutoff_50','cutoff_75','data')

    def get_success_url(self):
        return HttpResponseRedirect("/topics")

    def get_object(self, queryset=None):
        id = self.kwargs.get('pk')
        result = Topics.objects.all().get(id=id)
        return result

