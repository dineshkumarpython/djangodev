from django.shortcuts import render
from .models import CountNumber, Profie
# Create your views here.
def index(request):
    return render(request, 'medicalapp1/index.html')

def count(request):
    a = Profie.objects.all()




    return render(request, 'medicalapp1/countpage.html',{'a':a})
