exp = str(input('Digite a expressão: ')) 
pilha = list()

for simb in exp:  # Percorre cada caractere da expressão.
    if simb == '(':  
        pilha.append('(')  # Adiciona um parêntese aberto à pilha.
    elif simb == ')':  
        if len(pilha) > 0:  # Se a pilha não está vazia (há parênteses abertos a serem fechados):
            pilha.pop()  # Remove o último parêntese aberto da pilha.
        else:  
            pilha.append(')')  # Adiciona um parêntese fechado inválido à pilha.
            break  # Encerra o loop, pois já há um erro na expressão.

# Verifica se a pilha está vazia após o loop:
if len(pilha) == 0:  
    print('Sua expressão esta valida!')  
else:  
    print('Sua expressão esta errada! ') 
     
        
    