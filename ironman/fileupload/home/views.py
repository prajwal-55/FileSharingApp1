from tkinter import E
from.serializers import *
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

# Create your views here.

def home(request):
    return render(request,'home.html')

def download(request,uid):
    return render(request,'download.html',context={'uid' : uid })

class HandleFileUpload(APIView):
    parser_classes = [MultiPartParser]
    def post(self,request):
        try:
            data = request.data
            
            serializers = FileListSerializer(data = data)
            
            if serializers.is_valid():
                serializers.save()
                return Response({
                    'status' : 200,
                    'message' : 'files upload suceesfully',
                    'data' : serializers.data
                })
                
            return Response({
                'status' : '400',
                'message':'something went wrong',
                'data' : serializers.errors
            })
               
        except Exception as e:
            print(e)

