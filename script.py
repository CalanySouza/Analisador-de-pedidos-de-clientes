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

def calcular_total(ventiladores, tomadas):
    valor_ventiladores = ventiladores * 150
    valor_tomadas = tomadas * 40
    total = valor_ventiladores + valor_tomadas
    return total

pedido = {
    "ventiladores": 2,
    "tomadas": 3
}
resultado = calcular_total(pedido["ventiladores"], pedido["tomadas"])
print(resultado)

def analisar_pedido(mensagem):
    pedido = {
        "mensagem": mensagem
    }
    return pedido

resultado = analisar_pedido("Preciso instalar 2 ventiladores e trocar 3 tomadas.")
print(resultado)