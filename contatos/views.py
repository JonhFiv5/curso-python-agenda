from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from .models import Contato
from django.contrib import messages

def index(request):
    lista = Contato.objects.order_by('-id').exclude(mostrar=False)

    paginator = Paginator(lista, 20)
    numero_pag = request.GET.get('page')
    obj_pag = paginator.get_page(numero_pag)
    
    return render(
        request, 'contatos/index.html',
        {'contatos':obj_pag}
    )


def ver_contato(request, id):
    contato = get_object_or_404(Contato, id=id, mostrar=True)
    return render(request, 'contatos/detalhes.html', {'contato': contato})


def busca(request):
    termo = request.GET.get('termo')
    if termo is None or not termo:
        messages.error(request, 'Você precisa digitar um termo na busca.')
        return redirect('index')
        # raise Http404()
    nome_completo = Concat('nome', Value(' '), 'sobrenome')
    lista = Contato.objects.annotate(nome_completo=nome_completo)\
        .filter(
            Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo),
            mostrar=True
        ).order_by('-id')
    # Imprime a consulta SQL que é realizada
    # print(lista.query)

    paginator = Paginator(lista, 20)
    numero_pag = request.GET.get('page')
    obj_pag = paginator.get_page(numero_pag)
    
    return render(
        request, 'contatos/busca.html',
        {'contatos':obj_pag}
    )
