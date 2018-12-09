from rest_framework import serializers
from .models import Projects, Forms, Users


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ("id", "project", "description", "createdon", "lastupdated", "formsubmitted", "total", "count")
        # fields = ("project", "descreption", "total", "formsubmitted", "createdon")

class FormSerializer(serializers.ModelSerializer):
    class Meta:
	    model = Forms
	    fields = ("id","name", "shape")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
	    model = Users
	    fields = ("id","firstname", "lastname", "age", "imageUrl")
