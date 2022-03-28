from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import api
from .serializers import AuthorSerializer
from News.models import Author

# Create your views here.
#Author api
class AuthorList(APIView):
    def get(self, request, id=None, format=None):
        id = id
        if id is not None:
            author=Author.objects.get(id=id)
            serializer=AuthorSerializer(author)
            return Response(serializer.data)
        author=Author.objects.all()
        serializer=AuthorSerializer(author,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer=AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None, format=None):
        id = id
        author=Author.objects.get(id=id)
        serializer=AuthorSerializer(author,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Date updated successfull'})
        return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)

    def patch(self, request, id,format=None):
        id = id
        author=Author.objects.get(id=id)
        serializer=AuthorSerializer(Author,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Update'})
        return Response(serializer.errors)


    def delete(self, request, id, format=None):
        id = id
        author=Author.objects.get(id=id)
        author.delete()
        return Response({'msg':'Data Deleted'})