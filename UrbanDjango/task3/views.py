from django.views.generic import TemplateView
# Create your views here.

# Create your views here.

class template_cart(TemplateView):
    template_name = 'cart.html'

class template_games(TemplateView):
    template_name = 'games.html'

class template_platform(TemplateView):
    template_name = 'platform.html'