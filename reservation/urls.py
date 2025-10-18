from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter



urlpatterns = [
    #path('', views.index, name = 'home'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]