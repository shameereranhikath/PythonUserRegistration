from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userregistration:index')
    else:
        form=UserCreationForm()
        return render(request,'signup.html',{'form':form})
