import sweetify
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import get_user_model

from .forms import CustomUserCreationForm #CaptchaForm
from .models import Profile
# from .models import User
User = get_user_model()



def loginRegister(request):
    form = CustomUserCreationForm()
    # captcha = CaptchaForm()
    
    
    if request.method == "POST" and 'login' in request.POST :

        page = 'login'
        
        if request.user.is_authenticated:
            return redirect('stuff:stuff_list')

        # captcha = CaptchaForm(request.POST)
        # if captcha.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
                
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exits')
                    
        user = authenticate(request, username=username, password=password)

        messages.success(request, 'Username does not exits')
        if user is not None:
            
            login(request,user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'stuff:stuff_list')
        else:
            messages.error(request,'Username or password is incorrect.')
                  
        # else:
        #     messages.error(request, 'Captcha')
    elif request.method == "POST" and 'register' in request.POST:
        
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            # captcha = CaptchaForm(request.POST)
            if form.is_valid(): #and captcha.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()

                messages.success(request, 'User account was created!')
                    
                login(request, user)
                return redirect('stuff:stuff_list')
                
            else:
                messages.success(request, 'An error has occurred during registration')

    context = {'form': form} #,'captcha':captcha}
            
    return render(request, 'users/loginRegister.html', context)
            



def logOut(request):
    
    logout(request) 
    messages.info(request,'User was logget out')
    
    return redirect('stuff:stuff_list')
