from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Record
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'pages/index.html')

#logout
def logout(request):
    auth.logout(request)
    return redirect('')
    messages.success(request,"Logout Success!")



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
            messages.success(request,"Account Created Successfully!")
            return redirect('login')
        
    context = {'form': form}
    #print(context)

    return render(request, 'pages/register.html', context=context)

@login_required(login_url="login")
def dashboard(request):

    my_records = Record.objects.all()
    context = {'Records':my_records}

    return render(request, 'pages/dashboard.html', context=context)

@login_required(login_url="login")
def create_record(request):
    form = CreateRecordForm()
    if request.method == "POST":
        form = CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"Your record was Created!")
            return redirect("dashboard")
    context = {'create_form':form}
    return render(request, 'pages/create_record.html', context=context)

@login_required(login_url="login")
def update_record(request, pk):

    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)

    # if submit
    if request.method == "POST":
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid:
            form.save()
            messages.success(request, "Your record was Updated!")
            return redirect("dashboard")
        
    # if no submitted data - send form
    context = {'update_form':form}
    return render(request,'pages/update_record.html',context=context)

# Read a single record
@login_required(login_url='login')
def singular_record(request,pk):

    one_record = Record.objects.get(id=pk)
    context = {'record':one_record}
    return render(request, 'pages/view_record.html', context=context)

@login_required(login_url='login')
def delete_record(request,pk):
    record=Record.objects.get(id=pk)
    record.delete()
    messages.success(request,"Your record was Deleted!")

    return redirect("dashboard")
