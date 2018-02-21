from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Recurso
from .serializer import RecursoSerializer
from rest_framework import generics


class RecursoListView(APIView):
    serializer_class = RecursoSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Recurso.objects.all(), many=True)
        return Response(serializer.data)


# class RecusoView(APIView):
#
#     def get(self, request, pk, format=None):
#         recurso = Recurso.objects.get(pk=pk)
#         serializer = RecursoSerializer(recurso)
#         return Response(serializer.data)


class RecusoView(generics.ListAPIView):
    serializer_class = RecursoSerializer

    def get_queryset(self):
        data_json = self.kwargs['data_json']
        return Recurso.objects.filter(data_json=data_json)