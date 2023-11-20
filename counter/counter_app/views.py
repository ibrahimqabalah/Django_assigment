from django.shortcuts import render,HttpResponse

# Create your views here.
def method1(request):
    return HttpResponse("hellowwwwwwwwwww")


count = 0  # Counter variable

def index(request):
    if 'count' not in request.session:
        request.session['count']=1
    else:
        request.session['count']+=1
    return render(request,'root_route.html')
   