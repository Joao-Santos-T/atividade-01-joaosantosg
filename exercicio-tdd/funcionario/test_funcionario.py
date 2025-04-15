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
        salario_bruto = self.funcionario.calcular_salario_bruto()
        salario_base = self.funcionario.horas_trabalhadas * self.funcionario.salario_hora
        comissao = self.funcionario.valor_comissao * self.funcionario.contratos_fechados
        self.assertEqual(salario_bruto, salario_base + comissao)

    def test_calcular_salario_bruto_sem_comissao(self):
        """Testa o cálculo do salário bruto sem comissão."""
        self.funcionario.tem_comissao = False
        salario_bruto = self.funcionario.calcular_salario_bruto()
        salario_base = self.funcionario.horas_trabalhadas * self.funcionario.salario_hora
        self.assertEqual(salario_bruto, salario_base)

    def test_calcular_comissao(self):
        """Testa o cálculo da comissão."""
        comissao = self.funcionario.calcular_comissao()
        expected_comissao = self.funcionario.valor_comissao * self.funcionario.contratos_fechados
        self.assertEqual(comissao, expected_comissao)

    def test_calcular_comissao_negativa(self):
        """Testa cálculo com valor de comissão negativo."""
        self.funcionario.valor_comissao = -100.0
        with self.assertRaises(ValueError):
            self.funcionario.calcular_comissao()

    def test_calcular_custo_total(self):
        """Testa o cálculo do custo total."""
        custo_total = self.funcionario.calcular_custo_total()
        salario_bruto = self.funcionario.calcular_salario_bruto()
        self.assertEqual(custo_total, salario_bruto + self.funcionario.custo_empregador)

    def test_calcular_custo_total_sem_comissao(self):
        """Testa o cálculo do custo total sem comissão."""
        self.funcionario.tem_comissao = False
        custo_total = self.funcionario.calcular_custo_total()
        salario_base = self.funcionario.horas_trabalhadas * self.funcionario.salario_hora
        self.assertEqual(custo_total, salario_base + self.funcionario.custo_empregador)


if __name__ == "__main__":
    unittest.main() 