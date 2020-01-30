from django.shortcuts import render
from usuarios.forms import *
from usuarios.models import *
# Create your views here.

def cadastrar_empresa(request):
    form = PessoaJuridicaForm(request.POST or None)
    args = {
        'form':form
    }
    if form.is_valid():
        form.save()
        args = {
            'msg': 'Cadastro realizado com sucesso'
        }
        return render(request, 'cadastro_pj.html', args)
    return render(request, 'cadastro_pj.html', args)

def cadastrar_pessoa_fisica(request):
    form = PessoaFisicaForm(request.POST or None)
    if form.is_valid():
        form.save()
        args = {
            'form':form,
            'msg':'O cadastro foi realizado com sucesso'
        }
        return render(request, 'cadastro.html', args)
    args = {'form':form}
    return render(request, 'cadastro.html', args)

def acessibilidade_cadastro(request): 

    form = AcessibilidadeForm(request.POST or None)

    if form.is_valid():
        form.save()
        args ={
            'form':form,
            'msg':'O cadastro foi realizado com sucesso'

        }
        return render(request,'acessibilidade.html',args)
    args ={'form':form}
    return render(request,'acessibilidade.html',args)

def editar_empresa(request, id):
    empresa = Empresa.objects.get(pk=id)
    form = PessoaFisicaForm(request.POST or None, instance=empresa)
    
    args = {
        'form':form
    }

    if form.is_valid():
        form.save()
        args = {
            'msg': 'Empresa atualizada com sucesso.'
        }

    return render(request, 'edicao_empresa.html', args)

def detalhar_empresa(request, id):
    empresa = Empresa.objects.get(pk=id)

    args = {
        'empresa': empresa
    }
    
    return render(request, 'detalhe_empresa.html', args)

def remover_empresa(request, id):
    empresa = Empresa.objects.get(pk=id)
    empresa.delete()

    args = {
        'msg': 'O aluno foi deletado com sucesso',
        'empresa': empresa
    }

    return render(request, 'detalhe_empresa .html', args)