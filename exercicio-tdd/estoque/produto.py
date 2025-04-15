"""
Sistema de controle de estoque.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Produto:
    """Representação básica de um produto no estoque."""

    codigo: str
    nome: str
    preco: float
    quantidade: int = 0
    data_validade: Optional[datetime] = None
    estoque_minimo: int = 10

    def __post_init__(self):
        """Valida os dados do produto após a inicialização."""
        if not self.codigo:
            raise ValueError("Código do produto não pode ser vazio")
        if not self.nome:
            raise ValueError("Nome do produto não pode ser vazio")
        if self.preco < 0:
            raise ValueError("Preço do produto não pode ser negativo")
        if self.estoque_minimo < 0:
            raise ValueError("Estoque mínimo não pode ser negativo")

    def adicionar_estoque(self, quantidade: int) -> None:
        """Adiciona quantidade ao estoque do produto."""
        if quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa")
        self.quantidade += quantidade

    def remover_estoque(self, quantidade: int) -> bool:
        """Remove quantidade do estoque do produto."""
        if quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa")
        if quantidade > self.quantidade:
            return False
        self.quantidade -= quantidade
        return True

    def verificar_estoque_baixo(self) -> bool:
        """Verifica se o estoque está abaixo do mínimo."""
        return self.quantidade < self.estoque_minimo

    def calcular_valor_total(self) -> float:
        """Calcula o valor total do produto em estoque."""
        return self.quantidade * self.preco

    def verificar_validade(self) -> bool:
        """Verifica se o produto está dentro da validade."""
        if self.data_validade is None:
            return True
        return datetime.now() <= self.data_validade

    def necessita_reposicao(self) -> bool:
        """Verifica se o produto necessita de reposição.
        
        Um produto necessita de reposição se:
        1. Está dentro da validade (ou não tem data de validade)
        2. Está com estoque baixo
        """
        return self.verificar_validade() and self.verificar_estoque_baixo() 