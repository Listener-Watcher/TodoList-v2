from rest_framework import serializers
from todolist.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'created_at','deadline','priority','text','done')
    # def create(self, validated_data):
    #     title = validated_data.get('title', None)
    #     user = self.context.get('user')
    #     text = validated_data.get('text', None)
    #     created_at = validated_data.get('created_at', None)
    #     deadline = validated_data.get('deadline', None)
    #     priority = validated_data.get('priority', None)
    #     done = validated_data.get('done', None)
    #     return Task.objects.create(title=title,text=text, /
    #         created_at=created_at,deadline=deadline,priority=priority,done=done)
