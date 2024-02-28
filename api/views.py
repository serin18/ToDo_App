# Create your views here.
from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from reminder.models import Task
from api.serializer import task_serializer
from rest_framework.response import Response
from rest_framework import authentication,permissions
# Create your views here.

class Taskviewsetview(ViewSet):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]


    def list(self,request,*args,**kwargs):
        qs=Task.objects.all()
        serializer=task_serializer(qs,many=True)
        return Response(data=serializer.data)
    
    def create(self,request,*args,**kwargs):
        serializers=task_serializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data)
        return Response(serializers.errors)
    
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Task.objects.get(id=id)
        if qs.user==request.user:
            qs.delete()
            return Response()
        return Response("deleted successfully")
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Task.objects.get(id=id)
        serializers=task_serializer(qs)
        return Response(serializers.data)
    
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Task.objects.get(id=id)
        serializers=task_serializer(data=request.data,instance=qs)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data)
        return Response(serializers.errors)