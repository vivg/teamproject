from rest_framework import serializers
from .models import Member

class TeamSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        model = Member
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'role')
