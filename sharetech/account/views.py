from django.shortcuts import render, redirect
from .models import User, UserManager
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib import messages


def register(request):
    template = 'register.html'
    instancia = User()

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        instancia.username = request.POST['username']      
        instancia.first_name = request.POST.get('first_name')
        instancia.last_name = request.POST.get('last_name')       
        instancia.email = request.POST.get('email')

        print(request.POST.get('first_name'))
        instancia.set_password(request.POST.get('password') )
        instancia.save()

        user = authenticate(username=instancia.username, password=instancia.password)
        login(request, user)
        return redirect('core:home')

    else:
        print('fudeo')

    context = {
        'form': form,
    }
    return render(request,template)

def painel(request, pk):
    template = 'painel.html'
    query = User.objects.get(pk=pk)

    form = PainelForm(instance=query)
    form_more = PainelMoreForm(instance=query)

    context = {
        "form": form,
        "form_more":form_more,
    }
    return render(request,template,context)

def pass_change(request, pk):
    template = 'pass_change.html'
    query = User.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            if  query.check_password(form.cleaned_data.get('password')):                
                query.set_password(form.cleaned_data.get('new_password'))
                query.save()
                messages.success(request,'Senha alterada com sucesso!')
                context = {'messages': messages}

            else:
                messages.error(request,'Sua senha antiga está incorreta! Tente novamente')
                context = {'messages': messages}

    else:
        form = PasswordChangeForm ()
    context= {
        'form': form,
    }
    return render(request,template,context)