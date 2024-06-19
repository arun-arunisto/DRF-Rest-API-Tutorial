After creating the app other configurations (model, urls, serializers, etc) all are same like other apis, so let's start with the `views.py`

For class-based views we're not using the decorator `@api_view` that we use for the function-based views, we're going to use the module `APIView` from `rest_framework.views` so we need to import that first on our views so, after the necessary imports the code will look like below,
```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializer import TodoSerializer
```

### Class Based Views - GET
After the modules imported we're going to write the methods inside our class like below first we are going to look on the `GET` method

```python
class TodoListView(APIView):
    def get(self, request):
        data = Todo.objects.all()
        serialized_data = TodoSerializer(data, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
```
So, you can clearly seen that we're using our `get` function as instance method of the class. After adding the method to class we're going to map the view to urls on `urls.py` like below.
```python
from django.urls import path
from .views import TodoListView

urlpatterns = [
    path('todo-list/', TodoListView.as_view(), name="todo-list")
]
```
In class-based view we use `.as_view()` function on urls.

### Class Based Views - POST
Next, we're going look how to implement the `POST` method on our class

*(<span style="color:red;">always remember one thing POST method on LISTVIEW. PUT & DELETE on detail view</span>)

```python
class TodoListView(APIView):
    def get(self, request):
        """
        """

    def post(self, request):
        serialized_data = TodoSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

```
### Class Based Detail View - GET
Next, we are going to fetch a particular single data for that we're going to add a new class like below
```python
class TodoDetailView(APIView):
    def get(self, request, id):
        data = Todo.objects.get(id=id)
        serialized_data = TodoSerializer(data)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
```
Then going to add this view class on our `urls.py` file, like below
```python
from django.urls import path
from .views import TodoListView, TodoDetailView

urlpatterns = [
    path('todo-list/', TodoListView.as_view(), name="todo-list"),
    path('todo-details/<int:id>/', TodoDetailView.as_view(), name='todo-details')
]
```

### Class Based Views - PUT
For PUT request the code will look like below
```python
class TodoDetailView(APIView):
    def get(self, request, id):
        """
        """

    def put(self, request, id):
        t_data = Todo.objects.get(id=id)
        serialized_data = TodoSerializer(t_data, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
```

### Class Based Views - DELETE
For DELETE request the code will look like below
```python
class TodoDetailView(APIView):
    def get(self, request, id):
        """
        """

    def put(self, request, id):
        """
        """

    def delete(self, request, id):
        data = Todo.objects.get(id=id)
        data.delete()
        return Response({"message":"Deleted Successfully"}, status=status.HTTP_200_OK)
```
