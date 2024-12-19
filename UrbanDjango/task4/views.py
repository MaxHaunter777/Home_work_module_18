from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def func_template(request):
    return render(request, "fourth_task/func_template.html")

class class_template(TemplateView):
    template_name = 'fourth_task/class_template.html'

class template_cart(TemplateView):
    template_name = 'fourth_task/cart.html'

def games(request):
    game_dict = {'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay 77"]}
    context = {
        'game_dict': game_dict,
    }
    return render(request, 'fourth_task/games.html', context)

class template_platform(TemplateView):
    template_name = 'fourth_task/platform.html'