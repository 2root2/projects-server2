from django.urls import path
from .views import ListProjectsView, ListFormsView, ListUsersView


urlpatterns = [
    path('projects/', ListProjectsView.as_view(), name="projects-all"),
    path('forms/', ListFormsView.as_view(), name="forms-all"),
    path('users/', ListUsersView.as_view(), name="users-all")
]