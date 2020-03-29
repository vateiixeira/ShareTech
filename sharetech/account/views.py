from django.shortcuts import render, redirect
from .models import User, UserManager
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib import messages
import time
import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


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

@login_required
def painel(request, pk):
    template = 'painel.html'

    print(pk)
    print(request.user.pk)
    if request.user.pk == pk:        
        model_more = UserMore()

        if request.method == 'POST':
            dat_form_more = json.loads(request.body.decode('utf-8'))
            model_more.user = request.user
            model_more.rua = dat_form_more.get("logradouro")
            model_more.num_rua = dat_form_more.get("numero")
            model_more.bairro = dat_form_more.get("bairro")
            model_more.cep = dat_form_more.get("cep")
            model_more.fone = dat_form_more.get("fone")
            model_more.save() 
            print(model_more.rua)
            # form = PainelForm(request.POST,instance=query)
            # if form.is_valid():
            #     form.save()
        # else:
        #     form = PainelForm(instance=query)

        # context = {

        # }
    else:
        return redirect('account:error_404')
    return render(request,template)

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



@csrf_exempt
def login_page(request):
    template = 'login.html'

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')        
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('core:home')
        else:
            messages.error(request,'Usuário ou senha inválidos.')        

    return render(request, template)

def error_404(request):
    template='404.html'
    return render(request,template)