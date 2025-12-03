from abc import ABC, abstractmethod
from typing import List

class Pessoa(ABC):
    def __init__(self, id_: int, nome: str):
        self._id = id_
        self._nome = nome

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @abstractmethod
    def resumo(self) -> str:
        pass

class Cliente(Pessoa):
    def __init__(self, id_: int, nome: str, telefone: str, email: str):
        super().__init__(id_, nome)
        self._telefone = telefone
        self._email = email

    def resumo(self) -> str:
        return f"Cliente[{self.id}] {self.nome} - {self._telefone} - {self._email}"

class Tecnico(Pessoa):
    def __init__(self, id_: int, nome: str, especialidade: str):
        super().__init__(id_, nome)
        self._especialidade = especialidade

    def avaliar_produto(self, produto) -> str:
        return f"Técnico {self.nome} avaliou o produto {produto.nome} (garantia={'Sim' if produto.possui_garantia else 'Não'})"

    def executar_servico(self, ordem):
        ordem.status = 'Em execução'
        return f"Técnico {self.nome} está executando a OS {ordem.id}"

    def resumo(self) -> str:
        return f"Técnico[{self.id}] {self.nome} - {self._especialidade}"

class Produto:
    def __init__(self, id_: int, nome: str, marca: str, possui_garantia: bool):
        self._id = id_
        self._nome = nome
        self._marca = marca
        self._possui_garantia = possui_garantia

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def possui_garantia(self):
        return self._possui_garantia

    def verificar_garantia(self) -> bool:
        return self._possui_garantia

    def resumo(self) -> str:
        return f"Produto[{self.id}] {self.nome} - {self._marca} - Garantia: {'Sim' if self._possui_garantia else 'Não'}"

class ItemOS:
    def __init__(self, id_: int, descricao: str, quantidade: int, valor_unitario: float):
        self._id = id_
        self._descricao = descricao
        self._quantidade = quantidade
        self._valor_unitario = valor_unitario

    def calcular_subtotal(self) -> float:
        return self._quantidade * self._valor_unitario

    def resumo(self) -> str:
        return f"Item[{self._id}] {self._descricao} x{self._quantidade} = {self.calcular_subtotal():.2f}"

class OrdemServico:
    _next_id = 1
    def __init__(self, cliente: Cliente, produto: Produto):
        self._id = OrdemServico._next_id
        OrdemServico._next_id += 1
        self._cliente = cliente
        self._produto = produto
        self._itens: List[ItemOS] = []
        self._status = 'Aberta'
        self._tecnico = None

    @property
    def id(self):
        return self._id

    @property
    def cliente(self):
        return self._cliente

    @property
    def produto(self):
        return self._produto

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def tecnico(self):
        return self._tecnico

    def atribuir_tecnico(self, tecnico: Tecnico):
        self._tecnico = tecnico

    def adicionar_item(self, item: ItemOS):
        self._itens.append(item)

    def valor_total(self) -> float:
        return sum(i.calcular_subtotal() for i in self._itens)

    def fechar_os(self):
        self._status = 'Fechada'

    def resumo(self) -> str:
        itens_str = '\\n'.join(i.resumo() for i in self._itens) if self._itens else 'Sem itens'
        return (f"OS[{self.id}] Cliente: {self.cliente.nome} - Produto: {self.produto.nome} - Status: {self.status}\n"
                f"Técnico: {self.tecnico.nome if self.tecnico else 'Não atribuído'}\n"
                f"Itens:\n{itens_str}\nValor Total: {self.valor_total():.2f}")