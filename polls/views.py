from rest_framework.views import APIView
from .models import StudentModel
from .serializers import StudentSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_201_CREATED

class AllStudentView(APIView):
    def get(self,request,*args,**kwargs):
        all_students = StudentModel.objects.all()
        serializer= StudentSerializer(all_students,many=True)
        return Response(serializer.data)

class DetailStudentView(APIView):
    def get(self,request,*args,**kwargs):
        student = get_object_or_404( StudentModel, id=kwargs['student_id'])
        serializer = StudentSerializer(student)
        return Response(serializer.data)

class GetByEmailStudentView(APIView):
    def get(self,request,*args,**kwargs):
        student = get_object_or_404(StudentModel,email=kwargs['email'])
        serializer = StudentSerializer(student)
        return Response(serializer.data)

class CreateStudetView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        
        return Response(serializer.errors)

class UpdateStudentView(APIView):
    def patch(self,request,*args,**kwargs):
        student = get_object_or_404(StudentModel,id=kwargs['student_id'])
        
        serializer =  StudentSerializer(student,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DeleteStudentView(APIView):
    def delete(self,request,*args,**kwargs):
        student = get_object_or_404(StudentModel,id=kwargs['student_id'])
        student.delete()
        return Response({'msg':'deleted'})