from django.shortcuts import render,HttpResponse

# Create your views here.
def method1(request):
    return HttpResponse()

def display_form(request):
    return render(request,"dojo.html")
def handle_form(request):
    context={
        'names':request.POST['Your Name'],
        'locations':request.POST['location'],
        'favorites':request.POST['Favorite'],
        'commnets':request.POST['Comment'],
    }
    return render(request,"results.html",context)
