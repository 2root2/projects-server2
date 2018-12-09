
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework import generics
from django.shortcuts import render
from .models import Projects, Forms, Users
from .serializers import ProjectSerializer, FormSerializer, UserSerializer
# Create your views here.

class ListProjectsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer

    # @validate_request_data
    def post(self, request, *args, **kwargs):
        a_project= Projects.objects.create(
            project=request.data["project"],
            description=request.data["description"],
            # forms=request.data["forms"]
            # profile = Users.set(request.data["profile"])
        )
        return Response(
            data=ProjectSerializer(a_project).data,
            status=status.HTTP_201_CREATED
        )

class ListFormsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Forms.objects.all()
    serializer_class = FormSerializer

    # @validate_request_data
    def post(self, request, *args, **kwargs):
        a_form= Forms.objects.create(
            name=request.data["name"],
            shape=request.data["shape"]
        )
        return Response(
            data=FormSerializer(a_form).data,
            status=status.HTTP_201_CREATED
        )

class ListUsersView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    # @validate_request_data
    def post(self, request, *args, **kwargs):
        a_user= Users.objects.create(
            firstname=request.data["firstname"],
            lastname=request.data["lastname"],
            age=request.data["age"],
            imageUrl=request.data["imageUrl"]
        )
        return Response(
            data=UserSerializer(a_user).data,
            status=status.HTTP_201_CREATED
        )