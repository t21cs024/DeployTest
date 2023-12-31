from django.urls import path
from .views import IndexView, NameListView, NameDetailView, SendMailView

app_name = 'hello'

urlpatterns = [
    path('', IndexView.as_view()),
    path('list/', NameListView.as_view(), name='namelist'),
    path('detail/<int:pk>/', NameDetailView.as_view(), name='namedetail'),
    path('sendmail/', SendMailView.as_view(), name='sendmail'),
    ]