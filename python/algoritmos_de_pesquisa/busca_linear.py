def busca_linear(item,qnt_item,procurado):
    resposta = -1
    for i in range(qnt_item):
        if item[i] == procurado:
            return i
    return resposta

item = ['teclado','mouse','notebook','python']
qnt = 4
procurado = 'mouse2'

busca = busca_linear(item,qnt,procurado)
print(busca)