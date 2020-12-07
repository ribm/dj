from django.shortcuts import render
from .models import Employee
from .serializers import EmployeESerializers

# Create your views here.

from django.views.generic import View
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView


class EmployeeCBV(APIView):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        print("hiii")
        pdata=JSONParser().parse(stream)
        print(pdata)
        id=pdata.get('id',None)
        if id is not None:
            emp=Employee.objects.get(id=id)
            serializer=EmployeESerializers(emp)
            print(serializer.data)
            json_data=JSONRenderer().render(serializer.data)
            print((type(json_data)))
            return Response({"j":"g"})
        qs=Employee.objects.all()
        serializer = EmployeESerializers(qs)
        json_data = JSONRenderer(serializer.data)
        return HttpResponse(json_data, content_type='/application/json')
    def post(self,request,*args,**kwargs):
        data=request.body
        data=io.BytesIO(data)
        data=JSONParser().parse(data)
        serializer=EmployeESerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            msg={"msg":"created"}
            return HttpResponse(msg,content_type='/application/json')
        data=JSONRenderer().render(serializer.errors)
        return HttpResponse(data, content_type='/application/json')
    def put(self,request,*args,**kwargs):
        data=request.body
        data=io.BytesIO(data)
        data=JSONParser().parse(data)
        serializer=EmployeESerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            msg={"msg":"created"}
            return HttpResponse(msg,content_type='/application/json')
        data=JSONRenderer().render(serializer.errors)
        return HttpResponse(data, content_type='/application/json')

    def delete(self,request,*args,**kwargs):
        data=request.body
        data=io.BytesIO(data)
        data=JSONParser().parse(data)
        print(data.get('id'))
        emp=Employee.objects.get(id=data.get('id'))
        emp.delete()


        msg={"msg":"deleted"}
        msg=JSONRenderer().render(msg)
        return HttpResponse(msg,content_type='/application/json')







