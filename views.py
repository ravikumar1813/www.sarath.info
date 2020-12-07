from django.shortcuts import render
from .models import Contact
from datetime import datetime
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"aboutme.html")
def works(request):
    return render(request,"mywork.html")
def contact (request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        mobile_no=request.POST.get("mobile_no")
        address=request.POST.get("address")
        desc=request.POST.get("desc")
        contact=Contact(name=name, email=email, mobile_no=mobile_no, address=address, desc=desc, date=datetime.today())
        contact.save()
    return render(request,"contact.html")