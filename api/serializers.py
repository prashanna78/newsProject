from rest_framework import serializers
from News.models import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=['name','address','email','image']
        