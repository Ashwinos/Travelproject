from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import person
# Create your views here.
def demo(request):
    obj=place.objects.all()
    res=person.objects.all()
    #name="india"
    return render(request,"index.html",{'result':obj,'per':res})
#def result(request):
    #x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
    #res=x+y
    #res2=x-y
    #res3=x*y
    #res4=x//y
    #return render(request, "result.html", {'result':res,'result1':res2,'result2':res3,'result3':res4} )

