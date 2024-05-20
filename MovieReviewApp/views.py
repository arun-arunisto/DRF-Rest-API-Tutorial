from .models import *
from .serializer import *
from rest_framework import mixins, generics

class MovieListGenericView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

#Concrete API View
class MovieCreateConcreteView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewCreateConcreteView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class MovieListConcreteView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewListConcreteView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer