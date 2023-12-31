from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login

# Create your views here.


def index(request):
    
    return render(request, 'index.html')


def login_user(request):
    
    if request.method == "POST":
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('admin/')
        else:
            # Return an 'invalid login' error message.
            return('')
    else:
        return render(request, 'index.html')