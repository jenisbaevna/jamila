from django.shortcuts import render ,get_object_or_404
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
def detail(request,id):
    telefon=get_object_or_404(Phones,id=id)
    context={
        'telefon':telefon
    }
    return render(request,'detail.html',context=context)