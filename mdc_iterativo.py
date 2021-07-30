#MDC – Máximo Divisor Comum: Solução Iterativa

import time
start_time = time.time()
a= int(input("Escreva o primeiro número:"))
b= int(input("Escreva o segundo número:"))

def mdc_iterativo(a,b): # função do mdc_iterativo
    if b > a: # se o número b for maior que o número a então
        a, b = b, a # é feita a inversão para que o número a seja maior

    r= a%b # r é o resto da divisão entre o numerador a pelo denominador b

    while r!=0: # enquanto o resto for diferente de zero
        a=b # a recebe o valor de b
        b=r # b recebe o valor de recebe
        r=a%b # e novamente o processo de divisão se repete até que r seja igual a zero
    return b #Se r é igual a zero, significa que o número

# b é o máximo divisor comum
# b retorna a função e é exibido
print("O mdc entre os dois números é:", mdc_iterativo(a,b))
print("--- %s seconds ---" % (time.time() - start_time))