from django.contrib import admin
from usuarios.models import *

admin.site.register(PessoaFisica)
admin.site.register(PessoaJuridica)
admin.site.register(Endereco)
admin.site.register(Acessibilidade)