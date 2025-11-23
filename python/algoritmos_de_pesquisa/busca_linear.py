def busca_linear(item,qnt_item,procurado):
    resposta = -1
    for i in range(qnt_item):
        if item[i] == procurado:
            return i
    return resposta

item = ['teclado','mouse','notebook','python']
qnt = len(item)
procurado = 'python'

busca = busca_linear(item,qnt,procurado)
print(busca)