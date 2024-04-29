from rest_framework import serializers
from .models import BlogPost 
from .serializerutils import transformMethodTwo
class BlogPostSerializer(serializers.ModelSerializer) :
    class Meta:
        model = BlogPost
        fields = ["id","title","content", "published_date","blogger_name","blogger_ssn","blogger_email"]


class BlogPostTransformSerializer(serializers.ModelSerializer) :
    blogger_name = serializers.SerializerMethodField()
    blogger_ssn =serializers.SerializerMethodField()
    #modification of the ssn masked in another field
    def get_blogger_name(self, obj):
         return obj.title + obj.blogger_ssn + "-0953"
    
    def get_blogger_ssn(self, obj):  
        return  transformMethodTwo(obj.blogger_ssn)
        
    class Meta:
        model = BlogPost
        fields = ["id","published_date","blogger_name","blogger_ssn","blogger_email"]