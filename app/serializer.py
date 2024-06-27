from typing import ClassVar

from rest_framework import serializers

from app.models import URL


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields: ClassVar = ['id', 'original_url', 'slug', 'created_at']
