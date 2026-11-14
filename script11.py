def analisar_pedido(mensagem):
    pedido = {
        "mensagem": mensagem
    }
    return pedido

resultado = analisar_pedido("Preciso instalar 2 ventiladores e trocar 3 tomadas.")
print(resultado)

mensagem = "Preciso instalar 2 ventiladores e trocar 3 tomadas."
pedido = {
    "ventiladores": 2,
    "tomadas": 3,
}
def calcular_total(ventiladores, tomadas):
    valor_ventiladores = ventiladores * 150
    valor_tomadas = tomadas * 40
    total = valor_ventiladores + valor_tomadas

    return total

resultado = calcular_total(pedido["ventiladores"], pedido["tomadas"])
print(resultado)

