On today's section we're going to look into how to create views it's actually like the previous section but we're going to implement some features into it. I will explain you one by one

### ListCreateAPIView
first we're going to take the `ListCreateAPIView` first i already explained this view on `generics` topic! But first we're going to look into how to pass a message when it's listing some data if there's no data. That what we're going to look first. The sample code provided below

```python
class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = RecipeSerializer(queryset, many=True)
        if queryset.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message":"No data available"}, status=status.HTTP_204_NO_CONTENT)
```
The above code `self.get_queryset()` method will fetch the above queryset that you declared on your class. And this is how we can implement our own logics inside a default class. The above code will pass a message with the status code if no data available.


On the above code you can see that on your post field there's an field named `chef` but here we're going to remove the `chef` selecting field from the post method. for that first open your `serializer.py` file and change your code like below.
```python
class RecipeSerializer(serializers.ModelSerializer):
    chef = serializers.StringRelatedField(read_only=True) #This is the line we added
    class Meta:
        model = Recipe
        fields = "__all__"
```
The above line will remove the `chef` field from Recipe View. So, now you will get confused how we're going to add the recipe without chef. We're going to write the logic in backend that is who is logged in the app will takes the logged person as chef.
```python
class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = RecipeSerializer(queryset, many=True)
        if queryset.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message":"No data available"}, status=status.HTTP_204_NO_CONTENT)

    def create(self, request, *args, **kwargs):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(chef=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
The above `create` method will helps to save the data as the login user entered `serializer.save(chef=self.request.user)` this line's purpose is that to fetch the user information by checking who's login
