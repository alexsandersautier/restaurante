from django.urls import path
from dishes.views import DishListView, DishCreateView

urlpatterns = [
    path('', DishListView.as_view(), name='dish_list_view'),
    path('new/', DishCreateView.as_view(), name='dish_create_view'),
]