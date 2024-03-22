from django.urls import path
from Port import views

app_name="Port"

urlpatterns = [
    path('',views.index,name='index'),
]