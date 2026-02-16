from rest_framework import serializers

class ResumeSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=2)
    email = serializers.EmailField()
    phone = serializers.CharField()
    skills = serializers.ListField(
        child=serializers.CharField())
    experience = serializers.IntegerField(min_value=0)