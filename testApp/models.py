from __future__ import unicode_literals
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from django.db import models

class OverwriteStorage(FileSystemStorage):

    def get_available_name(self, name,max_length):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_DIR, name))
        return name

class Topics(models.Model):
    topic = models.CharField(max_length=100,primary_key=True)
    cutoff_25 = models.FloatField()
    cutoff_50 = models.FloatField()
    cutoff_75  = models.FloatField()
    data = models.FileField(upload_to='uploads',storage=OverwriteStorage())

    def __unicode__(self):
        return self.topic

    class Meta:
        ordering = ('topic',)


class Input(models.Model):
    TYPE_CHOICES = (
        ('U', 'Url'),
        ('T', 'Text')
    )
    input_class = models.ForeignKey(Topics,on_delete=models.CASCADE)
    input_content_type = models.CharField(max_length=10,choices=TYPE_CHOICES,default='Text')
    input_content = models.TextField(max_length=10000)
    input_datetime = models.DateTimeField(auto_now=True)
    predicted_class = models.CharField(max_length=500)
    confidence_score = models.FloatField()
    prediction_machine_id = models.FloatField()
    prediction_machine_version = models.FloatField()
    prediction_machine_verison_deploy_date = models.DateField()

    def __unicode__(self):
        return '%s %s %s' % (self.input_class, self.input_content_type,self.input_content)

    class Meta:
        ordering = ('input_class',)


