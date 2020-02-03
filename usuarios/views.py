from django.shortcuts import render
from usuarios.forms import *
from usuarios.models import *

# Create your views here.

def home(request):
    return render(request, 'base.html')

def cadastrar_empresa(request):
    form_pj = PessoaJuridicaForm(request.POST or None)
    form_endereco = EnderecoForm(request.POST or None)
    args = {
        'form_pj':form_pj,
        'form_endereco':form_endereco
    }
    if form_pj.is_valid() and form_endereco.is_valid():
        pessoa_juridica = form_pj.save()
        endereco = form_endereco.save(commit=False)
        endereco.usuario = pessoa_juridica
        endereco.save()
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
        return render(request, 'cadastro_pf.html', args)
    args = {'form':form}
    return render(request, 'cadastro_pf.html', args)

def detalhes_pessoa_fisica(request, id):
    pf = PessoaFisica.objects.get(pk=id)

    args = {'pf':pf}
    return render(request, 'detalhe_pf.html', args)

def atualizar_pessoa_fisica(request, id):
    pf = PessoaFisica.objects.get(pk = id)
    form = PessoaFisicaForm(request.POST or None, instance = pf)

    args = {'form': form}

    if form.is_valid():
        form.save()
        args = {'msg': 'Cadastro atualizado com sucesso'}
    return render(request, 'atualizar_pf.html', args)

def deletar_pessoa_fisica(request, id):
    pf = PessoaFisica.objects.get(pk=id)
    pf.delete()

    args = {
        'msg':'A pessoa foi deletada com sucesso',
        'pf':pf
        }
    return render(request, 'deletar_pf.html', args)



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
        'msg': 'A empresa foi deletado com sucesso',
        'empresa': empresa
    }

    return render(request, 'detalhe_empresa .html', args)

def avaliacao_secretaria(request):

    form = Avaliacao_SecretariaForm(request.POST or None)

    if form.is_valid():
        form.save()
        args ={
            'form':form,
            'msg':'Avaliação enviada com sucesso'
        }
        return render(request,'avaliacao_secretaria.html',args)
    args ={'form':form}
    return render(request,'avaliacao_secretaria.html',args)

def atualizar_cadastro(request, id):
    pessoafisica = PessoaFisica.objects.get(pk=id)
    form = PessoaFisicaForm(request.POST or None, instance=pessoafisica)

    args = {'form':form}

    if form.is_valid():
        form.save()
        args = {
            'msg':'Cadastro atualizado com sucesso'
        }
    return render(request, 'atualizar_cadastro.html', args)        
    
def deletar_cadastro(request, id):
    pessoafisica = PessoaFisica.objects.get(pk=id)
    pessoafisica.delete()
    args = {
        'msg':'O cadastro foi deletado com sucesso'
        'pessoafisica'
    }

    return render(request, 'deletar_cadastro.html', args)
