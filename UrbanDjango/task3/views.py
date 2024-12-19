from django.views.generic import TemplateView
# Create your views here.

# Create your views here.

class template_cart(TemplateView):
    template_name = 'third_task/cart.html'

class template_games(TemplateView):
    template_name = 'third_task/games.html'

class template_platform(TemplateView):
    template_name = 'third_task/platform.html'