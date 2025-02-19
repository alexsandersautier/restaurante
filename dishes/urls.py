from django.urls import path
from dishes.views import DishListView

urlpatterns = [
    path('', DishListView.as_view(), name='dish_list_view'),
]