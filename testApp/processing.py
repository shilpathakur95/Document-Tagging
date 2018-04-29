import urllib
from bs4 import BeautifulSoup
import csv
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testProject.settings")
django.setup()
import rake
from testApp.models import *
import numpy as np

from nltk.stem.porter import *
stemmer=PorterStemmer()




def execute_rake(text):
    stoppath = "StemStoplist.txt"
    rake_object = rake.Rake(stoppath,max_words_length=3)


    keywords = rake_object.run(text)
    max_value = max(keywords,key=lambda item:item[1])[1]
    normalized_keywords = [(word[0], word[1]/max_value) for word in keywords]
    normalized_keywords = sorted(normalized_keywords,key=lambda x: x[1],reverse=True)

    return normalized_keywords

def getSimilarity(dict1,dict2):
    all_phrase_list=[]
    for key in dict1:
        all_phrase_list.append(key)
    for key in dict2:
        all_phrase_list.append(key)
    vector1 = np.zeros(len(all_phrase_list), dtype=np.object)
    vector2 = np.zeros(len(all_phrase_list), dtype=np.object)
    i =0
    for (key) in all_phrase_list:
        vector1[i]=dict1.get(key,0)
        vector2[i]=dict2.get(key,0)
        i = i +1
    return cos_sim(vector1,vector2)

def cos_sim(v1,v2):
    print(v1)
    dot_product = np.dot(v1,v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    return dot_product / (norm_v1 * norm_v2)

def stem_text(text):
    final_text=""
    for line in text.splitlines():
        singles = []
        for word in re.findall(r"[\w']+|[.,!?;]", line):
            singles.append(stemmer.stem(word))

        final_text = final_text + ' '.join(singles) + "\n"
    return final_text


def get_probability(text,topic):
    text=stem_text(text)
    result={}
    base = Topics.objects.all()
    passed =""
    i=1
    for b in base:

        topic=b.topic
        cutoff_25=b.cutoff_25
        cutoff_75=b.cutoff_75
        cutoff_50=b.cutoff_50
        csv_file = csv.DictReader(b.data.open(mode='r'))

        base_keywords = [(line['phrase'],float(line['score'])) for line in csv_file]
        text_keywords=execute_rake(text)

        sim=getSimilarity(dict(base_keywords),dict(text_keywords))
        if sim>=cutoff_25:
            result[topic] = (1,sim)
            passed= passed + topic + ","
        else:
            result[topic] = (0, sim)
    return result,dict(text_keywords),passed

#print(get_probability("Java is cool","C++ programming"))