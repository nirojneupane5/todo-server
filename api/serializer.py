from rest_framework import serializers

class TodoSerializer(serializers.Serializer):
    task_name=serializers.CharField(max_length=150)
    desc=serializers.TextField()
    status=serializers.BooleanField(default=True)