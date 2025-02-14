from django.shortcuts import render
import json
from .serializer import TodoSerializer
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import Todo
from django.middleware.csrf import get_token
from django.http import JsonResponse


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def todo(request, pk=None):
    if request.method == "POST":
        data = json.loads(request.body)
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"msg": "Todo inserted successfully"}, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
        
    elif request.method == "GET":
        idOfUser_fk = request.GET.get('idOfUser_fk')  
        if idOfUser_fk:
            todos = Todo.objects.filter(idOfUser_fk=idOfUser_fk)
        else:
            todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    
    elif request.method == "PUT":
        data = json.loads(request.body)
        try:
            todo = Todo.objects.get(id=pk)
        except Todo.DoesNotExist:
            return JsonResponse({'error': 'Todo not found'}, status=404)
        serializer = TodoSerializer(todo, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"msg": "Todo updated successfully"})
        else:
            return JsonResponse(serializer.errors, status=400)
        
    elif request.method == "DELETE":
        try:
            todo = Todo.objects.get(id=pk)
        except Todo.DoesNotExist:
            return JsonResponse({'error': 'Todo not found'}, status=404)

        todo.delete()
        return JsonResponse({"msg": "Todo deleted successfully"}, status=204)
    
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})