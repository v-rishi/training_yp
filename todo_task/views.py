from django.shortcuts import render
from todo_task.models import Task, Comment
from django.shortcuts import get_object_or_404
from todo_task.serializers import TaskSerializer, CommentSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.response import Response


class TopFiveMixin:
    @action(detail = False, methods = ['get'])
    def top_five(self, request):
        queryset = self.get_queryset()[:5]
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)


class TaskViewSet(viewsets.ModelViewSet, TopFiveMixin):
    """
    A viewset for viewing and editing Task instances.
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    

class CommentViewSet(viewsets.ModelViewSet, TopFiveMixin):
    """
    A viewset for viewing and editing Comment instances.
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.prefetch_related('task').all()