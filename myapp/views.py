from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
def myfunctioncall(request):
    return HttpResponse("hello world!")
def myfunctionabout(request):
    return HttpResponse("About Response")
def add(request,a,b):
    return HttpResponse(a+b)
def intro(request,name,age):
    mydictionary={
        "name":name,
        "age":age,
    }
    return JsonResponse(mydictionary)
def myfirstpage(request):
    return render(request,'index.html')
def mysecondpage(request):
    return render(request,'second.html')
def mythirdpage(request):
    var="henlo"
    greeting="hello hi kemcho"
    fruits=["mango","pineapple","chikoo"]
    num1,num2=7,10
    ans=num1>num2
    mydictionary={
        "var":var,
        "msg":greeting,
        "myfruits":fruits,
        "num1":num1,
        "num2":num2,
        "ans":ans
    }
    return render(request,'third.html',context=mydictionary)
def myimagepage(request):
    return render(request,'myimage.html')
def myimagepage1(request,imagename):
    imagename=str(imagename).lower()
    if imagename=='django':
        var=True
    else:
        var=False
    mydictionary={
        "var":var
    }
    return render(request,"myimage1.html",context=mydictionary)
    