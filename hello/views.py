from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView 
from .models import Hello
from django.shortcuts import redirect
from django.core.mail import send_mail

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
    
class SendMailView(DetailView):
    #template_name = "hello/buy_item.html"
    
    def get(self, request):
        self.send_order_mail()      
        return redirect('hello:namelist')
    
    def send_order_mail(self):
        
        """題名"""
        subject = f"商品注文のお願い"
        """本文"""
        message = (
            "いつもお世話になっております。\n"
            )

        """送信元メールアドレス（企業DBから取得）"""
        from_email = "t21cs024@gmail.com"
        
        """宛先メールアドレス（企業DBから取得）"""
        recipient_list = [
            "tt342772@gmail.com"
            ]
        send_mail(subject, message, from_email, recipient_list)