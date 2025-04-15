"""
Testes da classe Aluno.
"""
import unittest

from aluno import Aluno


class TestAluno(unittest.TestCase):
    """Testes da classe Aluno."""

    def setUp(self):
        self.aluno = Aluno(
            nome="Joao Silva",
            matricula="2023001",
            notas={
                "Matemática": [8.5, 7.0, 9.0],
                "Português": [7.0, 8.0, 6.5]
            },
            faltas={
                "Matemática": 2,
                "Português": 1
            }
        )

    def test_adicionar_nota(self):
        """Testa a adição de uma nova nota."""
        self.aluno.adicionar_nota("Matemática", 8.0)
        self.assertIn(8.0, self.aluno.notas["Matemática"])

    def test_adicionar_nota_nova_disciplina(self):
        """Testa a adição de uma nota em uma nova disciplina."""
        self.aluno.adicionar_nota("História", 7.5)
        self.assertIn(7.5, self.aluno.notas["História"])

    def test_adicionar_nota_invalida(self):
        """Testa a adição de uma nota inválida."""
        with self.assertRaises(ValueError):
            self.aluno.adicionar_nota("Matemática", -1.0)
        with self.assertRaises(ValueError):
            self.aluno.adicionar_nota("Matemática", 11.0)

    def test_adicionar_nota_disciplina_invalida(self):
        """Testa a adição de nota em disciplina com nome inválido."""
        with self.assertRaises(ValueError):
            self.aluno.adicionar_nota("", 7.0)

    def test_calcular_media(self):
        """Testa o cálculo da média de uma disciplina."""
        media = self.aluno.calcular_media("Matemática")
        expected_media = (8.5 + 7.0 + 9.0) / 3
        self.assertEqual(media, expected_media)

    def test_calcular_media_disciplina_sem_notas(self):
        """Testa o cálculo da média de uma disciplina sem notas."""
        with self.assertRaises(ValueError):
            self.aluno.calcular_media("História")

    def test_verificar_aprovacao(self):
        """Testa a verificação de aprovação."""
        self.assertTrue(self.aluno.verificar_aprovacao("Matemática"))

    def test_verificar_aprovacao_reprovado(self):
        """Testa a verificação de reprovação."""
        self.aluno.notas["Matemática"] = [4.0, 3.0, 5.0]
        self.assertFalse(self.aluno.verificar_aprovacao("Matemática"))

    def test_registrar_falta(self):
        """Testa o registro de uma falta."""
        faltas_iniciais = self.aluno.faltas["Matemática"]
        self.aluno.registrar_falta("Matemática")
        self.assertEqual(self.aluno.faltas["Matemática"], faltas_iniciais + 1)

    def test_registrar_falta_nova_disciplina(self):
        """Testa o registro de uma falta em uma nova disciplina."""
        self.aluno.registrar_falta("História")
        self.assertEqual(self.aluno.faltas["História"], 1)

    def test_registrar_falta_disciplina_invalida(self):
        """Testa o registro de falta em disciplina com nome inválido."""
        with self.assertRaises(ValueError):
            self.aluno.registrar_falta("")

    def test_calcular_frequencia(self):
        """Testa o cálculo da frequência."""
        total_aulas = 20
        frequencia = self.aluno.calcular_frequencia("Matemática", total_aulas)
        expected_frequencia = ((total_aulas - 2) / total_aulas) * 100
        self.assertEqual(frequencia, expected_frequencia)

    def test_calcular_frequencia_disciplina_sem_faltas(self):
        """Testa o cálculo da frequência em uma disciplina sem faltas."""
        total_aulas = 20
        frequencia = self.aluno.calcular_frequencia("História", total_aulas)
        self.assertEqual(frequencia, 100.0)

    def test_calcular_frequencia_total_aulas_invalido(self):
        """Testa o cálculo da frequência com total de aulas inválido."""
        with self.assertRaises(ValueError):
            self.aluno.calcular_frequencia("Matemática", 0)
        with self.assertRaises(ValueError):
            self.aluno.calcular_frequencia("Matemática", -10)

    def test_obter_disciplinas(self):
        """Testa a obtenção da lista de disciplinas."""
        disciplinas = self.aluno.obter_disciplinas()
        self.assertEqual(set(disciplinas), {"Matemática", "Português"})

    def test_calcular_media_geral(self):
        """Testa o cálculo da média geral do aluno."""
        media_geral = self.aluno.calcular_media_geral()
        media_mat = (8.5 + 7.0 + 9.0) / 3
        media_port = (7.0 + 8.0 + 6.5) / 3
        expected_media = (media_mat + media_port) / 2
        self.assertEqual(media_geral, expected_media)

    def test_calcular_media_geral_sem_notas(self):
        """Testa o cálculo da média geral sem notas."""
        aluno_sem_notas = Aluno("Maria", "2023002")
        with self.assertRaises(ValueError):
            aluno_sem_notas.calcular_media_geral()


if __name__ == "__main__":
    unittest.main() 