from django.db.models import Model, DO_NOTHING
from django.db.models import CharField, DateTimeField, ForeignKey,\
    BooleanField, ImageField
from django.utils.timezone import now


class Categoria(Model):
    nome = CharField(max_length=255)

    def __str__(self) -> str:
        return self.nome


class Contato(Model):
    nome = CharField(max_length=255)
    sobrenome = CharField(max_length=255, blank=True)
    telefone = CharField(max_length=40)
    email = CharField(max_length=255, blank=True)
    data_criacao = DateTimeField(null=True, default=now)
    descricao = CharField(max_length=500, blank=True, null=True)
    mostrar = BooleanField(default=True)
    categoria = ForeignKey(Categoria, on_delete=DO_NOTHING)
    # O atributo upload_to especifica o caminho (dentro de media/)
    foto = ImageField(blank=True, upload_to='fotos/%Y/%m') 

    def __str__(self) -> str:
        return f'{self.nome} {self.sobrenome}'
