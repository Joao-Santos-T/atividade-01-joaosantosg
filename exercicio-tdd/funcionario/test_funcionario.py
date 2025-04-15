"""
Testes da classe Funcionario.
"""
import unittest

from funcionario import Funcionario


class TestFuncionario(unittest.TestCase):
    """Testes da classe Funcionario."""

    def setUp(self):
        self.funcionario = Funcionario(
            nome="Joao Vitor",
            matricula=1121,
            salario_hora=1000,
            horas_trabalhadas=160,
            custo_empregador=100,
            tem_comissao=True,
            valor_comissao=100,
            contratos_fechados=10
        )

    def test_calcular_salario_bruto(self):
        """Testa o cálculo do salário bruto."""
        salario_bruto = self.funcionario.horas_trabalhadas * self.funcionario.salario_hora
        if self.funcionario.tem_comissao:
            comissao = self.funcionario.valor_comissao * self.funcionario.contratos_fechados
            salario_bruto += comissao
        return salario_bruto

    def test_calcular_comissao(self):
        """Testa o cálculo da comissão."""
        return self.funcionario.valor_comissao * self.funcionario.contratos_fechados

    def testar_salario_negativo(self):
        """Testa cálculo com valor de comissão negativo."""
        self.funcionario.valor_comissao = -100.0
        with self.assertRaises(ValueError):
            self.funcionario.calcular_comissao()

if __name__ == "__main__":
    unittest.main() 