from rest_framework import serializers
from .models import Actor, Movie, Review


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview',)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content',)


class ActorDetailSerializerToMovie(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('name',)


class MovieDetailSerializerTitle(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',)


class ActorDetailSerializer(serializers.ModelSerializer):
    movies = MovieDetailSerializerTitle(many=True, read_only=True)
    class Meta:
        model = Actor
        fields = '__all__'


class MovieDetailSerializer(serializers.ModelSerializer):
    actors = ActorDetailSerializerToMovie(many=True, read_only = True)
    review_set = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'movie', 'title', 'content',)
    movie = MovieDetailSerializerTitle(read_only=True)

