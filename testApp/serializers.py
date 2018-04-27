from rest_framework import serializers
from testApp.models import *

class TopicsSerializer(serializers.ModelSerializer):
    class Meta:
            model = Topics
            fields = ('topic','cutoff_25','cutoff_50','cutoff_75','data')

