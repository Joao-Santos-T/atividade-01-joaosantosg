"""
Testes da classe Produto.
"""
import unittest
from datetime import datetime, timedelta

from produto import Produto


class TestProduto(unittest.TestCase):
    """Testa a classe Produto."""

    def setUp(self):
        """Configura o ambiente de teste."""
        self.data_validade = datetime.now() + timedelta(days=30)
        self.produto = Produto(
            codigo="001",
            nome="Produto Teste",
            preco=10.0,
            quantidade=5,
            data_validade=self.data_validade,
            estoque_minimo=10
        )

    def test_inicializacao(self):
        """Verifica se o produto é inicializado corretamente."""
        self.assertEqual(self.produto.codigo, "001")
        self.assertEqual(self.produto.nome, "Produto Teste")
        self.assertEqual(self.produto.preco, 10.0)
        self.assertEqual(self.produto.quantidade, 5)
        self.assertEqual(self.produto.data_validade, self.data_validade)
        self.assertEqual(self.produto.estoque_minimo, 10)

    def test_inicializacao_invalida(self):
        """Verifica se a inicialização com valores inválidos gera erro."""
        with self.assertRaises(ValueError):
            Produto("001", "Produto", -10.0)  # Preço negativo
        with self.assertRaises(ValueError):
            Produto("001", "Produto", 10.0, estoque_minimo=-5)  # Estoque mínimo negativo
        with self.assertRaises(ValueError):
            Produto("", "Produto", 10.0)  # Código vazio
        with self.assertRaises(ValueError):
            Produto("001", "", 10.0)  # Nome vazio

    def test_adicionar_estoque(self):
        """Verifica se o estoque é adicionado corretamente."""
        self.produto.adicionar_estoque(5)
        self.assertEqual(self.produto.quantidade, 10)

    def test_adicionar_estoque_negativo(self):
        """Verifica se adicionar quantidade negativa gera erro."""
        with self.assertRaises(ValueError):
            self.produto.adicionar_estoque(-5)

    def test_remover_estoque(self):
        """Verifica se o estoque é removido corretamente."""
        sucesso = self.produto.remover_estoque(3)
        self.assertTrue(sucesso)
        self.assertEqual(self.produto.quantidade, 2)

    def test_remover_estoque_insuficiente(self):
        """Verifica se remover mais que o disponível retorna False."""
        sucesso = self.produto.remover_estoque(10)
        self.assertFalse(sucesso)
        self.assertEqual(self.produto.quantidade, 5)

    def test_remover_estoque_negativo(self):
        """Verifica se remover quantidade negativa gera erro."""
        with self.assertRaises(ValueError):
            self.produto.remover_estoque(-5)

    def test_verificar_estoque_baixo(self):
        """Verifica se a detecção de estoque baixo funciona corretamente."""
        self.assertTrue(self.produto.verificar_estoque_baixo())
        self.produto.quantidade = 15
        self.assertFalse(self.produto.verificar_estoque_baixo())

    def test_calcular_valor_total(self):
        """Verifica se o valor total é calculado corretamente."""
        valor_total = self.produto.calcular_valor_total()
        self.assertEqual(valor_total, 50.0)  # 5 * 10.0

    def test_verificar_validade(self):
        """Verifica se a validação de data de validade funciona corretamente."""
        self.assertTrue(self.produto.verificar_validade())
        
        # Produto vencido
        produto_vencido = Produto(
            codigo="002",
            nome="Produto Vencido",
            preco=10.0,
            data_validade=datetime.now() - timedelta(days=1)
        )
        self.assertFalse(produto_vencido.verificar_validade())
        
        # Produto sem data de validade
        produto_sem_validade = Produto(
            codigo="003",
            nome="Produto Sem Validade",
            preco=10.0
        )
        self.assertTrue(produto_sem_validade.verificar_validade())

    def test_necessita_reposicao(self):
        """Verifica se a detecção de necessidade de reposição funciona."""
        self.assertTrue(self.produto.necessita_reposicao())
        self.produto.quantidade = self.produto.estoque_minimo + 5
        self.assertFalse(self.produto.necessita_reposicao())
        
        # Produto vencido não deve precisar de reposição
        produto_vencido = Produto(
            codigo="002",
            nome="Produto Vencido",
            preco=10.0,
            quantidade=1,
            data_validade=datetime.now() - timedelta(days=1)
        )
        self.assertFalse(produto_vencido.necessita_reposicao())


if __name__ == "__main__":
    unittest.main() 