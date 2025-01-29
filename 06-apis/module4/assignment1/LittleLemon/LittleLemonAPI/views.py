from django.shortcuts import render
from rest_framework.views import APIView

from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemsView(APIView):
    def get(self, request):
        items = MenuItem.objects.select_related('category').all()