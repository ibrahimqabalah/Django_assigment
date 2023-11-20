from django.shortcuts import render,HttpResponse,redirect
import random 
# Create your views here.
def method1(request):
    return HttpResponse("heloooooooooooooooooo")

# generating random number(1,100)

def index(request):
    if 'target_number' not in request.session:
        request.session['target_number']=random.randint(1, 100)
        print('meeeeeeeeeee')
    return render(request,'guess_number.html')

def guess_num(request):
    print('hiii')
    if request.method == 'POST':
        guess =int(request.POST['guess'])
        print('guess')
        if guess > request.session['target_number']:
            print('helloooooooooooo')
            request.session['result']='Too high!'
        elif guess < request.session['target_number']:
            request.session['result']='Too low!'
        else:
            request.session['result']= 'correct' 
        print (request.session['result'])  
         
    return redirect("/")
def play_again(request):
    request.session.flush()
    return redirect("/")