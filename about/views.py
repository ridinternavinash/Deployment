from django.shortcuts import render

# Create your views here.
def about(Req):
    return render(Req ,'about/index1.html')