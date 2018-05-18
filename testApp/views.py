from django.http import HttpResponseRedirect
from testApp.forms import *
from django.shortcuts import render,redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from testApp.models import *
from django.template.loader import get_template
from django.http import HttpResponse
import rake
from bs4 import BeautifulSoup
import urllib.request
import sys
import testApp.processing as process

import re
from lxml.html.clean import Cleaner
cleaner = Cleaner()
cleaner.javascript = True # This is True because we want to activate the javascript filter
cleaner.style = True
cleaner.scripts = True
cleaner.links = True
cleaner.meta = True
cleaner.page_structure = True
cleaner.frames = True
cleaner.forms = True
cleaner.annoying_tags = True


def get_url_content(url):
    try:
        with urllib.request.urlopen(url) as page:
            text = page.read()
    except Exception as e:
        return "Couldn't load url"
    return text



def index(request):
    return HttpResponse("Hello, world. You're at the homepage.")


def model_form_upload(request):
    if request.method == 'POST':
        form = TopicsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Upload successful')
    else:
        form = TopicsForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })



def enter_text(request):
    """
      List all snippets, or create a new snippet.
      """
    template = get_template("input.html")
    template2=get_template("result.html")
    if request.method == 'POST':

        input_form = InputForm(data=request.POST)
        if request.POST.get('input_content_type') == 'U':
            text = get_url_content(request.POST.get('input_content'))
            if text == "Couldn't load url":
                return HttpResponse(text)

            raw_document = cleaner.clean_html(text)
            text = BeautifulSoup(raw_document, "lxml").text
            text = re.sub(re.compile('<.*?>'), '', text)
            text = text.replace("-","")


        else:
            text = request.POST.get('input_content')
        topic = request.POST.get('input_class')
        result,keywords,p_class = process.get_probability(text,topic)
        input_instance=input_form.save(commit=False)
        input_instance.predicted_class=p_class
        input_instance.confidence_score = result[topic][0]
        input_instance.similarity = result[topic][1]
        input_instance.prediction_machine_id=1
        input_instance.prediction_machine_version=1.0
        input_instance.prediction_machine_deploy_date='2018-04-24'
        input_instance.save()
        return HttpResponse(template2.render(context={'list': result , 'keywords': keywords,'topic':topic},
                                         request=request))
    else:
        input_form=InputForm()
    return HttpResponse(template.render(context={'input_form': input_form},
                                         request=request))

def view_topics(request):
    list = Topics.objects.all()
    template=get_template("list.html")
    return HttpResponse(template.render(context={'list': list},
                                        request=request))

def view_input(request):
    list_input = Input.objects.all()
    template = get_template("input_list.html")
    return HttpResponse(template.render(context={'list': list_input},
                                        request=request))