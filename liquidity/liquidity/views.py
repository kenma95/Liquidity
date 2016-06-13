from django.shortcuts import render_to_response,render,get_object_or_404    
from django.http import HttpResponse, HttpResponseRedirect    
from django.contrib.auth.models import User    
from django.contrib import auth  
from django.contrib import messages  
from django.template.context import RequestContext  
  
from django.forms.formsets import formset_factory  
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage  
  
from django.contrib.auth.decorators import login_required  
  
from .forms import LoginForm,RegForm 
from django.contrib.auth import logout


def index(request):
    return render(request, 'index.html', {})


def register(request):
    if request.method == 'GET':  
        form = RegForm()  
        return render_to_response('register.html', RequestContext(request, {'form': form,}))  
    else:  
        form = RegForm(request.POST)  
        if form.is_valid():  
            username = request.POST.get('username', '')  
            password = request.POST.get('password', '')  
            if not User.objects.filter(username=username).exists() : 
                user = User.objects.create_user(username,password=password)
                user.save()
                return render_to_response('index.html', RequestContext(request))  
            else:  
                return render_to_response('register.html', RequestContext(request, {'form': form,'already_existed':True}))  
        else:  
            return render_to_response('register.html', RequestContext(request, {'form': form,}))


def login(request):  
    if request.method == 'GET':  
        form = LoginForm()  
        return render_to_response('login.html', RequestContext(request, {'form': form,}))  
    else:  
        form = LoginForm(request.POST)  
        if form.is_valid():  
            username = request.POST.get('username', '')  
            password = request.POST.get('password', '')  
            user = auth.authenticate(username=username, password=password)  
            if user is not None and user.is_active:  
                auth.login(request, user)  
                return render_to_response('index.html', RequestContext(request))  
            else:  
                return render_to_response('login.html', RequestContext(request, {'form': form,'password_is_wrong':True}))  
        else:  
            return render_to_response('login.html', RequestContext(request, {'form': form,}))  


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

