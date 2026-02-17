from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CandidateSerializer
import uuid

#in memory-storage
candidates=[]

#Health check endpoint
@api_view(['GET'])

def health(request):
    return Response({"status":"OK"},status=status.HTTP_200_OK)

#create candidate(Resume upload)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import uuid
from .serializers import CandidateSerializer

candidates = []  # temporary storage for candidates

@api_view(['POST'])
def create_candidate(request):
    serializer = CandidateSerializer(data=request.data)
    
    if serializer.is_valid():
        data = serializer.validated_data  # use only inside this block
        resume_file = data.get("resume")
        resume_name = resume_file.name if resume_file else None

        candidate_data = {
            "id": str(uuid.uuid4()),
            "full_name": data["full_name"],
            "dob": str(data["dob"]),
            "contact_number": data["contact_number"],
            "address": data["address"],
            "education": data["education"],
            "graduation_year": data["graduation_year"],
            "experience": data["experience"],
            "skill_set": data["skill_set"],
            "resume_name": resume_name
        }

        candidates.append(candidate_data)

        return Response({"message": "Candidate created successfully", "candidate": candidate_data}, status=status.HTTP_201_CREATED)
    
    else:
        # If invalid, return the errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#list candidate(with filters)
@api_view(['GET'])

def list_candidate(request):
    skill=request.GET.get("skill_set")
    experience=request.GET.get("experience")
    graduation_year=request.GET.get("graduation_year")

    filtered = candidates

    if skill:
        filtered = [
            c for c in filtered
            if skill.lower() in c["skill_set"].lower() 
            ]
    if experience:
        filtered =[
            c for c in filtered
            if float(c["experience"]) >= float(experience)
        ]
    if graduation_year:
        filtered = [
            c for c in filtered
            if str(c["graduation_year"]) == graduation_year
        ]
    return Response(filtered,status=status.HTTP_200_OK)

#get candidate by id
@api_view(['GET'])

def get_candidate(request,candidate_id):
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return Response(candidate,status=status.HTTP_200_OK)
    return Response({"error":"Candidate not found"},status=status.HTTP_404_NOT_FOUND)


#delete candidate by id
@api_view(['DELETE'])

def delete_candidate(request,candidate_id):
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            candidates.remove(candidate)
            return Response({"message":"Candidate removed successfully"},status=status.HTTP_200_OK)
    return Response({"error":"Candidate not found"},status=status.HTTP_404_NOT_FOUND)