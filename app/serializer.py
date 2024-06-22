from rest_framework import serializers

from app.models import URL


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = '__all__'
