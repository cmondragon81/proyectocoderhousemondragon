from django.shortcuts import redirect, render
from django.contrib.auth import login as django_login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def index(request):
    

    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user = authenticate(username=username,password=password)

            if user is not None:
                django_login(request, user=user)
                return render(request,'home.html',{})
            else:
                return render(request,'index.html',{'form':form})

        else:
            return render (request,'index.html',{'form':form, 'msg':'Error de autenticacion'})
    else:
# django_login, authenticate, AuthenticationForm
        form=AuthenticationForm()
        return render (request, 'index.html', {'form':form, 'msg':'Error de login'})

def home(request):
    return render (request, 'home.html', {})

# def logout(request):
#     return redirect('index.html',{})