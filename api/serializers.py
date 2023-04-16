from  rest_framework import serializers
from haminjory.models import Article,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


class ArticleSerializer(serializers.ModelSerializer):
    category=CategorySerializer(many=True,read_only=True)
    class Meta:
        model=Article
        fields=[
            'title',
            'slug',
            'description',
            'thumbnail',
            'publish',
            'created',
            'updated',
            'status',
            'category',
        ]
