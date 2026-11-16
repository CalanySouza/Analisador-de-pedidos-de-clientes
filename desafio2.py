mensagem = "Preciso instalar 3 ventiladores e trocar 2 tomadas."

def analisar_pedido (mensagem):
    pedido = {
        "pedido": [
            {
                "descricao": "Instalação de ventiladores",
                "quantidade": 3
            },
            {
                "descricao": "Troca de tomadas",
                "quantidade": 2
            } 
        ]
    } 
    return pedido

resultado = analisar_pedido(mensagem)
print(resultado["pedido"][1]["quantidade"])
for item in resultado["pedido"]:
    print(item["descricao"], item["quantidade"])
    