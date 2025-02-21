from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from dishes.models import Dish
from dishes.forms import DishModelForm

class DishListView(ListView):
    model = Dish
    template_name = 'list.html'
    context_object_name = 'dishes'

class DishCreateView(CreateView):
    model = Dish
    template_name = 'create.html'
    form_class = DishModelForm
    success_url = reverse_lazy('dish_list_view')