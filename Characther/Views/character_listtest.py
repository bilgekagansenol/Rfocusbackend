from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Characther.models import Character
from Characther.serializers import CharacterSerializer

class CharacterListTestView(APIView):
    def get(self, request):
        characters = Character.objects.all()
        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
