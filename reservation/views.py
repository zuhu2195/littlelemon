from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import permissions

from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer

# Create your views here.

# class bookingview(APIView):

#     def get(self, request):
#         items = Booking.objects.all()
#         serializer = BookingSerializer(items, many=True)
#         return Response(serializer.data)


# class menuview(APIView):
#     def post(self, request):
#         serializer = MenuSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status':'success', 'data': serializer.data})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 