from django.shortcuts import render, redirect
from .models import Volunteer, Contact, Cause,Donate, Person, work, Donations, Event

# Create your views here.
def index(request):
    causes=Cause.objects.all()
    return render(request,'index.html',{"causes":causes})

def about(request):
    works=work.objects.all()
    return render(request, 'about.html',{'works' : works})

def gallery(request):
    persons = Person.objects.all()
    return render(request, 'gallery.html', {'persons': persons})

def person_gallery(request):
    persons = Person.objects.all()
    return render(request, 'gallery.html', {'persons': persons})

def submit_valunteer(request):
    if request.method =="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        gender=request.POST['gender']
        dob=request.POST['dob']
        subject=request.POST['subject']
        message=request.POST.get('message')

        volunteer=Volunteer.objects.create(name=name,email=email,phone=phone, gender=gender, dob=dob, subject=subject,message=message)
        volunteer.save()
        return redirect('/')
    else:
        return redirect('/')

def contact(request):
    if request.method =="POST":
        f_name=request.POST['f_name']
        l_name=request.POST['l_name']
        email=request.POST['email']
        message=request.POST.get('message')

        contact=Contact.objects.create(name=f"{f_name}  {l_name}",email=email,message=message)
        contact.save()
        return redirect('/')
    else:
        return redirect('/')

def donate(request,id):
    if request.method =="POST":
        name=request.POST['name']
        email=request.POST['email']
        amount=request.POST.get('amount')

        cause=Cause.objects.get(id=id)
        cause.raised=cause.raised+float(amount)
        cause.goal=cause.goal-float(amount)
        cause.save()
        donation=Donate.objects.create(name=name,email=email,amount=float(amount))
        donation.save()
        return redirect('/')
    else:
        cause=Cause.objects.get(id=id)
        return render(request,'donate.html',{"cause":cause})
    
def contactus(request):
    return render(request, 'contactus.html')

def donates(request):
    if request.method =="POST":
        name=request.POST['name']
        email=request.POST['email']
        amount=request.POST.get('amount')
        photo = request.FILES.get('photo') 

        Donations.objects.create(name=name, email=email, amount=float(amount), photo=photo)
        return redirect('donates')
    
    donations = Donations.objects.all().order_by('-id')  # Order by latest first
    return render(request, 'donates.html', {"donations": donations})

def history(request):
    events = Event.objects.prefetch_related('images').all()
    return render(request, 'history.html', {'events': events})
    