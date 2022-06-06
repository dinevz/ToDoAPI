from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer



class TodoListApiView(APIView):
    #List all
    def get(self, request, *args, **kwargs):
        '''
            List all todo items
        '''
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #Create todo
    
    def post(self, request, *args, **kwargs):
        
        data = {
            'task': request.data.get('task'),
            'completed': request.data.get('completed'),
        }
        
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class TodoDetailApiView(APIView):
    
    def get_todo(self, todo_id):
        try:
            return Todo.objects.get(id=todo_id)
        except Todo.DoesNotExist:
            return None
    
    #Retrieve todo
    def get(self, request, todo_id, *args, **kwargs):
        
        todo_instance = self.get_todo(todo_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = TodoSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #Update todo
    
    def put(self, request, todo_id, *args, **kwargs):
        
        todo_instance = self.get_todo(todo_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        data = {
            'task': request.data.get('task'),
            'completed': request.data.get('completed'),
        }
        
        serializer = TodoSerializer(instance=todo_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, todo_id, *args, **kwargs):
        
        todo_instance = self.get_todo(todo_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        todo_instance.delete()
        return Response(
                {"res": "Object deleted!"},
                status=status.HTTP_200_OK
            )