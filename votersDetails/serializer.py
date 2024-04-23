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
    #field-level validations
    """def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("Age must be greater than 18")
        return value"""

    #object-level validation
    """def validate(self, data):
        if len(data["voter_id_no"]) > 15:
            raise serializers.ValidationError("Invalid Voter id")
        return data"""