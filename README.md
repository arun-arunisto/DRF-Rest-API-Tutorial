# Django-Rest-Framework-API-Tutorials

## API's using DRF 
### Tech Stacks
Install the following required packages/modules using pip
```commandline
pip install django djangorestframework
```
After the packages installing successfully, use the below command to create project
```commandline
django-admin startproject drf_api_project_folder .
```
The above code will create a project folder named `drf_api_project_folder`. I am going to create two applications `1. mainApp` and `2. helloWorld` by using the below command
### 1. mainApp
```commandline
python manage.py startapp mainApp
```
### 2. helloWorld
```commandline
python manage.py startapp helloWorld
```
Okay, so let's move into the next section, after successfully create apps, need to add into `INSTALLED_APPS` on `settings.py` file in the project folder.
```python
#settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'helloWorld',
    'mainApp'
]
```
## mainApp
`mainApp` will navigate the user about the end-points and other operations
## helloWorld 
`helloWorld` app just an application to demonstrate the basic api operations
On the day ```02.04.2024``` on hello world app we create a sample model and other sample views to display data on JSON format

## 03.04.2024 - ADMIN PANEL CONFIGURING
1. Changing Dash Board View

Changing the admin dashboard view from this

![img.png](img.png)

to this

![img_1.png](img_1.png)

by adding the code block on `admin.py` on your app folder, adding a new class in `admin.py` file like below

```python
class SampleAdmin(admin.ModelAdmin):
     list_display = ("id", "name", "age", "job", "created_at") #these names are the column names of our model
```

After adding the class you need to register on your admin site like below

```python
admin.site.register(Sample) #previous one only with model 
```
the above code needs to change to like below
```python
admin.site.register(Sample, SampleAdmin) 
```

2. Adding Links

Now you can view the data from dashboard and if you click the `id` it will navigate to the edit page, but if we need to do the same when we click other field like `name` to do that we are going to add an another attribute named `list_display_links` inside the class like below
```python
class SampleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "job", "created_at")
    list_display_links = ("id", "name")
```

3. Search Links

We can add search field using the same method, add a line of code like below
```python
class SampleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "job", "created_at")
    list_display_links = ("id", "name")
    search_fields = ("name", "job")
```
Always remember you need to provide column names on tuple always

4. Pagination

We can add pagination feature on our dashboard you can limit the table list per page, by adding the below line of code
```python
class SampleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "job", "created_at")
    list_display_links = ("id", "name")
    search_fields = ("name", "job")
    list_per_page = 10
```

5. Editing

We can implement the editing feature (without navigate to detail view) also, before that i am going to add an another boolean field on our model like below
```python
class Sample(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    job = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True) #<--- Added field
    created_at = models.DateTimeField(default=datetime.now())
```
After the column added we need to run the scripts for `makemigrations` and `migrate` on our command prompt. After the migration we are going to add the `is_active` column for editable columns, like below
```python
class SampleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "job", "is_active", "created_at")
    list_display_links = ("id", "name")
    search_fields = ("name", "job")
    list_per_page = 10
    list_editable = ('is_active',)
```

6. Filter

Next we're going to add the filter option by using `list_filter` like below

```python
class SampleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "job", "is_active", "created_at")
    list_display_links = ("id", "name")
    search_fields = ("name", "job")
    list_per_page = 10
    list_editable = ('is_active',)
    list_filter = ("id", "name", "created_at")
```

After all these changes your admin dashboard will look like this

![img_3.png](img_3.png)

<hr>

# Rest API

In the above part we just created a simple API using django's default json concept. But this is not the proper way to create an API we need some architecture or rules to follow for creating an API that's where the `djangorestframework` aka `drf` is going to use for that we are going to create a new app named `employeeDetails` for doing some CRUD operations on employee field using REST API, so first we're going to create an app using below command on terminal

```commandline
python manage.py startapp employeeDetails
```

After successfully created i had done the admin panel styling parts like above and created models you can check that out, that's all for today we will start to create REST API from tomorrow

