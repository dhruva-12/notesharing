from django.contrib.auth.models import User,auth
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .models import Note
from django.core.files.storage import FileSystemStorage
from .forms import NoteForm
from django.views.generic.edit import CreateView

def index(request):
    return render(request,'index.html')
def notesadd(request):
    form = NoteForm(request.POST,request.FILES)
    if request.method =='POST':
        if form.is_valid():
           
            form.save()
            return redirect('notesedit')
    else:
        form = NoteForm()
        
    context = {
        'form': form
    }       
    return render(request, 'notes.html', context)
    
    
def notesshow(request):
    notes = Note.objects.all()
    return render(request, 'notesshow.html',{'notes':notes})


def notesedit(request,id):
    notes = Note.objects.get(id=id)
    form = NoteForm(request.POST,instance=notes)
    if form.is_valid():
        form.save(commit=True)
    return render(request, 'notesedit.html',{'notes':notes})
   
def logoutpage(request):
    logout(request)
    return render(request,'logout.html')
def navigation(request):
    return render(request,'navigation.html')
def loginpage(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request , username=username,password=password)
        if user is not None:
            #login(request,username)
            return redirect('index')
        else:
            messages.info(request,'username or password is incorrect')
    context={}
    return render(request, 'registration/login.html')

   
def signup(request):
    context = {}
    form =  CreateUserForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account created successfully')
            return render(request,'index.html')
    context['form']=form
    return render(request,'registration/signup.html',context)
    
    


    
        
   
