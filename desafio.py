mensagem = "Preciso instalar 2 ventiladores e trocar 4 tomadas."
def analisar_pedido(mensagem):
    pedido = {
       "ventiladores": 2,
       "tomadas": 4
    }
    return pedido
print(analisar_pedido(mensagem))