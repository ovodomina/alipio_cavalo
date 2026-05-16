import sys
import os
import pytest
# Adiciona a pasta raiz do projeto ao sys.path dinamicamente
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.app import calcular_imc
def test_imc_correto():
    assert calcular_imc(70, 1.75) == 22.86