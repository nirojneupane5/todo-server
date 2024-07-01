from django.shortcuts import render
import json
from .serializer import TodoSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Todo

# Create your views here.
@csrf_exempt
def todo(request,pk=None):
    if request.method == "POST":
        data=json.loads(request.body)
        serializer=TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"msg":"Todo inserted successfully"}, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
        
    elif request.method=="GET":
        todos=Todo.objects.all()
        serializer=TodoSerializer(todos, many=True)
        return JsonResponse(serializer.data,safe=False,status=200)
    
    elif request.method=="PUT":
        data=json.loads(request.body)
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
        
    elif request.method=="DELETE":
        try:
            todo = Todo.objects.get(id=pk)
        except Todo.DoesNotExist:
            return JsonResponse({'error': 'Todo not found'}, status=404)

        todo.delete()
        return JsonResponse({"msg": "Todo deleted successfully"}, status=204)
    
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)