from django.shortcuts import render
from .models import reg
# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def save(request):
    if request.method=="POST":
        nm=request.POST["nm"]
        em=request.POST["em"]
        cn=request.POST["cn"]
        age=request.POST["age"]
        reg(name=nm,email=em,contact=cn,age=age).save()
        msg="Registration done"
        return render(request,"about.html",{'msg':msg})
