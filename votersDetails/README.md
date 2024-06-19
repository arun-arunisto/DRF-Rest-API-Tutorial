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
