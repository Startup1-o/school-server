from register_school.models import Teams
from rest_framework import serializers


class TeamsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teams
        fields = ("name", "description")
