"""
Testes da classe Funcionario.
"""
import unittest
from unittest import TestCase

from funcionario import Funcionario


class TestFuncionario(TestCase):
    """Testes da classe Funcionario."""

    def setUp(self):
        """Configuração inicial para os testes."""
        self.funcionario_sem_comissao = Funcionario(
            nome="João Silva",
            matricula=123,
            salario_hora=50.0,
            horas_trabalhadas=160,
            custo_empregador=1000.0,
            tem_comissao=False
        )
        
        self.funcionario_com_comissao = Funcionario(
            nome="Maria Santos",
            matricula=456,
            salario_hora=50.0,
            horas_trabalhadas=160,
            custo_empregador=1000.0,
            tem_comissao=True,
            valor_comissao=200.0,
            contratos_fechados=5
        )

    def test_calcular_salario_bruto(self):
        """Testa o cálculo do salário bruto."""
        # Teste para funcionário sem comissão
        self.assertEqual(
            self.funcionario_sem_comissao.calcular_salario_bruto(),
            8000.0  # 50 * 160
        )
        
        # Teste para funcionário com comissão
        self.assertEqual(
            self.funcionario_com_comissao.calcular_salario_bruto(),
            8000.0  # 50 * 160
        )

    def test_calcular_custo_total(self):
        """Testa o cálculo do custo total."""
        # Teste para funcionário sem comissão
        self.assertEqual(
            self.funcionario_sem_comissao.calcular_custo_total(),
            9000.0  # 8000 + 1000
        )
        
        # Teste para funcionário com comissão
        self.assertEqual(
            self.funcionario_com_comissao.calcular_custo_total(),
            10000.0  # 8000 + 1000 + 1000 (comissão)
        )

    def test_calcular_comissao(self):
        """Testa o cálculo da comissão."""
        # Teste para funcionário sem comissão
        self.assertEqual(
            self.funcionario_sem_comissao.calcular_comissao(),
            0.0
        )
        
        # Teste para funcionário com comissão
        self.assertEqual(
            self.funcionario_com_comissao.calcular_comissao(),
            1000.0  # 200 * 5
        )


if __name__ == "__main__":
    unittest.main() 