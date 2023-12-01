from commons.custom_permissions import IsAdmin
from dummy.models import Dummy
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class AllDummiesAPI(APIView):
    permission_classes =  [AllowAny]

    def get(self, request):
        dummies = Dummy.objects.all()
        return Response(dummies, status = status.HTTP_200_OK)
    
class DummyAPI(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return Response("I'm Dummy", status = status.HTTP_200_OK)
    
    def post(self, request):
        dummy = Dummy.objects.create(name = request.POST.get('name'))
        return Response(dummy, status = status.HTTP_201_OK)
    
class ProtectedDummyAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response("I'm Protected Dummy", status = status.HTTP_200_OK)
    
    def post(self, request):
        dummy = Dummy.objects.create(name = request.POST.get('name'))
        return Response(dummy, status = status.HTTP_201_OK)
    
class AdminDummyAPI(APIView):
    permission_classes = [IsAdmin]
    def get(self, request):
        return Response("I'm Admin Dummy", status = status.HTTP_200_OK)
