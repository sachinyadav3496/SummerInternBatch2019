from rest_framework import serializers
from .models import AddBlog


class AddBlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = AddBlog
        fields = ['title','post']
        #fields = __all__ #for all fields