## 09.04.2024 
REST API continues
<br>
After create an app you need to create a `serializer.py` file on your `app_folder`. Why we're using serializer?
<br>
Serializer - will help to convert complex datatypes into JSON format.
<br>
So after creating we need to add `serializers` to our program like below all the fields representing the fields in `models.py`. And there are two serializers one is `Serializer` other one is `ModelSerializer`, here we're using `Serializer`
```python
#serializer
from rest_framework import serializers

#creating serializers based on models field
class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    email = serializers.EmailField()
    phone_no = serializers.IntegerField()
    address = serializers.CharField()
    designation = serializers.CharField()
    joined_at = serializers.DateField()
    is_active = serializers.BooleanField()
```
We can clearly seen that all the field taken from the `models.py` `Employee` class, and `TextField` is `CharField` in serializer
<br>
After successfully implemented the code on `serializer`, we're moving to the `views.py` to write views for our application.
### Function-Based Views - GET
Before that clear all the default code on you're `views.py` file and add the below provided code
```python
from .models import Employee
from .serializer import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def employee_list(request):
    all_emp = Employee.objects.all()
    #converting to json using serializer
    serialized_data = EmployeeSerializer(all_emp, many=True)
    return Response(serialized_data.data)
```
`api_view` - In django rest framework `@api_view` decorator needs to be used if you're using function based views
`many=True` - If you want to fetch more than one data you need to pass this on args, otherwise, it will raise an error

After successfully created the views add your views to the `urls.py` then run the program and navigate to the url that provided by you here, and if you're running this repo the url will be like `http://127.0.0.1:8000/api/employee-details-api/employee-list/` navigate to this url using your browser the result will be look like below

![img_4.png](img_4.png)

Next, the code for fetching single data
```python
@api_view(["GET"])
def employee_details(request, id):
    emp = Employee.objects.get(id=id)
    serialized_data = EmployeeSerializer(emp)
    return Response(serialized_data.data)
```
Here you can clearly see that `many=True` is removed because we're fetching single data
### Function-Based views - POST
Before adding POST request you need to add a instance method called create on your `serializer` class like below
```python
class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    email = serializers.EmailField()
    phone_no = serializers.IntegerField()
    address = serializers.CharField()
    designation = serializers.CharField()
    joined_at = serializers.DateField()
    is_active = serializers.BooleanField()

    def create(self, validated_data): #<--- this method added for the post request
        return Employee.objects.create(**validated_data)
```
POST request for adding data, we're going to add a request method post to our `employee_details` view like below
```python
@api_view(['GET', 'POST'])
def employee_list(request):
    if request.method == "POST":
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    all_emp = Employee.objects.all()
    #converting to json using serializer
    serialized_data = EmployeeSerializer(all_emp, many=True) 
    return Response(serialized_data.data)
```
For api-testing i am using `postman` tool. You can use your own comfort tool/browser(drf-default config)
### Function-Based Views - PUT
For put method also we need to define a function called update on `serializer` like below
```python
class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    email = serializers.EmailField()
    phone_no = serializers.IntegerField()
    address = serializers.CharField()
    designation = serializers.CharField()
    joined_at = serializers.DateField()
    is_active = serializers.BooleanField()

    #post request
    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    #put request
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_no = validated_data.get('phone_no', instance.phone_no)
        instance.address = validated_data.get('address', instance.address)
        instance.designation = validated_data.get('designation', instance.designation)
        instance.joined_at = validated_data.get('joined_at', instance.joined_at)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance
```
And we're going to add view for PUT method
```python
@api_view(["GET", "PUT"])
def employee_details(request, id):
    if request.method == "PUT":
        emp = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    emp = Employee.objects.get(id=id)
    serialized_data = EmployeeSerializer(emp)
    return Response(serialized_data.data)
```
### Function-Based Views - DELETE
You don't need to add anything on `serializer` when it's to delete, so just add the below code to your views
```python
@api_view(["GET", "PUT", "DELETE"])
def employee_details(request, id):
    if request.method == "PUT":
        emp = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    if request.method == "DELETE":
        emp = Employee.objects.get(id=id)
        emp.delete()
        return Response({"message":"Success"})
    emp = Employee.objects.get(id=id)
    serialized_data = EmployeeSerializer(emp)
    return Response(serialized_data.data)
```

