from rest_framework import serializers
from todo.models import Todo


class TodoViewSet(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'Title', 'Description', 'created_at']