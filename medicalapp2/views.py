from django.shortcuts import render
from .models import Num, Appointment, Sample
# Create your views here.

def Home(request):
    number_of_token = Num.objects.all()
    context = {
        'token': number_of_token, 'var1': 23,
    }
    print(context['token'])
    return render(request, 'medicalapp2/home.html', context)

def appointment(request):
    if request.method == 'POST':
        myname = request.POST.get('myname','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone', '')
        appointment_date = request.POST.get('appointment date', '')
        doctor = request.POST.get('doctor', '')
        department = request.POST.get('department', '')
        message = request.POST.get('message', '')
        appointment_save = Appointment(name=myname, email=email, phone=phone, appointment_date=appointment_date,
                                       doctor=doctor,
                                       department=department, message=message)
        appointment_save.save()
    return render(request, 'medicalapp2/appointment.html')



def sample(request):
    if request.method == 'POST':
        myname = request.POST.get('myname', '')
        myaddress = request.POST.get('myaddress', '')
        sample_object = Sample(name=myname, address=myaddress)
        sample_object.save()
    return render(request, 'medicalapp2/samle.html')