## 10.04.2024
Added `status_code` on view methods for that first we need to import `status` from `rest_framework` like below
```python
from rest_framework import status
```
Then you can add it on your function `Response` like below
```python
@api_view(['GET', 'POST'])
def employee_list(request):
    if request.method == "POST":
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) #<- status code
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    all_emp = Employee.objects.all()
    #converting to json using serializer
    serialized_data = EmployeeSerializer(all_emp, many=True)
    return Response(serialized_data.data, status=status.HTTP_200_OK)
```
Find the status code link <a href="https://www.django-rest-framework.org/api-guide/status-codes/">Here</a>!

### Model Serializer
For demonstrating `ModelSerializer` we're going to create another app called `StudentDetails`
<br>
If your using `ModelSerializer` you dont need to add bunch of code like `serializer` class you can simple use the `Meta` class and you can add every field like a list. So, if your using `ModelSerializer` your code will be look like below
```python
from rest_framework import serializers
from .models import StudentData

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentData
        #choosing fields as a list
        fields = ["name", "degree", "specialization", "joined_at", "passed_out"]

```
It's really easy peasy ;)

## 11.04.2024
### Class Based Views
For that we're going to create an app called `TodoApp` and this app views will be completely using the class based views
<br>After creating the app other configurations (model, urls, serializers, etc) all are same like other apis, so let's start with the `views.py`

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

## 19.04.2024
### Validation
Next we're going to see how to validate the serialized fields for that we're going to create an application named `votersDetails`, and we are going to use class based views and model serailizers for the application.
## 22.04.2024
Today we're going to see the `Field-level Validators` for this topic we already created an app called `VotersDetails` on previous section. For the validation process open your 'serializer.py' file and select the field that you want to validate and write the code like below, here, i am going to take `age` field for validation.
for validating fields always start your function name with `validate_<field_name>`, here i am going to check that age is above 18 if less than 18 it will raise an error. The sample code look like below

```Python
from rest_framework import serializers
from .models import Voters

class VotersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voters
        fields = "__all__"

    #field-level validations
    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("Age must be greater than 18")
        return value
```
## 23.04.2024
`Object-level Validation` in this validation we dont need to specify the fields we can validate data using `validate` method like below

```python
from rest_framework import serializers
from .models import Voters

class VotersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voters
        fields = "__all__"

    #field-level validations
    def validate_age(self, value):
        ...

    #object-level validation
    def validate(self, data):
        if len(data["voter_id_no"]) > 15:
            raise serializers.ValidationError("Invalid Voter id")
        return data
```
Next, one is `validators` this also used to validate a single field but totally different compare to `field-level validators` first you need to add the validation field on your class and you need to specify the function for validation like below

```python
from rest_framework import serializers
from .models import Voters

#validators
def age_valid(value):
    if value < 18:
        raise serializers.ValidationError("Age must be greater than 18")
    return value

def voter_id_valid(value):
    if len(value) > 15:
        raise serializers.ValidationError("Voter id not valid")
    return value
class VotersSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    age = serializers.IntegerField(validators=[age_valid])
    voter_id_no = serializers.CharField(validators=[voter_id_valid])
    class Meta:
        model = Voters
        fields = "__all__"
```
### SerializerMethodField
It will help us to create an extra field on our api and we can use it for reference or any other useful contents, so here we are going to take the votersDetails app for this section also and we are going to add an extra field to show the length of the voter id number it will just to show how the `SerializerMethodField` working concept so for that first we need to create an object inside the serializer class to call the `SerializerMethodField` so i am going to name it as `len_voter_id_no` 

