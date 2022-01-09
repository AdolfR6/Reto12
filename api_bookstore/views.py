from rest_framework import viewsets
from .serializers import AuthorSerializers, BookSerializers
from .models import Author, Book
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])

def welcome(request):
    content = {"message": "Welcome to the BookStore!"}
    return JsonResponse(content)

# Create your views here.
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializers

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializers