pedido = {
  "pedido": [
    {
      "descricao": "Instalação de ventiladores",
      "quantidade": 3
    },
    {
      "descricao": "Troca de tomadas",
      "quantidade": 2
    },
    {
      "descricao": "Instalação de Luminárias",
      "quantidade": 4
    }
  ]
}

quantidade_ventiladores = pedido["pedido"][0]["quantidade"]
valor_ventiladores = quantidade_ventiladores * 150
quantidade_tomadas = pedido["pedido"][1]["quantidade"]
valor_tomadas = quantidade_tomadas * 40
total = valor_ventiladores + valor_tomadas
print(total)