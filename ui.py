from models import Cliente, Tecnico, Produto, ItemOS, OrdemServico
from persistence import load, save
from typing import List

def criar_amostra():
    # cria dados de amostra
    c = Cliente(1, 'Maria Silva', '1199999-0000', 'maria@ex.com')
    t = Tecnico(1, 'João Pedro', 'Eletrônica')
    p = Produto(1, 'Smartphone X', 'MarcaY', True)
    os1 = OrdemServico(c, p)
    os1.atribuir_tecnico(t)
    os1.adicionar_item(ItemOS(1, 'Troca de Tela', 1, 250.0))
    os1.adicionar_item(ItemOS(2, 'Mão de obra', 1, 150.0))
    return {'clientes':[{'id':c.id,'nome':c.nome,'telefone':'1199999-0000','email':'maria@ex.com'}],
            'tecnicos':[{'id':t.id,'nome':t.nome,'especialidade':'Eletrônica'}],
            'produtos':[{'id':p.id,'nome':p.nome,'marca':'MarcaY','possui_garantia':True}]}

def run_demo():
    data = load()
    if not data:
        data = criar_amostra()
        save(data)
    # demonstra objetos em memória (sem ORM)
    c = Cliente(1, 'Maria Silva', '1199999-0000', 'maria@ex.com')
    t = Tecnico(1, 'João Pedro', 'Eletrônica')
    p = Produto(1, 'Smartphone X', 'MarcaY', True)
    ordem = OrdemServico(c, p)
    ordem.atribuir_tecnico(t)
    ordem.adicionar_item(ItemOS(1, 'Troca de Tela', 1, 250.0))
    ordem.adicionar_item(ItemOS(2, 'Bateria', 1, 80.0))

    print('--- DEMO SISTEMA DE OS ---')
    print(ordem.resumo())
    # Mostrar polimorfismo: chamar resumo de Cliente e Tecnico
    print()
    print('Resumo Cliente:', c.resumo())
    print('Resumo Técnico:', t.resumo())
    print('Produto:', p.resumo())