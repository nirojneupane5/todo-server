from django.shortcuts import render
import json
from .serializer import TodoSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def todo(request):
    if request.method == "POST":
        data=json.loads(request.body)
        serializer=TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"msg":"Todo inserted successfully"}, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)