```python
len_voter_id_no = serializers.SerializerMethodField()
```
Then after creating the object we need to call it on a method that starts with `get` always remember your method name must start with `get` and after that you need to add your object name like `get_len_voter_id_no` so the method will be like below

```python
def get_len_voter_id_no(self, object):
    return len(object.voter_id_no)
```
so, it will generate an extra field on your api, the complete code will look like below

```python
from rest_framework import serializers
from .models import Voters

#validators
def age_valid(value):
    if value < 18:
        raise serializers.ValidationError("Age must be greater than 18")
    return value

def voter_id_valid(value):
    if len(value) > 15:
        raise serializers.ValidationError("Voter id not valid")
    return value
class VotersSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    age = serializers.IntegerField(validators=[age_valid])
    voter_id_no = serializers.CharField(validators=[voter_id_valid])

    #serializer method field
    len_voter_id_no = serializers.SerializerMethodField()
    class Meta:
        model = Voters
        fields = "__all__"

    def get_len_voter_id_no(self, object):
        return len(object.voter_id_no)
```

### Nested Serializer
For this topic we're going to create an new application called `spotifyApp` with 2 tables `Tracks` and `Albums` here, i will show you the `Foregin-key` concept also and other configurations all are same.

## 02.05.2024
Created a index page for `mainApp` to know about the api's that we built and their info and the endpoints details, so, if you run the project folder and navigate to the homepage you will see the page like below

![img_5.png](img_5.png)

## 03.05.2024
Again we're continuing with the `NestedSerializer` concept, so already we created an app to perform the nested serializer. So, the app contains two table already we created one table as an serialized object so today we're going to see how to do other
```python
from rest_framework import serializers
from .models import Album, Tracks

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracks
        fields = "__all__"
```
So, this is the already existing code. Here, you can see that we already created for `Tracks` model. Next, we're going to create for the `Album` model like this.

```python
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        exclude = ["id"]
```
In the above code we added our album serializer. And, I use `exclude` method to remove id from serialization after this we're going to add the views for album also like that we already done on our previous projects. 

Data which belong to the foreign key should displayed this is why we use `Nested Serializer`. For this we need to add some code on our Serializer that we created for our album, Actually `album` is the foreign key of `tracks`. So, we're going to add some code on the album serializer like below.

```python
class AlbumSerializer(serializers.ModelSerializer):
    #nested serializer concept
    album_name = serializers.CharField() # <------
    album = TrackSerializer(many=True, read_only=True) # <-----
    class Meta:
        model = Album
        exclude = ["id",]
```
So, here we added two lines of code first one for our album_name, second one for album. And, always remember what you will use as a `related_name` in your foreign key model like my model below

```python
class Tracks(models.Model):
    track_name = models.CharField(max_length=50)
    artist_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="album")

    def __str__(self):
        return f"Track {self.track_name}"
```
on the above code you can see the `related_name` as `album`. After this change again restart your server and go to your endpoint. so, you can view the data that belongs to this foreign key. like below,

![img_7.png](img_7.png)

So, here we do it for the list-view, next we're going to do for the detail view for that we're going to create a new view for the `detail-view`.  No, need to worry actually this is also the same type of code that we used on our previous projects.


### API Reference
For this topic we're going to create a new Application named `BlogApp`, because this topic covers various concept like serialization on `StringRelatedField`, `HyperLink`, `SlugField`, etc so, we're going to create a new app and going to add lots of columns in our models, like below

```python
import random
import string
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return f"Category: {self.category_name}"

class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    post_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    slug = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.blog_title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.blog_title+" "+self.category.category_name)
            self.slug = base_slug+''.join(random.choice(string.ascii_letters+string.digits) for _ in range(5))
        return super().save(*args, **kwargs)
```

Then as usual add views, urls, serializers like we before did.

