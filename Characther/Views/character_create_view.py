from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Characther.serializers import CharacterSerializer

class CharacterCreateView(APIView):
    def post(self, request):
        serializer = CharacterSerializer(data=request.data)
        if serializer.is_valid():
           ## serializer.save(user=request.user)  # karakteri oturumdaki kullanıcıya bağla FUTURE WORK
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

## HERHANGI BIR USER OLMADIGINDAN ŞUANLIK KULLANILMAZ DURUMDA 