from django.shortcuts import render,HttpResponse
from time import gmtime,strftime
# Create your views here.
def method1(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'time.html',context)
