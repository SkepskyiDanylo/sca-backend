from rest_framework import serializers

from cats.models import Cat
from cats.validators import breed_validator


class CatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cat
        fields = (
            "id",
            "name",
            "breed",
            "salary",
            "years_of_experience"
        )

    def validate_breed(self, value):
        if not breed_validator(value):
            raise serializers.ValidationError("Invalid breed")
        return value


class CatUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cat
        fields = (
            "id",
            "salary"
        )