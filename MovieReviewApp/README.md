### Create API View
This view used for create-only endpoints (This means it's only for `post` method) this is the first Concrete view class that we're going to look. So, open your `views.py` file and type the below code.

```python
#Concrete API View
class MovieCreateConcreteView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
```
This is the only code that we want to provide for the post method (this is only for `post` method `get` method is not allowed in this ViewClass)

### List API View
This view is used for read-only endpoints (This means it's only for `get` method)

```python
class MovieListConcreteView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
```
The main usage of this type views is that we can simply create an application with minimum lines of code.

### Retrieve API View
This view is used for getting (read-only) single model instances

```python
class MovieDetailConcreteView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
```
You dont need to mention any keys to fetch it will automatically fetch the elements from that key you gave it in url or you can add a look up field using the `lookup_field` object

### Destroy API View
This view is used to delete an element

```python
class MovieDeleteConcreteView(generics.DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
```

### Update API View
This view is used for update(PUT)

```python
class MovieUpdateConcreteView(generics.UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
```

## 21.05.2024
### ListCreateAPIView
This view is used for read-write endpoints ti represent a collection of model instances
```python
class MovieListCreateConcreteView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
```
The generic view help us to use `get` and `post` methods in a single view

### RetrieveUpdateAPIView
This view is used for read or update endpoints to represent a single model instance
```python
class MovieDetailUpdateConcreteView(generics.RetrieveUpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
```
This generic view is used for get a single instance from model and helps to update the element.

### RetrieveDestroyAPIView
This view is used for read and delete endpoints
```python
class MovieDetailDeleteConcreteView(generics.RetrieveDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
```
This generic view is used to retrieve an element or read an element then destroy or delete it

### RetrieveUpdateDestroyAPIView
This view is used for read-write-delete a single model instance
```python
class MovieDetailUpdateDeleteConcreteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
```
This generic view is used to do the 3 get-update-delete methods in a single model instance

