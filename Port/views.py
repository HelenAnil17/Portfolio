from django.shortcuts import render
from Port.models import *
# Create your views here.
def index(request):
    if request.method == 'POST':
        contact.objects.create(
            name=request.POST.get('name'),
            mail=request.POST.get('mail'),
            message=request.POST.get('message'),
        )
        return render(request,'Port/index.html')
    else:
        return render(request,'Port/index.html')
