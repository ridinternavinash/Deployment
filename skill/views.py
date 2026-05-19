from django.shortcuts import render

# Create your views here.
def home(Req):
    return render(Req ,'home.html')

def img(Req):
    d={
        "name" :"Avinash" ,
        "image" :"myimage/photo.jpg",
        "video" :"myvideo/video.mp4",
        "pdf" : "mypdf/resume.pdf",
    }
    return render(Req , 'index.html' ,d)