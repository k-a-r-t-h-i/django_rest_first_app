from http.client import OK
from telnetlib import STATUS
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .serializers import BookSerializer
from .models import Book
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# rest_framework_simplejwt module has to be installed separately using pip install djangorestframework_simplejwt
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework_simplejwt.authentication import JWTAuthentication

class BookAPIView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class BookDetails(APIView):

    def get(self, request, id):
        book = get_object_or_404(Book, id = id)
        serializer = BookSerializer(book, many = False)
        return Response(serializer.data)
        
        # except Book.DoesNotExist:
        #     return HttpResponse(status = status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        book = get_object_or_404(Book, id = id)
        serializer = BookSerializer(book, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id):
        book = get_object_or_404(Book, id = id)
        book.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    serializer_class = BookSerializer
    queryset = Book.objects.all()

    #lookup_field = 'id' when anyother name other than pk is used

    def get(self, request, pk = None):
        return self.retrieve(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

    
class BookViewSet(viewsets.ViewSet):
    def list(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many = True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BookSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self, request, pk=None):   #if id is used lookup_field must be used
        book = get_object_or_404(Book, id = pk)
        serializer = BookSerializer(book, many = False)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        book = get_object_or_404(Book, id = pk)
        serializer = BookSerializer(book, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class BookModelViewSet(viewsets.ModelViewSet):
    
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]




# @api_view(['GET'])
# def get_data(request):
#     books = Book.objects.all()
#     serialized_response = BookSerializer(books, many = True)
#     return Response(serialized_response.data)

# @api_view(['GET'])
# def get_data_filter(request, id):
#     books = Book.objects.get(id = id)
#     serialized_response = BookSerializer(books, many = False)
#     return Response(serialized_response.data)
# 
# #yet to learn tokens