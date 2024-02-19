from rest_framework.views import APIView
from rest_framework.response import response
from .models import Profile

class ProfileList(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        return Response(profiles)
