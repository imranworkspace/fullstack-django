from django.shortcuts import render
from .models import StudentModel
from .serializers import StudentSerializers
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
# Create your views here.
class StudentView(viewsets.ViewSet):
    def list(self,request):
        all = StudentModel.objects.all()
        serializer = StudentSerializers(all,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        s_id=pk
        if s_id is not None:
            stu = StudentModel.objects.get(s_id=s_id)
            serializers = StudentSerializers(stu)
            return Response(serializers.data)
    
    def create(self,request):
        serializers = StudentSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk):
        s_id=pk
        if s_id is not None:
            stu = StudentModel.objects.get(s_id=s_id)
            serializer = StudentSerializers(stu,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'updated'},status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        s_id=pk
        if s_id is not None:
            stu = StudentModel.objects.get(s_id=s_id)
            serializer = StudentSerializers(stu,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'partially updated'},status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk):
        s_id=pk
        stu = StudentModel.objects.get(pk=s_id)
        stu.delete()
        return Response({'msg':f'{id} record deleted'},status=status.HTTP_200_OK)
        # return Response({'msg':'something wrong'},status=status.HTTP_400_BAD_REQUEST)