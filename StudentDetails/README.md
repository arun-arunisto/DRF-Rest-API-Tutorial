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
