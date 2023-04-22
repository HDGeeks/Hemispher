
from rest_framework import serializers

# local imports
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'description', 'location', 'contact']
        extra_kwargs = {
            'name': {'required': True},
            'description': {'required': True},
            'location': {'required': True},
            'contact': {'required': True},
        }

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id','customer','name','description','date','location','noOfDataCollectors','budget']
        extra_kwargs = {
            'customer': {'required': True},
            'name': {'required': True},
            'description': {'required': True},
            'no_of_data_collectors': {'required': True},
            'budget': {'required': True},
        }



class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['id', 'project', 'name', 'description', 'status']
        extra_kwargs = {
            'project': {'required': True},
            'name': {'required': True},
            'description': {'required': True},
            'status': {'required': True},
        }




class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('survey', 'title', 'has_multiple_answers', 'is_dependent', 'dependent_question',
                  'is_required', 'type', 'options', 'audio_url', 'image_url', 'video_url')
        extra_kwargs = {
            'survey': {'required': True},
            'title': {'required': True},
            'has_multiple_answers': {'required': True},
            'is_dependent': {'required': True},
            'dependent_question': {'required': True},
            'is_required': {'required': True},
            'type': {'required': True},
            'options': {'required': True},
            'audio_url': {'required': True},
            'image_url': {'required': True},
            'video_url': {'required': True},
        }




class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = ('question', 'responses')
        extra_kwargs = {
            'question': {'required': True},
            'responses': {'required': True},
            #'location': {'required': True},
        }