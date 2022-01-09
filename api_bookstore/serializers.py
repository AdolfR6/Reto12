from rest_framework import serializers
from .models import Author, Book

class AuthorSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'

class BookSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'