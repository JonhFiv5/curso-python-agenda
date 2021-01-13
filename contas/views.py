from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import FormContato

# from django.contrib.auth.hashers import check_password, make_password

def login(request):
    if request.method != 'POST':
        return render(request, 'contas/login.html')
    
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    if not usuario or not senha:
        messages.error(
            request, 
            'Você precisa informar o nome de usuário e a senha.'
        )
        return render(request, 'contas/login.html')
    
    user = auth.authenticate(request, username=usuario, password=senha)
    if user is None:
        messages.error(request, 'Usuário e/ou senha inválidos.')
        return render(request, 'contas/login.html')
    else:
        auth.login(request, user)
        messages.success(request, f'Você fez login com sucesso.')
        return redirect('dashboard')



def logout(request):
    auth.logout(request)
    return redirect('dashboard')


def cadastro(request):
    if request.method != 'POST':
        return render(request, 'contas/cadastro.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha_a = request.POST.get('senha_a')
    senha_b = request.POST.get('senha_b')

    if not email or not nome or not sobrenome or not usuario \
            or not senha_a or not senha_b:
        messages.error(request, 'Preencha todos os campos.')
        return render(request, 'contas/cadastro.html')
    try:
        validate_email(email)
    except ValidationError:
        messages.error(request, 'O e-mail informado é inválido.')
        return render(request, 'contas/cadastro.html')

    if len(senha_a) < 6:
        messages.error(request, 'A senha precisa ter no mínimo 6 caracteres.')
        return render(request, 'contas/cadastro.html')

    if senha_a != senha_b:
        messages.error(request, 'As senhas digitadas são diferentes.')
        return render(request, 'contas/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'O nome de usuário informado já está em uso.')
        return render(request, 'contas/cadastro.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'O e-mail informado já está em uso.')
        return render(request, 'contas/cadastro.html')
    
    user = User.objects.create_user(
        first_name=nome, last_name=sobrenome, email=email,
        username=usuario, password=senha_a
    )
    user.save()

    messages.success(
        request,
        'Cadastro realizado com sucesso. Você já pode fazer login.'
    )
    return redirect('login')


@login_required(redirect_field_name='login')
def dashboard(request):
    formulario = FormContato()
    return render(request, 'contas/dashboard.html', {'form': formulario})


def salvar_contato(request):
    form = FormContato(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Verifique as informações.')

        formulario = FormContato(request.POST)
        return render(
            request,
            'contas/dashboard.html',
            {'form': formulario}
        )

    # Validacao manual (exemplo)
    descricao = request.POST.get('descricao')
    if len(descricao) < 5:
        messages.error(
            request,
            'A descrição precisa ter no mínimo 5 caracteres.'
        )

        formulario = FormContato(request.POST)
        return render(
            request,
            'contas/dashboard.html',
            {'form': formulario}
        )

    form.save()
    messages.success(
        request,
        f'Contato {request.POST.get("nome")} salvo com sucesso'
    )
    return redirect('dashboard')
