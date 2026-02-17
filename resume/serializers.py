from rest_framework import serializers
import os
from datetime import datetime
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['POST'])
def create_candidate(request):
    serializer = CandidateSerializer(data=request.data)
    
    if serializer.is_valid():
        data = serializer.validated_data  # valid data
        return JsonResponse({"success": True, "candidate": data})
    else:
        # if not valid, return the errors instead
        return JsonResponse({"success": False, "errors": serializer.errors})

class CandidateSerializer(serializers.Serializer):
    full_name=serializers.CharField(max_length=100)
    dob=serializers.DateField()
    contact_number=serializers.CharField(max_length=15)
    address=serializers.CharField()
    education=serializers.CharField(max_length=100)
    graduation_year=serializers.IntegerField()
    experience=serializers.FloatField()
    skill_set=serializers.CharField()
    resume=serializers.FileField(required=False)

    #experience validation
    def validate_experience(self,value):
        if value<0:
            raise serializers.ValidationError("Experience cannot be negative")
        return value
    

    #graduation year validation
    def validate_graduation_year(self,value):
        current_year=datetime.now().year
        if value < 2020 or value > current_year:
            raise serializers.ValidationError("Enter a valid graduation year")
        return value
    
    #resume file validation
    def validate_resume(self,value):
        allowed_extensions=['.pdf','.doc','.docx']
        ext= os.path.splitext(value.name)[1].lower()

        if ext not in allowed_extensions:
            raise serializers.ValidationError("Resume must be in PDF,DOC or DOCX format.")
        return value