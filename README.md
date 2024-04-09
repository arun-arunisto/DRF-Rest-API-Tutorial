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









