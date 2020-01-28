from django.shortcuts import render
from usuarios.forms import PessoaJuridicaForm
from usuarios.models import PessoaJuridica
# Create your views here.

def cadastro_empresa(request):
    form = PessoaJuridicaForm(request.POST or None)
    args = {
        'form':form
    }
    if form.is_valid():
        form.save()
        args = {
            'msg': 'Cadastro realizado com sucesso'
        }
        return render(request, 'cadastro_empresa.html', args)
    return render(request, 'cadastro_empresa.html', args)

def cadastrar_pessoa_fisica(request):
    form = PessoaFisicaForm(request.POST or None)
    if form.is_valid():
        form.save()
        args = {
             'form': form, 
             'msg': 'Cadastro foi realizado com sucesso!'
        }
        render(request, 'cadastro.html', args)
        args = {'form': form}
        return render('request.cadastro.html', args)
        args = {form'form'}
