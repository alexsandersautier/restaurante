from django.views.generic import ListView
from dishes.models import Dish

class DishListView(ListView):
    model = Dish
    template_name = 'list.html'
    context_object_name = 'dishes'