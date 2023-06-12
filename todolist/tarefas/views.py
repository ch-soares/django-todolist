from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from todolist.tarefas.forms import TarefaNovaForm
from django.urls import reverse

from todolist.tarefas.models import Tarefa


def home(request):
    tarefas_pendentes = Tarefa.objects.filter(feita=False).all()
    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tarefas:home'))
        else:
            return render(request, 'tarefas/home.html', {'form': form, 'tarefas_pendentes': tarefas_pendentes}, status=400)
    return render(request, 'tarefas/home.html', {'tarefas_pendentes': tarefas_pendentes})
