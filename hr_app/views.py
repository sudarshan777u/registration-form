from django.shortcuts import render

# Create your views here.

from django.shortcuts import render , HttpResponse
from .models import student

from django.core.mail import send_mail 
from django.conf import settings 
from django.contrib import messages



def register(request):
    if request.method =="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        add= request.POST.get("address")
        city = request.POST.get("city")
        post = request.POST.get("postal_code")
        high = request.POST.get("highest_qualification")
        percent= request.POST.get("percentage")
        college= request.POST.get("college")
        yop = request.POST.get("year_of_passing")
        cour= request.POST.get("course")
        cer = request.POST.get("certifications")
        skill= request.POST.get("skills")  
        expe= request.POST.get("experience")
       
        obj=student.objects.create(
            name=name,email=email,mobile=mobile,
            address=add,city=city,postal_code=post,
            highest_qualification=high,percentage=percent,
            college=college,year_of_passing=yop,course=cour,
            certifications=cer,skills=skill,experience=expe

        )    
    
        print(settings.EMAIL_HOST_USER)
        send_mail(
            'Registration Details',
            f"Name: {name}\nemail:{email}\nmobile:{mobile}\naddress:{add}\ncity:{city}\npostal_code:{post}\nhighest_qualification:{high}\npercentage:{percent}\ncollege:{college}\nyear_of_passing:{yop}\ncourse:{cour}\nskills:{skill}\nexperience:{expe}",
            settings.EMAIL_HOST_USER,
            ['chembakurusudarshanreddy@gmail.com'],
            fail_silently=False,
            )

      
    return render(request,"form.html")

