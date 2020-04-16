import json

print("Digite o número de Autores a serem apresentados")
qtd = int(input())
print("Quantidade de autores é: ", qtd)


arquivo = open('lista_autores.txt', 'r', encoding="utf8")

n = 0
while n < qtd:
    conteudo = arquivo.readline().strip()
    valores=conteudo.split(' ',1)

    sobrenome=valores[1].upper().rstrip()
    nome=valores[0].capitalize()
    if "da" or "de" or "das" or "dos" in valor1:
        var_temp=sobrenome.replace("D","d")
        final=var_temp+","+" "+nome
               
    else:
        final=var_temp+","+" "+nome
    print(final)
    

    

        
    n = n + 1
