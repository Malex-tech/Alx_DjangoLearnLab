from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()
    target = serializers.StringRelatedField()

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'target', 'timestamp', 'read']
        read_only_fields = ['recipient', 'actor', 'verb', 'target', 'timestamp', 'read']
