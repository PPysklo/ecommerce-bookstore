import sweetify
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, ProfileForm
from .models import Profile
from app_books.models import Tag, OrderItem, Order
# from .models import User
User = get_user_model()

def statute(request):
    return render(request, 'statute.html')

def loginRegister(request):
    form = CustomUserCreationForm()
    
    if request.method == "POST" and 'login' in request.POST:
        page = 'login'
        if request.user.is_authenticated:
            return redirect('app_books:books-list')

        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'Username does not exist.')
            return redirect('app_users:login-register') 

        user = authenticate(request, username=user.username, password=password)  

        if user is not None:
            login(request, user)
            messages.success(request, message="zalogowano")

            return redirect(request.GET.get('next', 'app_books:books-list'))
        else:
            messages.error(request, 'Username or password is incorrect.')
                  
        # else:
        #     messages.error(request, 'Captcha')
    elif request.method == "POST" and 'register' in request.POST:
        
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            # captcha = CaptchaForm(request.POST)
            if form.is_valid(): #and captcha.is_valid():

                user = form.save(commit=False)
                user.email = user.email.lower()
                user.username = user.email
                user.save()

                messages.success(request, 'User account was created!')
                    
                login(request, user)
                return redirect('app_books:books-list')
                
            else:
                messages.success(request, 'An error has occurred during registration')

    context = {'form': form} #,'captcha':captcha}
            
    return render(request, 'app_users/login_register.html', context)

def logOut(request):
    
    logout(request) 
    messages.info(request,'User was logget out')
    
    return redirect('app_books:books-list')

@login_required(login_url="app_user:login")
def profile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)

    orders = Order.objects.filter(customer=profile, complete=True).prefetch_related('orderitem_set')

    context = {
        'profile': profile, 
        'orders': orders
    }
    
    return render(request, 'app_users/profile.html', context)

@login_required(login_url="app_user:login")
def edit_profile(request, pk):
    tags = Tag.objects.all()
    
    profile = get_object_or_404(Profile, id=pk)
    
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            
            profile = form.save(commit=False)
            profile.save()


        return redirect('app_users:profile')

    context = {'form': form, 'tags':tags}
    return render(request, 'app_users/profile_edit.html', context)
