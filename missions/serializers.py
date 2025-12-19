from django.db import transaction
from rest_framework import serializers

from missions.models import Mission, Target


class TargetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Target
        fields = (
            "id",
            "name",
            "country",
            "complete_state",
        )
        read_only_fields = ("id",)


class TargetUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = (
            "id",
            "complete_state",
            "notes"
        )

    def validate(self, attrs):
        instance = self.instance

        if instance and instance.complete_state:
            old_notes = instance.notes
            new_notes = attrs.get("notes", old_notes)
            if new_notes != old_notes:
                raise serializers.ValidationError({
                    "notes": "Cannot change notes when target is completed"
                })

        return attrs


class MissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mission
        fields = (
            "id",
            "cat",
            "complete_state",
            "targets",
        )


class MissionCreateSerializer(MissionSerializer):
    targets = TargetSerializer(many=True, read_only=False)

    @transaction.atomic
    def create(self, validated_data):
        targets_data = validated_data.pop("targets")

        mission = Mission.objects.create(**validated_data)

        targets = [
            Target(mission=mission, **target_data)
            for target_data in targets_data
        ]

        Target.objects.bulk_create(targets)

        return mission