## 10.05.2024
### API Reference Continues
So, on our previous section we see that nested serializer concept that displaying the details of foreign key related table. And we can see that it fetching all the details but we don't want that. So, we are going to return the string that we provided on our `__str__` special method on our `models.py` file. For that we want to make some changes on our `serializer.py` file like below
```python
class CategorySerializer(serializers.ModelSerializer):
    #category_name = serializers.CharField()
    #category = BlogSerializer(many=True, read_only=True)

    #API Reference
    category = serializers.StringRelatedField(many=True)

    class Meta:
        model = Category
        exclude = ["id"]
```
You can clearly see that previous topics code that i comment down and added a new line with `serializers.StringRelatedField` after making these changes the output result will be look like below

![img_8.png](img_8.png)

We just saw that how the `StringRelatedField` works, next we're going to display the `PrimaryKeyRlatedField`
```python
class CategorySerializer(serializers.ModelSerializer):
    #category_name = serializers.CharField()
    #category = BlogSerializer(many=True, read_only=True)

    #API Reference
    #category = serializers.StringRelatedField(many=True)
    category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Category
        exclude = ["id"]
```
This will display only the primary key, next, we're going to see the `HyperlinkedRelatedField` for this method you need to pass two arguments called `view_name` and `lookup_field`. After the implementation code will look like below
```python
class CategorySerializer(serializers.ModelSerializer):
    #category_name = serializers.CharField()
    #category = BlogSerializer(many=True, read_only=True)

    #API Reference
    #category = serializers.StringRelatedField(many=True)
    #category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    category = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True, view_name='blog-list-view', lookup_field='id')

    class Meta:
        model = Category
        exclude = ["id"]
```
After make this change you need to add one more argument `context` at your `views.py`'s serialize_data object like below

```python
class CategoryDetailView(APIView):
    def get(self, request):
        data = Category.objects.all()
        serialized_data = CategorySerializer(data, many=True, context={'request': request})
        return Response(serialized_data.data, status=status.HTTP_200_OK)

class CategoryListView(APIView):
    def get(self, request, id):
        data = Category.objects.get(id=id)
        serialized_data = CategorySerializer(data, context={'request': request})
        return Response(serialized_data.data, status=status.HTTP_200_OK)
```
After making this change you will see a link of the data on your result. And next we're going to execute `SlugRelatedField`, like below
```python
class CategorySerializer(serializers.ModelSerializer):
    #category_name = serializers.CharField()
    #category = BlogSerializer(many=True, read_only=True)

    #API Reference
    #category = serializers.StringRelatedField(many=True)
    #category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    """category = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True, view_name='blog-list-view', lookup_field='id')"""
    category = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')

    class Meta:
        model = Category
        exclude = ["id"]
```
## 14.05.2024
### Generic View - Mixins
We saw how the Class based views works in our previous parts. From today onwards we're going to look into how the `Generic View` works! Comparing to other views Generic view is easy and it's only need a short code we dont need junk line of codes. For this `Generic View` initialization we're going to create a new app called `booksApp` so we will continue this topic after all the other configuration of app's finish! I will be right back after sometime!! Happy Coding!!

![img_9.png](img_9.png)

The above picture shows that how the normal class based views look like, but here we're not going to use the normal class based view. We're going to use the `Generic Views` like below

But before that you need to know about the attributes (default) for generic views. There are lots of attributes there so it's a default attr you're not allowed to change their names. So, first we are going to look into two generic view mixins 

1. ListModelMixin
2. CreateModelMixin

Before you start you need to import the `mixins` and `generics` from `rest_framework` like below
```python
from rest_framework import mixins, generics
```
After the import, we're able to use the methods inside our code, So, the code for `Generic Views` will be look like below.
```python
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Author, Category, Book
from .serializer import AuthorSerializer, CategorySerializer, BookSerializer
from rest_framework import mixins, generics

# Create your views here.
#Generic Views
class BookListGenericView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    #get method
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    #post method
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

```
On the above code you will see `queryset` and `serializer_class` objects, actually these are the default attribute I mentioned in previous part. 

