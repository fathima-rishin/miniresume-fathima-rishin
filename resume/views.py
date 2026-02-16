from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ResumeSerializer

resumes = []
from django.http import JsonResponse

def health(request):
    return JsonResponse({"status": "healthy"})

@api_view(['GET'])
def health(request):
    return Response({"status": "healthy"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_resume(request):
    serializer = ResumeSerializer(data=request.data)

    if serializer.is_valid():
        resumes.append(serializer.validated_data)
        return Response(
            {"message": "Resume submitted successfully"},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
