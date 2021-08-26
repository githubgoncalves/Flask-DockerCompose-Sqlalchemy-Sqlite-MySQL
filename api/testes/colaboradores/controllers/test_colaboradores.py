import os
import tempfile
import pytest

from api.app import app

@pytest.fixture
def colaboradores():
    app.config['TESTING'] = True
    colaboradores = app.test_client()
    yield colaboradores

def test_valid_transaction(colaboradores):
    retorno = colaboradores.get("/api/colaboradores")    
    assert  "API de Colaboradores Disponivel!" == retorno.get_json()