1. `queryset` - on this attribute you only allowed to write query otherwise it will raise an error
2. `serializer_class` - on this attribute you only allowed to write the serializer class without `()` these parenthesis. otherwise it will raise an error

Actually you can see that how many lines we just needed for the list view operations(GET, POST) this is one of the main reason for the `Generic View` use. And the other reason is after running the code just navigate to the url the result will be look like below

![img_10.png](img_10.png)

Previous parts you need to post data as in a JSON format but after the implementation of `Generic View` you are able to add data using a form. Now we're going to add this for other `Author` and `Category` models like above.

## 16.05.2024
### RetrieveModelMixin
On the above tutorial we've been look into fetch all the data using `ListModelMixin` here I am going to show you guys how to fetch a single data using `RetrieveModelMixin`.

```python
class BookDetailGenericView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
```
On the above code we're returning `retrieve` instead of `list` because we're trying to fetch a single data, and yu can see that i didn't provide any keys to fetch data. Because you don't need to the `RetrieveModelMixin` will automatically takes the key as argument from `urls.py` and the url file remains same as the old applications urls file. And also dont worry i am providing the urls.py code below for a reference.

```python
from django.urls import path
from .views import *

urlpatterns = [
    path('book-list-view/', BookListView.as_view(), name="book-list-view"),
    path('book-list-generic-view/', BookListGenericView.as_view(), name="book-list-generic-view"),
    path('author-list-generic-view/', AuthorListGenericView.as_view(), name='author-list-generic-view'),
    path('category-list-generic-view/', CategoryListGenericView.as_view(), name="category-list-generic-view"),
    path('book-detail-generic-view/<int:pk>/', BookDetailGenericView.as_view(), name='book-detail-generic-view')
]
```
And i am going to add the feature to the remaining two models `Category` and `Author` like above

### UpdateModelMixin
`UpdateModelMixin` is used to update a particular data. For this, you don't need to create a new class you can simply add it on you're retrieve class that we created above you can add the update model mixin to the same class like below

```python
class BookDetailGenericView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
```
That's it that's all!!! <3

### DestroyModelMixin
`DestroyModelMixin` is used to delete an element, for this also you dont need to create a separate class you can simply add to your existing class like `UpdateModelMixin` still confused don't worry i will provide the code below.

```python
class BookDetailGenericView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
```
In the above mixins we're using `pk` to retrieve data but how to use another field instead of `pk` (primary key) that's where we're going to use `lookup_field` for set a particular field from our model to fetch data. Here, we're going to use the `book_title` field for fetching data, always remember if the field doesn't exist on your model it will raise an error.

```python
class BookDetailGenericView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "book_title"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
```

And also you need to make a change on your `urls.py` file also, like below:

```python
from django.urls import path
from .views import *

urlpatterns = [
    path('book-list-view/', BookListView.as_view(), name="book-list-view"),
    path('book-list-generic-view/', BookListGenericView.as_view(), name="book-list-generic-view"),
    path('author-list-generic-view/', AuthorListGenericView.as_view(), name='author-list-generic-view'),
    path('category-list-generic-view/', CategoryListGenericView.as_view(), name="category-list-generic-view"),
    path('book-detail-generic-view/<str:book_title>/', BookDetailGenericView.as_view(), name='book-detail-generic-view'),
    path('author-detail-generic-view/<int:pk>/', AuthorDetailGenericView.as_view(), name='author-detail-generic-view'),
    path('category-detail-generic-view/<int:pk>/', CategoryDetailGenericView.as_view(), name='category-detail-generic-view')
]
```
On the above code you can see that i changed `<int:pk>` to `<str:book_title>`!!

## 20.05.2024
### Concrete View Classes
Today we're going to discuss about the `ConcreteViewClasses` for this! I am going to create a new `application` called `MovieReviewApp`, by using the above methods

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
You dont need to mention any keys to fetch it will automatically fetch the elements from that key you gave it in url

