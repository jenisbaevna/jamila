from django.shortcuts import render
from .models import Students,Phones
# Create your views here.

def homepage(request):
    oqiwshilar=Students.objects.all()
    phones=Phones.objects.all()
    context={
        'students':oqiwshilar,
        'telefonlar':phones
    }
    return render(request,'home.html',context=context)