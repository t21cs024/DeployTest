from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView 
from .models import Hello

class IndexView(TemplateView):
    template_name = "hello/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['one_name'] = Hello.objects.all()[0]
        return context

class NameListView(ListView):
    model = Hello
    
class NameDetailView(DetailView):
    model = Hello