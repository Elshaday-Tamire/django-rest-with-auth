from django.shortcuts import render

from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class CarsViewset(APIView):
    def get(self, request, id=None):
        if id:
            try:
                item = get_object_or_404(models.Cars, id=id)
                response={"carName":item.car_name,"message":"cool"}
                #serializer = serializers.CarsSerializer(item)
                return Response(response, status=status.HTTP_200_OK)
            except Http404:
                return Response({"status": "error", "message": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

        items = models.Cars.objects.all()
        #serializer = serializers.CarsSerializer(items, many=True)
        response=[{"carName":item.car_name,"message":"cool"} for item in items]
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request):
        if isinstance(request.data, list):
            serializer = serializers.CarsSerializer(data=request.data, many=True)
        else:
            serializer = serializers.CarsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "message": "success fully saved"}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        item = models.Cars.objects.get(id=id)
        serializer = serializers.CarsSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        item = models.Cars.objects.filter(id=id)
        print(item)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
