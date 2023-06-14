from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from todolist.tarefas.forms import TarefaNovaForm, TarefaForm
from django.urls import reverse

from todolist.tarefas.models import Tarefa


def home(request):
    tarefas_pendentes = Tarefa.objects.filter(feita=False).all()
    tarefas_feitas = Tarefa.objects.filter(feita=True).all()
    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tarefas:home'))
        else:
            return render(
                request, 'tarefas/home.html',
                {
                    'form': form,
                    'tarefas_pendentes': tarefas_pendentes,
                    'tarefas_feitas': tarefas_feitas
                },
                status=400)
    return render(
        request, 'tarefas/home.html',
        {
          'tarefas_pendentes': tarefas_pendentes,
          'tarefas_feitas': tarefas_feitas,
        }
        )


def detalhe(request, tarefa_id):
    if request.method == 'POST':
        tarefa = Tarefa.objects.get(id=tarefa_id)
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('tarefas:home'))


def apagar(request, tarefa_id):
    if request.method == 'POST':
        Tarefa.objects.filter(id=tarefa_id).delete()
    return HttpResponseRedirect(reverse('tarefas:home'))
