def sequencia_crescente(lista):
  #variavel que vai verificar se o valor atual no laço é menor que o próximo
  resultado = ""
  #variavel que vai definir se a lista pode ou não ser uma sequência crescente
  condicao = "false"

  #verificação inicial, se a lista tiver apenas um elemento o resultado será true
  if(len(lista) == 1):
    condicao = "true"
  #se não, iremos fazer algumas verificações
  else:
    #passa por cada indice da lista
    for i in range(len(lista)):
      #cria uma lista vazia que irá armazenar os valores sem um determinado elemento da lista
      lista2 = []
      #novo laço para adicionar os elementos restantes na nova lista
      for k in range(len(lista)):
        #se for diferente do valor do laço, iremos adicionar a nossa nova lisata
        if(k != i):
          lista2.append(lista[k])

      #com a lista já preenchida, vamos verificar se o tamanho da lista é 1, se for, o resultado será true
      if(len(lista2) == 1):
        condicao = "true"
        break
      #se não, vamos verificar se a lista é crescente por meior do nosso laço
      for j in range(len(lista2)-1):
        #se o valor atual for menor que o próximo, a variavel resultado recebe ok e as verificações continuam sendo feitas
        if(lista2[j] < lista2[j+1]):
          resultado = "ok"
        else:
        #se não, o resultado será 'nada ok' e o programa retornará falso
          resultado = "nada ok"
          break
      #verifica o valor final da variável resultado para um determinado número removido da lista original, se for crescente retorna true, se não a lista continuará com suas verificações
      if(resultado == "ok"):
        condicao = "true"
        break

         
    
  #resultado final
  return condicao



#testes
print(sequencia_crescente([1, 3, 2, 1])) 
print(sequencia_crescente([1, 3, 2]))  
print(sequencia_crescente([1, 2, 1, 2])) 
print(sequencia_crescente([3, 6, 5, 8, 10, 20, 15]))  
print(sequencia_crescente([1, 1, 2, 3, 4, 4]))
print(sequencia_crescente([1, 4, 10, 4, 2]))
print(sequencia_crescente([10, 1, 2, 3, 4, 5]))
print(sequencia_crescente([1, 1, 1, 2, 3]))
print(sequencia_crescente([0, -2, 5, 6]))
print(sequencia_crescente([1, 2, 3, 4, 5, 3, 5, 6]))
print(sequencia_crescente([40, 50, 60, 10, 20, 30]))
print(sequencia_crescente([1, 1]))
print(sequencia_crescente([1, 2, 5, 3, 5]))
print(sequencia_crescente([1, 2, 5, 5, 5]))
print(sequencia_crescente([10, 1, 2, 3, 4, 5, 6, 1]))
print(sequencia_crescente([1, 2, 3, 4, 3, 6]))
print(sequencia_crescente([1, 2, 3, 4, 99, 5, 6]))
print(sequencia_crescente([123, -17, -5, 1, 2, 3, 12, 43, 45]))
print(sequencia_crescente([3, 5, 67, 98, 3]))