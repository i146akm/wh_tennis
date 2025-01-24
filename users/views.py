from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
def login_users(request):
    if not request.user.is_authenticated:
        form = LoginForm()
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid() and form.check_account():
                try:
                    is_active = models.IsActive.objects.get(user=form.check_account())
                    return redirect('/login/')
                        

                except models.IsActive.DoesNotExist:
                    user = authenticate(request, username=form.cleaned_data["username"], password=form.cleaned_data["password"])
                    if user is not None:
                        auth_login(request, user)
                        is_active_model = models.IsActive(
                            user=user,
                            user_agent=request.META.get('HTTP_USER_AGENT', ''),
                            is_active=True
                        )
                        is_active_model.save()
                        return redirect('/')
            else:
                return redirect('/login')
                
        return render(request=request, template_name='login.html', context={
            'form': form
        })
    
    else:
        return redirect('/')

@login_required(login_url='/login')
def logout(request):
    try:
        user = models.IsActive.objects.get(
            user=request.user,
            user_agent=request.META.get('HTTP_USER_AGENT', ''),
            is_active=True
        )
        if user:
            user.delete()
            auth_logout(request)
            return redirect('/login/')
        
    except IsActive.DoesNotExist:
        auth_logout(request)
        return redirect('/login/')