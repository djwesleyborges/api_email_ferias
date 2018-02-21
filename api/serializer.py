from rest_framework import serializers
from .models import Recurso


class RecursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recurso
        field = 1
        fields = '__all__'