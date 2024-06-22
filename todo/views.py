from django.shortcuts import render
from rest_framework import permissions, viewsets
from .serializers import TodoViewSet

from todo.models import Todo

# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoViewSet
    permission_classes = [] # permissions.IsAuthenticated