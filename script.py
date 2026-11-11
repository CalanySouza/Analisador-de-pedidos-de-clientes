def criar_pedido(nome, servico, valor):
    pedido = {
        "cliente": nome,
        "servico": servico,
        "valor": valor
    }

    return pedido


resultado = criar_pedido(
    "Carlos",
    "Instalação de 2 ventiladores",
    300
)

print(resultado)
def calcular_servico(valor_unitario, quantidade):
    total = valor_unitario * quantidade
    return total


total = calcular_servico(150, 2)

print(total)
def calcular_orcamento(quantidade, valor):
    orcamento = quantidade * valor
    return orcamento
