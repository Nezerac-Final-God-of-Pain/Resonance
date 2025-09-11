from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from .models import Record
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'pages/index.html')

#logout
def logout(request):
    auth.logout(request)
    return redirect('login')



def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            
    context = {'form': form}
    return render(request, 'pages/login.html', context = context)

# Register a user
def register(request):
    # make a form from forms.py
    form = CreateUserForm()

    if request.method == "POST":
        # make a form with the users submitted data
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save() # save to database
            return redirect('')
        
    context = {'form': form}
    #print(context)

    return render(request, 'pages/register.html', context=context)

@login_required(login_url = 'login')
def dashboard(request):

    my_records = Record.objects.all()
    context = {'records': my_records}

    return render(request, 'website/dashboard.html', context=context)
 