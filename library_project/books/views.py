from rest_framework import generics
from .serializers import BookSerializer
from .models import Book


class BookApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer