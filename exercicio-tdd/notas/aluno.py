"""
Sistema de gerenciamento de notas escolares.
"""
from dataclasses import dataclass
from typing import Dict, List, Set


@dataclass
class Aluno:
    """Representação de um aluno no sistema de notas.
    
    Attributes:
        nome: Nome do aluno
        matricula: Número de matrícula do aluno
        notas: Dicionário com as notas por disciplina
        faltas: Dicionário com o número de faltas por disciplina
    """

    nome: str
    matricula: str
    notas: Dict[str, List[float]] = None  # Disciplina -> Lista de notas
    faltas: Dict[str, int] = None  # Disciplina -> Número de faltas

    def __post_init__(self):
        """Inicializa os dicionários se não forem fornecidos."""
        if self.notas is None:
            self.notas = {}
        if self.faltas is None:
            self.faltas = {}

    def _validar_disciplina(self, disciplina: str) -> None:
        """Valida o nome da disciplina."""
        if not disciplina:
            raise ValueError("Nome da disciplina não pode ser vazio")

    def adicionar_nota(self, disciplina: str, nota: float) -> None:
        """Adiciona uma nota para uma disciplina específica."""
        self._validar_disciplina(disciplina)
        if nota < 0 or nota > 10:
            raise ValueError("Nota deve estar entre 0 e 10")
        if disciplina not in self.notas:
            self.notas[disciplina] = []
        self.notas[disciplina].append(nota)

    def calcular_media(self, disciplina: str) -> float:
        """Calcula a média das notas de uma disciplina."""
        self._validar_disciplina(disciplina)
        if disciplina not in self.notas or not self.notas[disciplina]:
            raise ValueError(f"Disciplina {disciplina} não possui notas registradas")
        return sum(self.notas[disciplina]) / len(self.notas[disciplina])

    def verificar_aprovacao(self, disciplina: str) -> bool:
        """Verifica se o aluno está aprovado em uma disciplina."""
        media = self.calcular_media(disciplina)
        return media >= 6.0

    def registrar_falta(self, disciplina: str) -> None:
        """Registra uma falta em uma disciplina."""
        self._validar_disciplina(disciplina)
        if disciplina not in self.faltas:
            self.faltas[disciplina] = 0
        self.faltas[disciplina] += 1

    def calcular_frequencia(self, disciplina: str, total_aulas: int) -> float:
        """Calcula a frequência do aluno em uma disciplina."""
        self._validar_disciplina(disciplina)
        if total_aulas <= 0:
            raise ValueError("Total de aulas deve ser maior que zero")
        if disciplina not in self.faltas:
            return 100.0
        faltas = self.faltas[disciplina]
        return ((total_aulas - faltas) / total_aulas) * 100

    def obter_disciplinas(self) -> Set[str]:
        """Retorna o conjunto de todas as disciplinas do aluno."""
        return set(self.notas.keys() | self.faltas.keys())

    def calcular_media_geral(self) -> float:
        """Calcula a média geral do aluno considerando todas as disciplinas.
        
        Returns:
            float: Média geral do aluno
            
        Raises:
            ValueError: Se o aluno não tiver notas registradas
        """
        disciplinas = self.obter_disciplinas()
        if not disciplinas:
            raise ValueError("Aluno não possui notas registradas")
        
        medias = []
        for disciplina in disciplinas:
            if disciplina in self.notas and self.notas[disciplina]:
                medias.append(self.calcular_media(disciplina))
        
        if not medias:
            raise ValueError("Aluno não possui notas registradas")
        
        return sum(medias) / len(medias) 