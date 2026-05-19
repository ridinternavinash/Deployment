from django.shortcuts import render

# Create your views here.
def login(Req):
    return render(Req , 'login/index.html')