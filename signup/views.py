from django.shortcuts import render
from signup.models import stu_reg

# Create your views here.
def signup(Req):
    if Req.method=='POST':
        stu_reg.objects.create(
            name=Req.POST.get("name"),
            email=Req.POST.get("email"),
            number=Req.POST.get("number"),
            dob=Req.POST.get("date"),
            gender=Req.POST.get("gender"),
            username=Req.POST.get("username"),
            password=Req.POST.get("pwd"),
            address=Req.POST.get("address"),
            country=Req.POST.get("country"),
            agree=Req.POST.get("agree"),

        )
        return render(Req , "home.html")
    return render(Req , "signup/signup.html")