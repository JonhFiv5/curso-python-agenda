from django.contrib import admin
from .models import Categoria, Contato

# @admin.register(Contato) Tambem podemos registrar desse jeito
class ContatoAdmin(admin.ModelAdmin):

    # Campos que serao exibidos na listagem de registros
    list_display = (
        'id',
        'nome',
        'sobrenome',
        'telefone',
        'email',
        'data_criacao',
        'categoria',
        'mostrar'
    )

    # Campos clicaveis para abrir a tela de atualizacao do registro
    list_display_links = ('id','nome','sobrenome',)

    # Define o limite de registros por pagina (tabulacao)
    list_per_page = 8

    # Campos que serao buscados atraves da caixa de pesquisa
    search_fields = ('nome', 'categoria',)

    # Os campos poderao editados diretamente na lista de exibicao
    list_editable = ('telefone', 'mostrar')


# Registra os models para aparecerem na sessao administrativa
admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
