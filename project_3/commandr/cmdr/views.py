from django.views.generic import ListView
from .models import Cmdr
# Create your views here.

class HomepageView(ListView):
    model = Cmdr
    template_name = 'button.html'
