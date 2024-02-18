from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serialiazers import BookSerializer
from rest_framework.response import Response

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = []

    def list(self, request, *args, **kwargs):
        queryset = Book.objects.all().filter(status=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



# class BookAPIView(views.class CLASSNAMEViewSet(viewsets.ModelViewSet):
#     queryset = CLASSNAME.objects.all()
#     serializer_class = CLASSNAMESerializer
#     permission_classes = []


# ):

#     def get(self, request):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)

#     def post(self):
#         pass
