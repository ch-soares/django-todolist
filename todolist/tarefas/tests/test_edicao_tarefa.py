import pytest
from django.urls import reverse
from todolist.tarefas.models import Tarefa


@pytest.fixture
def tarefa_pendente(db):
    return Tarefa.objects.create(nome='Tarefa 1', feita=False)


@pytest.fixture
def resposta_com_tarefa_pendente(client, tarefa_pendente):
    resp = client.post(
        reverse('tarefas:detalhe', kwargs={'tarefa_id': tarefa_pendente.id}),
        data={'feita': 'True', 'nome': f'{tarefa_pendente.nome}-editada'}
    )
    return resp


def test_tarefa_feita(resposta_com_tarefa_pendente):
    assert Tarefa.objects.first().feita


def test_status_code_redirect(resposta_com_tarefa_pendente):
    assert resposta_com_tarefa_pendente.status_code == 302
